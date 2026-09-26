source: https://docs.nvidia.com/cuda/npp/signal_statistical_functions.html

# Signal Statistical Functions[](https://docs.nvidia.com#signal-statistical-functions)

Functions that provide global signal statistics like: sum, mean, standard deviation, min, max, etc.

## Signal Min Every Or Max Every[](https://docs.nvidia.com#signal-min-every-or-max-every)

### MinEvery And MaxEvery Functions[](https://docs.nvidia.com#group__signal__min__every__or__max__every_1signal_min_every_or_max_every)

Performs the min or max operation on the samples of a signal.

Functions

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsMinEvery_8u_I_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrcDst, size_t nLength,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsMinEvery_8u_I_Ctx)

-
8-bit in place min value for each pair of elements.

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pSrcDst**–[In-Place Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1in_place_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsMinEvery_16u_I_Ctx(const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrc,[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrcDst, size_t nLength,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsMinEvery_16u_I_Ctx)

-
16-bit unsigned short integer in place min value for each pair of elements.

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pSrcDst**–[In-Place Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1in_place_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsMinEvery_16s_I_Ctx(const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrc,[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrcDst, size_t nLength,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsMinEvery_16s_I_Ctx)

-
16-bit signed short integer in place min value for each pair of elements.

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pSrcDst**–[In-Place Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1in_place_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsMinEvery_32s_I_Ctx(const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pSrc,[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pSrcDst, size_t nLength,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsMinEvery_32s_I_Ctx)

-
32-bit signed integer in place min value for each pair of elements.

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pSrcDst**–[In-Place Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1in_place_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsMinEvery_32f_I_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrcDst, size_t nLength,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsMinEvery_32f_I_Ctx)

-
32-bit floating point in place min value for each pair of elements.

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pSrcDst**–[In-Place Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1in_place_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsMinEvery_64f_I_Ctx(const[Npp64f](https://docs.nvidia.com/nppdefs.html#c.Npp64f)*pSrc,[Npp64f](https://docs.nvidia.com/nppdefs.html#c.Npp64f)*pSrcDst, size_t nLength,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsMinEvery_64f_I_Ctx)

-
64-bit floating point in place min value for each pair of elements.

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pSrcDst**–[In-Place Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1in_place_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsMaxEvery_8u_I_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrcDst, size_t nLength,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsMaxEvery_8u_I_Ctx)

-
8-bit in place max value for each pair of elements.

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pSrcDst**–[In-Place Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1in_place_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsMaxEvery_16u_I_Ctx(const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrc,[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrcDst, size_t nLength,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsMaxEvery_16u_I_Ctx)

-
16-bit unsigned short integer in place max value for each pair of elements.

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pSrcDst**–[In-Place Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1in_place_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsMaxEvery_16s_I_Ctx(const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrc,[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrcDst, size_t nLength,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsMaxEvery_16s_I_Ctx)

-
16-bit signed short integer in place max value for each pair of elements.

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pSrcDst**–[In-Place Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1in_place_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsMaxEvery_32s_I_Ctx(const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pSrc,[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pSrcDst, size_t nLength,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsMaxEvery_32s_I_Ctx)

-
32-bit signed integer in place max value for each pair of elements.

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pSrcDst**–[In-Place Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1in_place_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsMaxEvery_32f_I_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrcDst, size_t nLength,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsMaxEvery_32f_I_Ctx)

-
32-bit floating point in place max value for each pair of elements.

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pSrcDst**–[In-Place Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1in_place_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


## Signal Sum[](https://docs.nvidia.com#signal-sum)

signal_min_every_or_max_every

### Sum[](https://docs.nvidia.com#group__signal__sum_1signal_sum)

Performs the sum operation on the samples of a signal.

Functions

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsSumGetBufferSize_32f_Ctx(size_t nLength, size_t *hpBufferSize,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsSumGetBufferSize_32f_Ctx)

-
Device scratch buffer size (in bytes) for nppsSum_32f.

- Parameters
-
**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**hpBufferSize**– Required buffer size. Important: hpBufferSize is a*host pointer.*[Scratch Buffer and Host Pointer](https://docs.nvidia.com/introduction.html#general_conventions_lb_1general_scratch_buffer).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
NPP_SUCCESS



-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsSumGetBufferSize_32fc_Ctx(size_t nLength, size_t *hpBufferSize,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsSumGetBufferSize_32fc_Ctx)

-
Device scratch buffer size (in bytes) for nppsSum_32fc.

- Parameters
-
**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**hpBufferSize**– Required buffer size. Important: hpBufferSize is a*host pointer.*[Scratch Buffer and Host Pointer](https://docs.nvidia.com/introduction.html#general_conventions_lb_1general_scratch_buffer).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
NPP_SUCCESS



-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsSumGetBufferSize_64f_Ctx(size_t nLength, size_t *hpBufferSize,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsSumGetBufferSize_64f_Ctx)

-
Device scratch buffer size (in bytes) for nppsSum_64f.

- Parameters
-
**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**hpBufferSize**– Required buffer size. Important: hpBufferSize is a*host pointer.*[Scratch Buffer and Host Pointer](https://docs.nvidia.com/introduction.html#general_conventions_lb_1general_scratch_buffer).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
NPP_SUCCESS



-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsSumGetBufferSize_64fc_Ctx(size_t nLength, size_t *hpBufferSize,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsSumGetBufferSize_64fc_Ctx)

-
Device scratch buffer size (in bytes) for nppsSum_64fc.

- Parameters
-
**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**hpBufferSize**– Required buffer size. Important: hpBufferSize is a*host pointer.*[Scratch Buffer and Host Pointer](https://docs.nvidia.com/introduction.html#general_conventions_lb_1general_scratch_buffer).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
NPP_SUCCESS



-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsSumGetBufferSize_16s_Sfs_Ctx(size_t nLength, size_t *hpBufferSize,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsSumGetBufferSize_16s_Sfs_Ctx)

-
Device scratch buffer size (in bytes) for nppsSum_16s_Sfs_Ctx.

- Parameters
-
**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**hpBufferSize**– Required buffer size. Important: hpBufferSize is a*host pointer.*[Scratch Buffer and Host Pointer](https://docs.nvidia.com/introduction.html#general_conventions_lb_1general_scratch_buffer).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
NPP_SUCCESS



-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsSumGetBufferSize_16sc_Sfs_Ctx(size_t nLength, size_t *hpBufferSize,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsSumGetBufferSize_16sc_Sfs_Ctx)

-
Device scratch buffer size (in bytes) for nppsSum_16sc_Sfs_Ctx.

- Parameters
-
**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**hpBufferSize**– Required buffer size. Important: hpBufferSize is a*host pointer.*[Scratch Buffer and Host Pointer](https://docs.nvidia.com/introduction.html#general_conventions_lb_1general_scratch_buffer).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
NPP_SUCCESS



-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsSumGetBufferSize_16sc32sc_Sfs_Ctx(size_t nLength, size_t *hpBufferSize,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsSumGetBufferSize_16sc32sc_Sfs_Ctx)

-
Device scratch buffer size (in bytes) for nppsSum_16sc32sc_Sfs_Ctx.

- Parameters
-
**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**hpBufferSize**– Required buffer size. Important: hpBufferSize is a*host pointer.*[Scratch Buffer and Host Pointer](https://docs.nvidia.com/introduction.html#general_conventions_lb_1general_scratch_buffer).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
NPP_SUCCESS



-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsSumGetBufferSize_32s_Sfs_Ctx(size_t nLength, size_t *hpBufferSize,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsSumGetBufferSize_32s_Sfs_Ctx)

-
Device scratch buffer size (in bytes) for nppsSum_32s_Sfs_Ctx.

- Parameters
-
**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**hpBufferSize**– Required buffer size. Important: hpBufferSize is a*host pointer.*[Scratch Buffer and Host Pointer](https://docs.nvidia.com/introduction.html#general_conventions_lb_1general_scratch_buffer).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
NPP_SUCCESS



-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsSumGetBufferSize_16s32s_Sfs_Ctx(size_t nLength, size_t *hpBufferSize,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsSumGetBufferSize_16s32s_Sfs_Ctx)

-
Device scratch buffer size (in bytes) for nppsSum_16s32s_Sfs_Ctx.

- Parameters
-
**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**hpBufferSize**– Required buffer size. Important: hpBufferSize is a*host pointer.*[Scratch Buffer and Host Pointer](https://docs.nvidia.com/introduction.html#general_conventions_lb_1general_scratch_buffer).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
NPP_SUCCESS



-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsSum_32f_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc, size_t nLength,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSum,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDeviceBuffer,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsSum_32f_Ctx)

-
32-bit float vector sum method

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**pSum**– Device memory pointer to the output result.**pDeviceBuffer**– Pointer to the required device memory allocation,[Scratch Buffer and Host Pointer](https://docs.nvidia.com/introduction.html#general_conventions_lb_1general_scratch_buffer). Use[nppsSumGetBufferSize_32f_Ctx](https://docs.nvidia.com#group__signal__sum_1ga13cd6f4e6caed4a4994e37ff0964a7e9)to determine the minimum number of bytes required.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsSum_32fc_Ctx(const[Npp32fc](https://docs.nvidia.com/nppdefs.html#c.Npp32fc)*pSrc, size_t nLength,[Npp32fc](https://docs.nvidia.com/nppdefs.html#c.Npp32fc)*pSum,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDeviceBuffer,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsSum_32fc_Ctx)

-
32-bit float complex vector sum method

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**pSum**– Device memory pointer to the output result.**pDeviceBuffer**– Pointer to the required device memory allocation,[Scratch Buffer and Host Pointer](https://docs.nvidia.com/introduction.html#general_conventions_lb_1general_scratch_buffer). Use[nppsSumGetBufferSize_32fc_Ctx](https://docs.nvidia.com#group__signal__sum_1ga1befbb2ea6a8b08df7fb1c192555d8b6)to determine the minimum number of bytes required.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsSum_64f_Ctx(const[Npp64f](https://docs.nvidia.com/nppdefs.html#c.Npp64f)*pSrc, size_t nLength,[Npp64f](https://docs.nvidia.com/nppdefs.html#c.Npp64f)*pSum,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDeviceBuffer,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsSum_64f_Ctx)

-
64-bit double vector sum method

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**pSum**– Device memory pointer to the output result.**pDeviceBuffer**– Pointer to the required device memory allocation,[Scratch Buffer and Host Pointer](https://docs.nvidia.com/introduction.html#general_conventions_lb_1general_scratch_buffer). Use[nppsSumGetBufferSize_64f_Ctx](https://docs.nvidia.com#group__signal__sum_1gac04f6adf434b041ce3fefb6dfa5b96b5)to determine the minimum number of bytes required.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsSum_64fc_Ctx(const[Npp64fc](https://docs.nvidia.com/nppdefs.html#c.Npp64fc)*pSrc, size_t nLength,[Npp64fc](https://docs.nvidia.com/nppdefs.html#c.Npp64fc)*pSum,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDeviceBuffer,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsSum_64fc_Ctx)

-
64-bit double complex vector sum method

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**pSum**– Device memory pointer to the output result.**pDeviceBuffer**– Pointer to the required device memory allocation,[Scratch Buffer and Host Pointer](https://docs.nvidia.com/introduction.html#general_conventions_lb_1general_scratch_buffer). Use[nppsSumGetBufferSize_64fc_Ctx](https://docs.nvidia.com#group__signal__sum_1ga82a9938452ae60b371f46fa64def1217)to determine the minimum number of bytes required.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsSum_16s_Sfs_Ctx(const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrc, size_t nLength,[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSum, int nScaleFactor,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDeviceBuffer,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsSum_16s_Sfs_Ctx)

-
16-bit short vector sum with integer scaling method

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**pSum**– Device memory pointer to the output result.**pDeviceBuffer**– Pointer to the required device memory allocation,[Scratch Buffer and Host Pointer](https://docs.nvidia.com/introduction.html#general_conventions_lb_1general_scratch_buffer). Use[nppsSumGetBufferSize_16s_Sfs_Ctx](https://docs.nvidia.com#group__signal__sum_1ga7c69e837cf6897188adbef6bbaa7a683)to determine the minimum number of bytes required.**nScaleFactor**–[Integer Result Scaling](https://docs.nvidia.com/introduction.html#general_conventions_lb_1integer_result_scaling).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsSum_32s_Sfs_Ctx(const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pSrc, size_t nLength,[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pSum, int nScaleFactor,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDeviceBuffer,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsSum_32s_Sfs_Ctx)

-
32-bit integer vector sum with integer scaling method

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**pSum**– Device memory pointer to the output result.**pDeviceBuffer**– Pointer to the required device memory allocation,[Scratch Buffer and Host Pointer](https://docs.nvidia.com/introduction.html#general_conventions_lb_1general_scratch_buffer). Use[nppsSumGetBufferSize_32s_Sfs_Ctx](https://docs.nvidia.com#group__signal__sum_1gaec9b51f43d578d3566bd80bb66470ed5)to determine the minimum number of bytes required.**nScaleFactor**–[Integer Result Scaling](https://docs.nvidia.com/introduction.html#general_conventions_lb_1integer_result_scaling).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsSum_16sc_Sfs_Ctx(const[Npp16sc](https://docs.nvidia.com/nppdefs.html#c.Npp16sc)*pSrc, size_t nLength,[Npp16sc](https://docs.nvidia.com/nppdefs.html#c.Npp16sc)*pSum, int nScaleFactor,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDeviceBuffer,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsSum_16sc_Sfs_Ctx)

-
16-bit short complex vector sum with integer scaling method

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**pSum**– Device memory pointer to the output result.**pDeviceBuffer**– Pointer to the required device memory allocation,[Scratch Buffer and Host Pointer](https://docs.nvidia.com/introduction.html#general_conventions_lb_1general_scratch_buffer). Use[nppsSumGetBufferSize_16sc_Sfs_Ctx](https://docs.nvidia.com#group__signal__sum_1ga098fb900500465a7736e371562b7db20)to determine the minimum number of bytes required.**nScaleFactor**–[Integer Result Scaling](https://docs.nvidia.com/introduction.html#general_conventions_lb_1integer_result_scaling).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsSum_16sc32sc_Sfs_Ctx(const[Npp16sc](https://docs.nvidia.com/nppdefs.html#c.Npp16sc)*pSrc, size_t nLength,[Npp32sc](https://docs.nvidia.com/nppdefs.html#c.Npp32sc)*pSum, int nScaleFactor,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDeviceBuffer,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsSum_16sc32sc_Sfs_Ctx)

-
16-bit short complex vector sum (32bit int complex) with integer scaling method

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**pSum**– Device memory pointer to the output result.**pDeviceBuffer**– Pointer to the required device memory allocation,[Scratch Buffer and Host Pointer](https://docs.nvidia.com/introduction.html#general_conventions_lb_1general_scratch_buffer). Use[nppsSumGetBufferSize_16sc32sc_Sfs_Ctx](https://docs.nvidia.com#group__signal__sum_1ga6e5d45d2636c413c79ea1bf0d453608f)to determine the minimum number of bytes required.**nScaleFactor**–[Integer Result Scaling](https://docs.nvidia.com/introduction.html#general_conventions_lb_1integer_result_scaling).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsSum_16s32s_Sfs_Ctx(const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrc, size_t nLength,[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pSum, int nScaleFactor,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDeviceBuffer,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsSum_16s32s_Sfs_Ctx)

-
16-bit integer vector sum (32bit) with integer scaling method

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**pSum**– Device memory pointer to the output result.**pDeviceBuffer**– Pointer to the required device memory allocation,[Scratch Buffer and Host Pointer](https://docs.nvidia.com/introduction.html#general_conventions_lb_1general_scratch_buffer). Use[nppsSumGetBufferSize_16s32s_Sfs_Ctx](https://docs.nvidia.com#group__signal__sum_1ga458aaba55927e0922bdc1641020bfdc9)to determine the minimum number of bytes required.**nScaleFactor**–[Integer Result Scaling](https://docs.nvidia.com/introduction.html#general_conventions_lb_1integer_result_scaling).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


## Signal Maximum[](https://docs.nvidia.com#signal-maximum)

### Maximum[](https://docs.nvidia.com#group__signal__max_1signal_max)

Performs the maximum operation on the samples of a signal.

Functions

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsMaxGetBufferSize_16s_Ctx(size_t nLength, size_t *hpBufferSize,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsMaxGetBufferSize_16s_Ctx)

-
Device scratch buffer size (in bytes) for nppsMax_16s.

- Parameters
-
**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**hpBufferSize**– Required buffer size. Important: hpBufferSize is a*host pointer.*[Scratch Buffer and Host Pointer](https://docs.nvidia.com/introduction.html#general_conventions_lb_1general_scratch_buffer).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
NPP_SUCCESS



-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsMaxGetBufferSize_32s_Ctx(size_t nLength, size_t *hpBufferSize,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsMaxGetBufferSize_32s_Ctx)

-
Device scratch buffer size (in bytes) for nppsMax_32s.

- Parameters
-
**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**hpBufferSize**– Required buffer size. Important: hpBufferSize is a*host pointer.*[Scratch Buffer and Host Pointer](https://docs.nvidia.com/introduction.html#general_conventions_lb_1general_scratch_buffer).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
NPP_SUCCESS



-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsMaxGetBufferSize_32f_Ctx(size_t nLength, size_t *hpBufferSize,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsMaxGetBufferSize_32f_Ctx)

-
Device scratch buffer size (in bytes) for nppsMax_32f.

- Parameters
-
**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**hpBufferSize**– Required buffer size. Important: hpBufferSize is a*host pointer.*[Scratch Buffer and Host Pointer](https://docs.nvidia.com/introduction.html#general_conventions_lb_1general_scratch_buffer).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
NPP_SUCCESS



-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsMaxGetBufferSize_64f_Ctx(size_t nLength, size_t *hpBufferSize,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsMaxGetBufferSize_64f_Ctx)

-
Device scratch buffer size (in bytes) for nppsMax_64f.

- Parameters
-
**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**hpBufferSize**– Required buffer size. Important: hpBufferSize is a*host pointer.*[Scratch Buffer and Host Pointer](https://docs.nvidia.com/introduction.html#general_conventions_lb_1general_scratch_buffer).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
NPP_SUCCESS



-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsMax_16s_Ctx(const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrc, size_t nLength,[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pMax,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDeviceBuffer,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsMax_16s_Ctx)

-
16-bit integer vector max method

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**pMax**– Device memory pointer to the output result.**pDeviceBuffer**– Pointer to the required device memory allocation,[Scratch Buffer and Host Pointer](https://docs.nvidia.com/introduction.html#general_conventions_lb_1general_scratch_buffer). Use[nppsMaxGetBufferSize_16s_Ctx](https://docs.nvidia.com#group__signal__max_1gae6e35623ff0f2e5e4e348177d8853efe)to determine the minimum number of bytes required.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsMax_32s_Ctx(const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pSrc, size_t nLength,[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pMax,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDeviceBuffer,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsMax_32s_Ctx)

-
32-bit integer vector max method

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**pMax**– Device memory pointer to the output result.**pDeviceBuffer**– Pointer to the required device memory allocation,[Scratch Buffer and Host Pointer](https://docs.nvidia.com/introduction.html#general_conventions_lb_1general_scratch_buffer). Use[nppsMaxGetBufferSize_32s_Ctx](https://docs.nvidia.com#group__signal__max_1ga7dd774f3c86ac2985a7deecd6fefb3a2)to determine the minimum number of bytes required.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsMax_32f_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc, size_t nLength,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pMax,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDeviceBuffer,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsMax_32f_Ctx)

-
32-bit float vector max method

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**pMax**– Device memory pointer to the output result.**pDeviceBuffer**– Pointer to the required device memory allocation,[Scratch Buffer and Host Pointer](https://docs.nvidia.com/introduction.html#general_conventions_lb_1general_scratch_buffer). Use[nppsMaxGetBufferSize_32f_Ctx](https://docs.nvidia.com#group__signal__max_1ga419ab1d877b04e5446c90389da3052af)to determine the minimum number of bytes required.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsMax_64f_Ctx(const[Npp64f](https://docs.nvidia.com/nppdefs.html#c.Npp64f)*pSrc, size_t nLength,[Npp64f](https://docs.nvidia.com/nppdefs.html#c.Npp64f)*pMax,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDeviceBuffer,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsMax_64f_Ctx)

-
64-bit float vector max method

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**pMax**– Device memory pointer to the output result.**pDeviceBuffer**– Pointer to the required device memory allocation,[Scratch Buffer and Host Pointer](https://docs.nvidia.com/introduction.html#general_conventions_lb_1general_scratch_buffer). Use[nppsMaxGetBufferSize_64f_Ctx](https://docs.nvidia.com#group__signal__max_1ga9720267d499b0728c4169c98007faec7)to determine the minimum number of bytes required.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsMaxIndxGetBufferSize_16s_Ctx(size_t nLength, size_t *hpBufferSize,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsMaxIndxGetBufferSize_16s_Ctx)

-
Device scratch buffer size (in bytes) for nppsMaxIndx_16s.

- Parameters
-
**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**hpBufferSize**– Required buffer size. Important: hpBufferSize is a*host pointer.*[Scratch Buffer and Host Pointer](https://docs.nvidia.com/introduction.html#general_conventions_lb_1general_scratch_buffer).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
NPP_SUCCESS



-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsMaxIndxGetBufferSize_32s_Ctx(size_t nLength, size_t *hpBufferSize,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsMaxIndxGetBufferSize_32s_Ctx)

-
Device scratch buffer size (in bytes) for nppsMaxIndx_32s.

- Parameters
-
**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**hpBufferSize**– Required buffer size. Important: hpBufferSize is a*host pointer.*[Scratch Buffer and Host Pointer](https://docs.nvidia.com/introduction.html#general_conventions_lb_1general_scratch_buffer).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
NPP_SUCCESS



-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsMaxIndxGetBufferSize_32f_Ctx(size_t nLength, size_t *hpBufferSize,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsMaxIndxGetBufferSize_32f_Ctx)

-
Device scratch buffer size (in bytes) for nppsMaxIndx_32f.

- Parameters
-
**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**hpBufferSize**– Required buffer size. Important: hpBufferSize is a*host pointer.*[Scratch Buffer and Host Pointer](https://docs.nvidia.com/introduction.html#general_conventions_lb_1general_scratch_buffer).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
NPP_SUCCESS



-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsMaxIndxGetBufferSize_64f_Ctx(size_t nLength, size_t *hpBufferSize,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsMaxIndxGetBufferSize_64f_Ctx)

-
Device scratch buffer size (in bytes) for nppsMaxIndx_64f.

- Parameters
-
**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**hpBufferSize**– Required buffer size. Important: hpBufferSize is a*host pointer.*[Scratch Buffer and Host Pointer](https://docs.nvidia.com/introduction.html#general_conventions_lb_1general_scratch_buffer).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
NPP_SUCCESS



-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsMaxIndx_16s_Ctx(const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrc, size_t nLength,[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pMax, int *pIndx,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDeviceBuffer,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsMaxIndx_16s_Ctx)

-
16-bit integer vector max index method

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**pMax**– Device memory pointer to the output result.**pIndx**– Device memory pointer to the index value of the first maximum element.**pDeviceBuffer**– Pointer to the required device memory allocation,[Scratch Buffer and Host Pointer](https://docs.nvidia.com/introduction.html#general_conventions_lb_1general_scratch_buffer). Use[nppsMaxIndxGetBufferSize_16s_Ctx](https://docs.nvidia.com#group__signal__max_1ga626b75fb6728926f246fcdbf9ac367f6)to determine the minimum number of bytes required.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsMaxIndx_32s_Ctx(const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pSrc, size_t nLength,[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pMax, int *pIndx,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDeviceBuffer,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsMaxIndx_32s_Ctx)

-
32-bit integer vector max index method

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**pMax**– Device memory pointer to the output result.**pIndx**– Device memory pointer to the index value of the first maximum element.**pDeviceBuffer**– Pointer to the required device memory allocation,[Scratch Buffer and Host Pointer](https://docs.nvidia.com/introduction.html#general_conventions_lb_1general_scratch_buffer). Use[nppsMaxIndxGetBufferSize_32s_Ctx](https://docs.nvidia.com#group__signal__max_1ga64833494f5e9efa5b2018b95865083ab)to determine the minimum number of bytes required.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsMaxIndx_32f_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc, size_t nLength,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pMax, int *pIndx,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDeviceBuffer,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsMaxIndx_32f_Ctx)

-
32-bit float vector max index method

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**pMax**– Device memory pointer to the output result.**pIndx**– Device memory pointer to the index value of the first maximum element.**pDeviceBuffer**– Pointer to the required device memory allocation,[Scratch Buffer and Host Pointer](https://docs.nvidia.com/introduction.html#general_conventions_lb_1general_scratch_buffer). Use[nppsMaxIndxGetBufferSize_32f_Ctx](https://docs.nvidia.com#group__signal__max_1gae4c9982c3d25c333812599d033404e1b)to determine the minimum number of bytes required.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsMaxIndx_64f_Ctx(const[Npp64f](https://docs.nvidia.com/nppdefs.html#c.Npp64f)*pSrc, size_t nLength,[Npp64f](https://docs.nvidia.com/nppdefs.html#c.Npp64f)*pMax, int *pIndx,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDeviceBuffer,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsMaxIndx_64f_Ctx)

-
64-bit float vector max index method

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**pMax**– Device memory pointer to the output result.**pIndx**– Device memory pointer to the index value of the first maximum element.**pDeviceBuffer**– Pointer to the required device memory allocation,[Scratch Buffer and Host Pointer](https://docs.nvidia.com/introduction.html#general_conventions_lb_1general_scratch_buffer). Use[nppsMaxIndxGetBufferSize_64f_Ctx](https://docs.nvidia.com#group__signal__max_1gac1420eaf3b62c4449589d9a78909d536)to determine the minimum number of bytes required.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsMaxAbsGetBufferSize_16s_Ctx(size_t nLength, size_t *hpBufferSize,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsMaxAbsGetBufferSize_16s_Ctx)

-
Device scratch buffer size (in bytes) for nppsMaxAbs_16s_Ctx.

- Parameters
-
**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**hpBufferSize**– Required buffer size. Important: hpBufferSize is a*host pointer.*[Scratch Buffer and Host Pointer](https://docs.nvidia.com/introduction.html#general_conventions_lb_1general_scratch_buffer).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
NPP_SUCCESS



-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsMaxAbsGetBufferSize_32s_Ctx(size_t nLength, size_t *hpBufferSize,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsMaxAbsGetBufferSize_32s_Ctx)

-
Device scratch buffer size (in bytes) for nppsMaxAbs_32s.

- Parameters
-
**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**hpBufferSize**– Required buffer size. Important: hpBufferSize is a*host pointer.*[Scratch Buffer and Host Pointer](https://docs.nvidia.com/introduction.html#general_conventions_lb_1general_scratch_buffer).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
NPP_SUCCESS



-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsMaxAbs_16s_Ctx(const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrc, size_t nLength,[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pMaxAbs,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDeviceBuffer,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsMaxAbs_16s_Ctx)

-
16-bit integer vector max absolute method

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**pMaxAbs**– Device memory pointer to the output result.**pDeviceBuffer**– Pointer to the required device memory allocation,[Scratch Buffer and Host Pointer](https://docs.nvidia.com/introduction.html#general_conventions_lb_1general_scratch_buffer). Use[nppsMaxAbsGetBufferSize_16s_Ctx](https://docs.nvidia.com#group__signal__max_1gad10e5eb602df002ba15bf5590c8cb476)to determine the minimum number of bytes required.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsMaxAbs_32s_Ctx(const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pSrc, size_t nLength,[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pMaxAbs,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDeviceBuffer,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsMaxAbs_32s_Ctx)

-
32-bit integer vector max absolute method

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**pMaxAbs**– Device memory pointer to the output result.**pDeviceBuffer**– Pointer to the required device memory allocation,[Scratch Buffer and Host Pointer](https://docs.nvidia.com/introduction.html#general_conventions_lb_1general_scratch_buffer). Use[nppsMaxAbsGetBufferSize_32s_Ctx](https://docs.nvidia.com#group__signal__max_1ga541287c8720444a1aa5a3a42a83c8753)to determine the minimum number of bytes required.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsMaxAbsIndxGetBufferSize_16s_Ctx(size_t nLength, size_t *hpBufferSize,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsMaxAbsIndxGetBufferSize_16s_Ctx)

-
Device scratch buffer size (in bytes) for nppsMaxAbsIndx_16s.

- Parameters
-
**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**hpBufferSize**– Required buffer size. Important: hpBufferSize is a*host pointer.*[Scratch Buffer and Host Pointer](https://docs.nvidia.com/introduction.html#general_conventions_lb_1general_scratch_buffer).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
NPP_SUCCESS



-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsMaxAbsIndxGetBufferSize_32s_Ctx(size_t nLength, size_t *hpBufferSize,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsMaxAbsIndxGetBufferSize_32s_Ctx)

-
Device scratch buffer size (in bytes) for nppsMaxAbsIndx_32s.

- Parameters
-
**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**hpBufferSize**– Required buffer size. Important: hpBufferSize is a*host pointer.*[Scratch Buffer and Host Pointer](https://docs.nvidia.com/introduction.html#general_conventions_lb_1general_scratch_buffer).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
NPP_SUCCESS



-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsMaxAbsIndx_16s_Ctx(const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrc, size_t nLength,[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pMaxAbs, int *pIndx,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDeviceBuffer,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsMaxAbsIndx_16s_Ctx)

-
16-bit integer vector max absolute index method

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**pMaxAbs**– Device memory pointer to the output result.**pIndx**– Device memory pointer to the index value of the first maximum element.**pDeviceBuffer**– Pointer to the required device memory allocation,[Scratch Buffer and Host Pointer](https://docs.nvidia.com/introduction.html#general_conventions_lb_1general_scratch_buffer). Use[nppsMaxAbsIndxGetBufferSize_16s_Ctx](https://docs.nvidia.com#group__signal__max_1ga80b567b7328e1c349d11eb429ca9e345)to determine the minimum number of bytes required.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsMaxAbsIndx_32s_Ctx(const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pSrc, size_t nLength,[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pMaxAbs, int *pIndx,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDeviceBuffer,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsMaxAbsIndx_32s_Ctx)

-
32-bit integer vector max absolute index method

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**pMaxAbs**– Device memory pointer to the output result.**pIndx**– Device memory pointer to the index value of the first maximum element.**pDeviceBuffer**– Pointer to the required device memory allocation,[Scratch Buffer and Host Pointer](https://docs.nvidia.com/introduction.html#general_conventions_lb_1general_scratch_buffer). Use[nppsMaxAbsIndxGetBufferSize_32s_Ctx](https://docs.nvidia.com#group__signal__max_1ga45a792c96ade7f9e6dbe50d755bd9e61)to determine the minimum number of bytes required.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


## Signal Minimum[](https://docs.nvidia.com#signal-minimum)

### Minimum[](https://docs.nvidia.com#group__signal__min_1signal_min)

Performs the minimum operation on the samples of a signal.

Functions

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsMinGetBufferSize_16s_Ctx(size_t nLength, size_t *hpBufferSize,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsMinGetBufferSize_16s_Ctx)

-
Device scratch buffer size (in bytes) for nppsMin_16s.

- Parameters
-
**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**hpBufferSize**– Required buffer size. Important: hpBufferSize is a*host pointer.*[Scratch Buffer and Host Pointer](https://docs.nvidia.com/introduction.html#general_conventions_lb_1general_scratch_buffer).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
NPP_SUCCESS



-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsMinGetBufferSize_32s_Ctx(size_t nLength, size_t *hpBufferSize,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsMinGetBufferSize_32s_Ctx)

-
Device scratch buffer size (in bytes) for nppsMin_32s.

- Parameters
-
**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**hpBufferSize**– Required buffer size. Important: hpBufferSize is a*host pointer.*[Scratch Buffer and Host Pointer](https://docs.nvidia.com/introduction.html#general_conventions_lb_1general_scratch_buffer).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
NPP_SUCCESS



-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsMinGetBufferSize_32f_Ctx(size_t nLength, size_t *hpBufferSize,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsMinGetBufferSize_32f_Ctx)

-
Device scratch buffer size (in bytes) for nppsMin_32f.

- Parameters
-
**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**hpBufferSize**– Required buffer size. Important: hpBufferSize is a*host pointer.*[Scratch Buffer and Host Pointer](https://docs.nvidia.com/introduction.html#general_conventions_lb_1general_scratch_buffer).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
NPP_SUCCESS



-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsMinGetBufferSize_64f_Ctx(size_t nLength, size_t *hpBufferSize,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsMinGetBufferSize_64f_Ctx)

-
Device scratch buffer size (in bytes) for nppsMin_64f.

- Parameters
-
**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**hpBufferSize**– Required buffer size. Important: hpBufferSize is a*host pointer.*[Scratch Buffer and Host Pointer](https://docs.nvidia.com/introduction.html#general_conventions_lb_1general_scratch_buffer).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
NPP_SUCCESS



-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsMin_16s_Ctx(const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrc, size_t nLength,[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pMin,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDeviceBuffer,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsMin_16s_Ctx)

-
16-bit integer vector min method

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**pMin**– Device memory pointer to the output result.**pDeviceBuffer**– Pointer to the required device memory allocation,[Scratch Buffer and Host Pointer](https://docs.nvidia.com/introduction.html#general_conventions_lb_1general_scratch_buffer). Use[nppsMinGetBufferSize_16s_Ctx](https://docs.nvidia.com#group__signal__min_1ga63cf1283b3abfa9635c7b0a26bbca1fb)to determine the minimum number of bytes required.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsMin_32s_Ctx(const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pSrc, size_t nLength,[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pMin,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDeviceBuffer,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsMin_32s_Ctx)

-
32-bit integer vector min method

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**pMin**– Device memory pointer to the output result.**pDeviceBuffer**– Pointer to the required device memory allocation,[Scratch Buffer and Host Pointer](https://docs.nvidia.com/introduction.html#general_conventions_lb_1general_scratch_buffer). Use[nppsMinGetBufferSize_32s_Ctx](https://docs.nvidia.com#group__signal__min_1ga62ef99fa1313fbaa5bea5d8ec879379c)to determine the minimum number of bytes required.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsMin_32f_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc, size_t nLength,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pMin,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDeviceBuffer,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsMin_32f_Ctx)

-
32-bit integer vector min method

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**pMin**– Device memory pointer to the output result.**pDeviceBuffer**– Pointer to the required device memory allocation,[Scratch Buffer and Host Pointer](https://docs.nvidia.com/introduction.html#general_conventions_lb_1general_scratch_buffer). Use[nppsMinGetBufferSize_32f_Ctx](https://docs.nvidia.com#group__signal__min_1ga00d531278785b8ad573dba1594c08922)to determine the minimum number of bytes required.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsMin_64f_Ctx(const[Npp64f](https://docs.nvidia.com/nppdefs.html#c.Npp64f)*pSrc, size_t nLength,[Npp64f](https://docs.nvidia.com/nppdefs.html#c.Npp64f)*pMin,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDeviceBuffer,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsMin_64f_Ctx)

-
64-bit integer vector min method

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**pMin**– Device memory pointer to the output result.**pDeviceBuffer**– Pointer to the required device memory allocation,[Scratch Buffer and Host Pointer](https://docs.nvidia.com/introduction.html#general_conventions_lb_1general_scratch_buffer). Use[nppsMinGetBufferSize_64f_Ctx](https://docs.nvidia.com#group__signal__min_1ga854e700dd2f4a81cc8e730c2ff203da8)to determine the minimum number of bytes required.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsMinIndxGetBufferSize_16s_Ctx(size_t nLength, size_t *hpBufferSize,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsMinIndxGetBufferSize_16s_Ctx)

-
Device scratch buffer size (in bytes) for nppsMinIndx_16s.

- Parameters
-
**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**hpBufferSize**– Required buffer size. Important: hpBufferSize is a*host pointer.*[Scratch Buffer and Host Pointer](https://docs.nvidia.com/introduction.html#general_conventions_lb_1general_scratch_buffer).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
NPP_SUCCESS



-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsMinIndxGetBufferSize_32s_Ctx(size_t nLength, size_t *hpBufferSize,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsMinIndxGetBufferSize_32s_Ctx)

-
Device scratch buffer size (in bytes) for nppsMinIndx_32s.

- Parameters
-
**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**hpBufferSize**– Required buffer size. Important: hpBufferSize is a*host pointer.*[Scratch Buffer and Host Pointer](https://docs.nvidia.com/introduction.html#general_conventions_lb_1general_scratch_buffer).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
NPP_SUCCESS



-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsMinIndxGetBufferSize_32f_Ctx(size_t nLength, size_t *hpBufferSize,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsMinIndxGetBufferSize_32f_Ctx)

-
Device scratch buffer size (in bytes) for nppsMinIndx_32f.

- Parameters
-
**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**hpBufferSize**– Required buffer size. Important: hpBufferSize is a*host pointer.*[Scratch Buffer and Host Pointer](https://docs.nvidia.com/introduction.html#general_conventions_lb_1general_scratch_buffer).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
NPP_SUCCESS



-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsMinIndxGetBufferSize_64f_Ctx(size_t nLength, size_t *hpBufferSize,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsMinIndxGetBufferSize_64f_Ctx)

-
Device scratch buffer size (in bytes) for nppsMinIndx_64f.

- Parameters
-
**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**hpBufferSize**– Required buffer size. Important: hpBufferSize is a*host pointer.*[Scratch Buffer and Host Pointer](https://docs.nvidia.com/introduction.html#general_conventions_lb_1general_scratch_buffer).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
NPP_SUCCESS



-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsMinIndx_16s_Ctx(const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrc, size_t nLength,[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pMin, int *pIndx,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDeviceBuffer,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsMinIndx_16s_Ctx)

-
16-bit integer vector min index method

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**pMin**– Device memory pointer to the output result.**pIndx**– Device memory pointer to the index value of the first minimum element.**pDeviceBuffer**– Pointer to the required device memory allocation,[Scratch Buffer and Host Pointer](https://docs.nvidia.com/introduction.html#general_conventions_lb_1general_scratch_buffer). Use[nppsMinIndxGetBufferSize_16s_Ctx](https://docs.nvidia.com#group__signal__min_1ga717f97d18d4c8c7e153c92c3e807799e)to determine the minimum number of bytes required.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsMinIndx_32s_Ctx(const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pSrc, size_t nLength,[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pMin, int *pIndx,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDeviceBuffer,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsMinIndx_32s_Ctx)

-
32-bit integer vector min index method

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**pMin**– Device memory pointer to the output result.**pIndx**– Device memory pointer to the index value of the first minimum element.**pDeviceBuffer**– Pointer to the required device memory allocation,[Scratch Buffer and Host Pointer](https://docs.nvidia.com/introduction.html#general_conventions_lb_1general_scratch_buffer). Use[nppsMinIndxGetBufferSize_32s_Ctx](https://docs.nvidia.com#group__signal__min_1ga5a411b8868b6088e40c1ad24e1dc75d3)to determine the minimum number of bytes required.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsMinIndx_32f_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc, size_t nLength,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pMin, int *pIndx,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDeviceBuffer,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsMinIndx_32f_Ctx)

-
32-bit float vector min index method

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**pMin**– Device memory pointer to the output result.**pIndx**– Device memory pointer to the index value of the first minimum element.**pDeviceBuffer**– Pointer to the required device memory allocation,[Scratch Buffer and Host Pointer](https://docs.nvidia.com/introduction.html#general_conventions_lb_1general_scratch_buffer). Use[nppsMinIndxGetBufferSize_32f_Ctx](https://docs.nvidia.com#group__signal__min_1gab24bb49aeb276da40acb1ee2c4e305e3)to determine the minimum number of bytes required.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsMinIndx_64f_Ctx(const[Npp64f](https://docs.nvidia.com/nppdefs.html#c.Npp64f)*pSrc, size_t nLength,[Npp64f](https://docs.nvidia.com/nppdefs.html#c.Npp64f)*pMin, int *pIndx,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDeviceBuffer,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsMinIndx_64f_Ctx)

-
64-bit float vector min index method

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**pMin**– Device memory pointer to the output result.**pIndx**– Device memory pointer to the index value of the first minimum element.**pDeviceBuffer**– Pointer to the required device memory allocation,[Scratch Buffer and Host Pointer](https://docs.nvidia.com/introduction.html#general_conventions_lb_1general_scratch_buffer). Use[nppsMinIndxGetBufferSize_64f_Ctx](https://docs.nvidia.com#group__signal__min_1ga11cfdab2f04e4387adaec0b97aa7cbba)to determine the minimum number of bytes required.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsMinAbsGetBufferSize_16s_Ctx(size_t nLength, size_t *hpBufferSize,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsMinAbsGetBufferSize_16s_Ctx)

-
Device scratch buffer size (in bytes) for nppsMinAbs_16s.

- Parameters
-
**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**hpBufferSize**– Required buffer size. Important: hpBufferSize is a*host pointer.*[Scratch Buffer and Host Pointer](https://docs.nvidia.com/introduction.html#general_conventions_lb_1general_scratch_buffer).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
NPP_SUCCESS



-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsMinAbsGetBufferSize_32s_Ctx(size_t nLength, size_t *hpBufferSize,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsMinAbsGetBufferSize_32s_Ctx)

-
Device scratch buffer size (in bytes) for nppsMinAbs_32s.

- Parameters
-
**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**hpBufferSize**– Required buffer size. Important: hpBufferSize is a*host pointer.*[Scratch Buffer and Host Pointer](https://docs.nvidia.com/introduction.html#general_conventions_lb_1general_scratch_buffer).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
NPP_SUCCESS



-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsMinAbs_16s_Ctx(const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrc, size_t nLength,[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pMinAbs,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDeviceBuffer,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsMinAbs_16s_Ctx)

-
16-bit integer vector min absolute method

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**pMinAbs**– Device memory pointer to the output result.**pDeviceBuffer**– Pointer to the required device memory allocation,[Scratch Buffer and Host Pointer](https://docs.nvidia.com/introduction.html#general_conventions_lb_1general_scratch_buffer). Use[nppsMinAbsGetBufferSize_16s_Ctx](https://docs.nvidia.com#group__signal__min_1ga77f88fb82629ecbdeada1df9fee9dd56)to determine the minimum number of bytes required.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsMinAbs_32s_Ctx(const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pSrc, size_t nLength,[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pMinAbs,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDeviceBuffer,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsMinAbs_32s_Ctx)

-
32-bit integer vector min absolute method

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**pMinAbs**– Device memory pointer to the output result.**pDeviceBuffer**– Pointer to the required device memory allocation,[Scratch Buffer and Host Pointer](https://docs.nvidia.com/introduction.html#general_conventions_lb_1general_scratch_buffer). Use[nppsMinAbsGetBufferSize_16s_Ctx](https://docs.nvidia.com#group__signal__min_1ga77f88fb82629ecbdeada1df9fee9dd56)to determine the minimum number of bytes required.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsMinAbsIndxGetBufferSize_16s_Ctx(size_t nLength, size_t *hpBufferSize,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsMinAbsIndxGetBufferSize_16s_Ctx)

-
Device scratch buffer size (in bytes) for nppsMinAbsIndx_16s.

- Parameters
-
**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**hpBufferSize**– Required buffer size. Important: hpBufferSize is a*host pointer.*[Scratch Buffer and Host Pointer](https://docs.nvidia.com/introduction.html#general_conventions_lb_1general_scratch_buffer).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
NPP_SUCCESS



-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsMinAbsIndxGetBufferSize_32s_Ctx(size_t nLength, size_t *hpBufferSize,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsMinAbsIndxGetBufferSize_32s_Ctx)

-
Device scratch buffer size (in bytes) for nppsMinAbsIndx_32s.

- Parameters
-
**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**hpBufferSize**– Required buffer size. Important: hpBufferSize is a*host pointer.*[Scratch Buffer and Host Pointer](https://docs.nvidia.com/introduction.html#general_conventions_lb_1general_scratch_buffer).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
NPP_SUCCESS



-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsMinAbsIndx_16s_Ctx(const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrc, size_t nLength,[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pMinAbs, int *pIndx,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDeviceBuffer,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsMinAbsIndx_16s_Ctx)

-
16-bit integer vector min absolute index method

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**pMinAbs**– Device memory pointer to the output result.**pIndx**– Device memory pointer to the index value of the first minimum element.**pDeviceBuffer**– Pointer to the required device memory allocation,[Scratch Buffer and Host Pointer](https://docs.nvidia.com/introduction.html#general_conventions_lb_1general_scratch_buffer). Use[nppsMinAbsIndxGetBufferSize_16s_Ctx](https://docs.nvidia.com#group__signal__min_1ga40f82cd6b0f705210a90542d469c3fcd)to determine the minimum number of bytes required.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsMinAbsIndx_32s_Ctx(const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pSrc, size_t nLength,[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pMinAbs, int *pIndx,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDeviceBuffer,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsMinAbsIndx_32s_Ctx)

-
32-bit integer vector min absolute index method

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**pMinAbs**– Device memory pointer to the output result.**pIndx**– Device memory pointer to the index value of the first minimum element.**pDeviceBuffer**– Pointer to the required device memory allocation,[Scratch Buffer and Host Pointer](https://docs.nvidia.com/introduction.html#general_conventions_lb_1general_scratch_buffer). Use[nppsMinAbsIndxGetBufferSize_32s_Ctx](https://docs.nvidia.com#group__signal__min_1ga1ec37d8c2f23aa17dcabcbff760095d1)to determine the minimum number of bytes required.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


## Signal Mean[](https://docs.nvidia.com#signal-mean)

### Mean[](https://docs.nvidia.com#group__signal__mean_1signal_mean)

Performs the mean operation on the samples of a signal.

Functions

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsMeanGetBufferSize_32f_Ctx(size_t nLength, size_t *hpBufferSize,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsMeanGetBufferSize_32f_Ctx)

-
Device scratch buffer size (in bytes) for nppsMean_32f.

- Parameters
-
**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**hpBufferSize**– Required buffer size. Important: hpBufferSize is a*host pointer.*[Scratch Buffer and Host Pointer](https://docs.nvidia.com/introduction.html#general_conventions_lb_1general_scratch_buffer).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
NPP_SUCCESS



-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsMeanGetBufferSize_32fc_Ctx(size_t nLength, size_t *hpBufferSize,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsMeanGetBufferSize_32fc_Ctx)

-
Device scratch buffer size (in bytes) for nppsMean_32fc.

- Parameters
-
**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**hpBufferSize**– Required buffer size. Important: hpBufferSize is a*host pointer.*[Scratch Buffer and Host Pointer](https://docs.nvidia.com/introduction.html#general_conventions_lb_1general_scratch_buffer).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
NPP_SUCCESS



-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsMeanGetBufferSize_64f_Ctx(size_t nLength, size_t *hpBufferSize,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsMeanGetBufferSize_64f_Ctx)

-
Device scratch buffer size (in bytes) for nppsMean_64f.

- Parameters
-
**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**hpBufferSize**– Required buffer size. Important: hpBufferSize is a*host pointer.*[Scratch Buffer and Host Pointer](https://docs.nvidia.com/introduction.html#general_conventions_lb_1general_scratch_buffer).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
NPP_SUCCESS



-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsMeanGetBufferSize_64fc_Ctx(size_t nLength, size_t *hpBufferSize,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsMeanGetBufferSize_64fc_Ctx)

-
Device scratch buffer size (in bytes) for nppsMean_64fc.

- Parameters
-
**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**hpBufferSize**– Required buffer size. Important: hpBufferSize is a*host pointer.*[Scratch Buffer and Host Pointer](https://docs.nvidia.com/introduction.html#general_conventions_lb_1general_scratch_buffer).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
NPP_SUCCESS



-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsMeanGetBufferSize_16s_Sfs_Ctx(size_t nLength, size_t *hpBufferSize,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsMeanGetBufferSize_16s_Sfs_Ctx)

-
Device scratch buffer size (in bytes) for nppsMean_16s_Sfs_Ctx.

- Parameters
-
**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**hpBufferSize**– Required buffer size. Important: hpBufferSize is a*host pointer.*[Scratch Buffer and Host Pointer](https://docs.nvidia.com/introduction.html#general_conventions_lb_1general_scratch_buffer).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
NPP_SUCCESS



-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsMeanGetBufferSize_32s_Sfs_Ctx(size_t nLength, size_t *hpBufferSize,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsMeanGetBufferSize_32s_Sfs_Ctx)

-
Device scratch buffer size (in bytes) for nppsMean_32s_Sfs_Ctx.

- Parameters
-
**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**hpBufferSize**– Required buffer size. Important: hpBufferSize is a*host pointer.*[Scratch Buffer and Host Pointer](https://docs.nvidia.com/introduction.html#general_conventions_lb_1general_scratch_buffer).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
NPP_SUCCESS



-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsMeanGetBufferSize_16sc_Sfs_Ctx(size_t nLength, size_t *hpBufferSize,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsMeanGetBufferSize_16sc_Sfs_Ctx)

-
Device scratch buffer size (in bytes) for nppsMean_16sc_Sfs_Ctx.

- Parameters
-
**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**hpBufferSize**– Required buffer size. Important: hpBufferSize is a*host pointer.*[Scratch Buffer and Host Pointer](https://docs.nvidia.com/introduction.html#general_conventions_lb_1general_scratch_buffer).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
NPP_SUCCESS



-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsMean_32f_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc, size_t nLength,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pMean,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDeviceBuffer,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsMean_32f_Ctx)

-
32-bit float vector mean method

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**pMean**– Device memory pointer to the output result.**pDeviceBuffer**– Pointer to the required device memory allocation,[Scratch Buffer and Host Pointer](https://docs.nvidia.com/introduction.html#general_conventions_lb_1general_scratch_buffer). Use[nppsMeanGetBufferSize_32f_Ctx](https://docs.nvidia.com#group__signal__mean_1gac4ba80a80b29b8959996fcbe7f10a72f)to determine the minimum number of bytes required.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsMean_32fc_Ctx(const[Npp32fc](https://docs.nvidia.com/nppdefs.html#c.Npp32fc)*pSrc, size_t nLength,[Npp32fc](https://docs.nvidia.com/nppdefs.html#c.Npp32fc)*pMean,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDeviceBuffer,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsMean_32fc_Ctx)

-
32-bit float complex vector mean method

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**pMean**– Device memory pointer to the output result.**pDeviceBuffer**– Pointer to the required device memory allocation,[Scratch Buffer and Host Pointer](https://docs.nvidia.com/introduction.html#general_conventions_lb_1general_scratch_buffer). Use[nppsMeanGetBufferSize_32fc_Ctx](https://docs.nvidia.com#group__signal__mean_1ga947fcf9503a98fe3099ed991d786ac6d)to determine the minimum number of bytes required.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsMean_64f_Ctx(const[Npp64f](https://docs.nvidia.com/nppdefs.html#c.Npp64f)*pSrc, size_t nLength,[Npp64f](https://docs.nvidia.com/nppdefs.html#c.Npp64f)*pMean,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDeviceBuffer,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsMean_64f_Ctx)

-
64-bit double vector mean method

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**pMean**– Device memory pointer to the output result.**pDeviceBuffer**– Pointer to the required device memory allocation,[Scratch Buffer and Host Pointer](https://docs.nvidia.com/introduction.html#general_conventions_lb_1general_scratch_buffer). Use[nppsMeanGetBufferSize_64f_Ctx](https://docs.nvidia.com#group__signal__mean_1gac281e50bd2e92bbbc269f41a53f35331)to determine the minimum number of bytes required.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsMean_64fc_Ctx(const[Npp64fc](https://docs.nvidia.com/nppdefs.html#c.Npp64fc)*pSrc, size_t nLength,[Npp64fc](https://docs.nvidia.com/nppdefs.html#c.Npp64fc)*pMean,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDeviceBuffer,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsMean_64fc_Ctx)

-
64-bit double complex vector mean method

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**pMean**– Device memory pointer to the output result.**pDeviceBuffer**– Pointer to the required device memory allocation,[Scratch Buffer and Host Pointer](https://docs.nvidia.com/introduction.html#general_conventions_lb_1general_scratch_buffer). Use[nppsMeanGetBufferSize_64fc_Ctx](https://docs.nvidia.com#group__signal__mean_1gad17902d4b182eed083b328b8845b79c5)to determine the minimum number of bytes required.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsMean_16s_Sfs_Ctx(const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrc, size_t nLength,[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pMean, int nScaleFactor,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDeviceBuffer,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsMean_16s_Sfs_Ctx)

-
16-bit short vector mean with integer scaling method

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**pMean**– Device memory pointer to the output result.**pDeviceBuffer**– Pointer to the required device memory allocation,[Scratch Buffer and Host Pointer](https://docs.nvidia.com/introduction.html#general_conventions_lb_1general_scratch_buffer). Use[nppsMeanGetBufferSize_16s_Sfs_Ctx](https://docs.nvidia.com#group__signal__mean_1ga184fb16a503df7cfe75d628d07f06256)to determine the minimum number of bytes required.**nScaleFactor**–[Integer Result Scaling](https://docs.nvidia.com/introduction.html#general_conventions_lb_1integer_result_scaling).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsMean_32s_Sfs_Ctx(const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pSrc, size_t nLength,[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pMean, int nScaleFactor,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDeviceBuffer,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsMean_32s_Sfs_Ctx)

-
32-bit integer vector mean with integer scaling method

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**pMean**– Device memory pointer to the output result.**pDeviceBuffer**– Pointer to the required device memory allocation,[Scratch Buffer and Host Pointer](https://docs.nvidia.com/introduction.html#general_conventions_lb_1general_scratch_buffer). Use[nppsMeanGetBufferSize_32s_Sfs_Ctx](https://docs.nvidia.com#group__signal__mean_1gac309dd1e22f6dfff51407c921c1380f6)to determine the minimum number of bytes required.**nScaleFactor**–[Integer Result Scaling](https://docs.nvidia.com/introduction.html#general_conventions_lb_1integer_result_scaling).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsMean_16sc_Sfs_Ctx(const[Npp16sc](https://docs.nvidia.com/nppdefs.html#c.Npp16sc)*pSrc, size_t nLength,[Npp16sc](https://docs.nvidia.com/nppdefs.html#c.Npp16sc)*pMean, int nScaleFactor,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDeviceBuffer,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsMean_16sc_Sfs_Ctx)

-
16-bit short complex vector mean with integer scaling method

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**pMean**– Device memory pointer to the output result.**pDeviceBuffer**– Pointer to the required device memory allocation,[Scratch Buffer and Host Pointer](https://docs.nvidia.com/introduction.html#general_conventions_lb_1general_scratch_buffer). Use[nppsMeanGetBufferSize_16sc_Sfs_Ctx](https://docs.nvidia.com#group__signal__mean_1ga7124cf3b47328a713eaf70076615e358)to determine the minimum number of bytes required.**nScaleFactor**–[Integer Result Scaling](https://docs.nvidia.com/introduction.html#general_conventions_lb_1integer_result_scaling).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


## Signal StdDev[](https://docs.nvidia.com#signal-stddev)

### Standard Deviation[](https://docs.nvidia.com#group__signal__standard__deviation_1signal_standard_deviation)

Calculates the standard deviation for the samples of a signal.

Functions

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsStdDevGetBufferSize_32f_Ctx(size_t nLength, size_t *hpBufferSize,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsStdDevGetBufferSize_32f_Ctx)

-
Device scratch buffer size (in bytes) for nppsStdDev_32f.

- Parameters
-
**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**hpBufferSize**– Required buffer size. Important: hpBufferSize is a*host pointer.*[Scratch Buffer and Host Pointer](https://docs.nvidia.com/introduction.html#general_conventions_lb_1general_scratch_buffer).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
NPP_SUCCESS



-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsStdDevGetBufferSize_64f_Ctx(size_t nLength, size_t *hpBufferSize,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsStdDevGetBufferSize_64f_Ctx)

-
Device scratch buffer size (in bytes) for nppsStdDev_64f.

- Parameters
-
**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**hpBufferSize**– Required buffer size. Important: hpBufferSize is a*host pointer.*[Scratch Buffer and Host Pointer](https://docs.nvidia.com/introduction.html#general_conventions_lb_1general_scratch_buffer).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
NPP_SUCCESS



-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsStdDevGetBufferSize_16s32s_Sfs_Ctx(size_t nLength, size_t *hpBufferSize,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsStdDevGetBufferSize_16s32s_Sfs_Ctx)

-
Device scratch buffer size (in bytes) for nppsStdDev_16s32s_Sfs_Ctx.

- Parameters
-
**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**hpBufferSize**– Required buffer size. Important: hpBufferSize is a*host pointer.*[Scratch Buffer and Host Pointer](https://docs.nvidia.com/introduction.html#general_conventions_lb_1general_scratch_buffer).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
NPP_SUCCESS



-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsStdDevGetBufferSize_16s_Sfs_Ctx(size_t nLength, size_t *hpBufferSize,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsStdDevGetBufferSize_16s_Sfs_Ctx)

-
Device scratch buffer size (in bytes) for nppsStdDev_16s_Sfs_Ctx.

- Parameters
-
**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**hpBufferSize**– Required buffer size. Important: hpBufferSize is a*host pointer.*[Scratch Buffer and Host Pointer](https://docs.nvidia.com/introduction.html#general_conventions_lb_1general_scratch_buffer).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
NPP_SUCCESS



-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsStdDev_32f_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc, size_t nLength,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pStdDev,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDeviceBuffer,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsStdDev_32f_Ctx)

-
32-bit float vector standard deviation method

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**pStdDev**– Device memory pointer to the output result.**pDeviceBuffer**– Pointer to the required device memory allocation,[Scratch Buffer and Host Pointer](https://docs.nvidia.com/introduction.html#general_conventions_lb_1general_scratch_buffer). Use[nppsStdDevGetBufferSize_32f_Ctx](https://docs.nvidia.com#group__signal__standard__deviation_1gad2a3d69b83ffeeebcdf94d8ee0fd7694)to determine the minimum number of bytes required.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsStdDev_64f_Ctx(const[Npp64f](https://docs.nvidia.com/nppdefs.html#c.Npp64f)*pSrc, size_t nLength,[Npp64f](https://docs.nvidia.com/nppdefs.html#c.Npp64f)*pStdDev,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDeviceBuffer,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsStdDev_64f_Ctx)

-
64-bit float vector standard deviation method

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**pStdDev**– Device memory pointer to the output result.**pDeviceBuffer**– Pointer to the required device memory allocation,[Scratch Buffer and Host Pointer](https://docs.nvidia.com/introduction.html#general_conventions_lb_1general_scratch_buffer). Use[nppsStdDevGetBufferSize_64f_Ctx](https://docs.nvidia.com#group__signal__standard__deviation_1ga8a43774be2e3a0cc483369897d629c45)to determine the minimum number of bytes required.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsStdDev_16s32s_Sfs_Ctx(const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrc, size_t nLength,[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pStdDev, int nScaleFactor,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDeviceBuffer,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsStdDev_16s32s_Sfs_Ctx)

-
16-bit float vector standard deviation method (return value is 32-bit)

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**pStdDev**– Device memory pointer to the output result.**nScaleFactor**–[Integer Result Scaling](https://docs.nvidia.com/introduction.html#general_conventions_lb_1integer_result_scaling).**pDeviceBuffer**– Pointer to the required device memory allocation,[Scratch Buffer and Host Pointer](https://docs.nvidia.com/introduction.html#general_conventions_lb_1general_scratch_buffer). Use[nppsStdDevGetBufferSize_16s32s_Sfs_Ctx](https://docs.nvidia.com#group__signal__standard__deviation_1ga8d3815e10b3a7c615e9a079af906ee87)to determine the minimum number of bytes required.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsStdDev_16s_Sfs_Ctx(const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrc, size_t nLength,[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pStdDev, int nScaleFactor,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDeviceBuffer,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsStdDev_16s_Sfs_Ctx)

-
16-bit float vector standard deviation method (return value is also 16-bit)

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**pStdDev**– Device memory pointer to the output result.**nScaleFactor**–[Integer Result Scaling](https://docs.nvidia.com/introduction.html#general_conventions_lb_1integer_result_scaling).**pDeviceBuffer**– Pointer to the required device memory allocation,[Scratch Buffer and Host Pointer](https://docs.nvidia.com/introduction.html#general_conventions_lb_1general_scratch_buffer). Use[nppsStdDevGetBufferSize_16s_Sfs_Ctx](https://docs.nvidia.com#group__signal__standard__deviation_1ga22a752ef8403e0f4db296fea4cf3d494)to determine the minimum number of bytes required.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


## Signal Mean And StdDev[](https://docs.nvidia.com#signal-mean-and-stddev)

### Mean And Standard Deviation[](https://docs.nvidia.com#group__signal__mean__and__standard__deviation_1signal_mean_and_standard_deviation)

Performs the mean and calculates the standard deviation for the samples of a signal.

Functions

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsMeanStdDevGetBufferSize_32f_Ctx(size_t nLength, size_t *hpBufferSize,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsMeanStdDevGetBufferSize_32f_Ctx)

-
Device scratch buffer size (in bytes) for nppsMeanStdDev_32f.

- Parameters
-
**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**hpBufferSize**– Required buffer size. Important: hpBufferSize is a*host pointer.*[Scratch Buffer and Host Pointer](https://docs.nvidia.com/introduction.html#general_conventions_lb_1general_scratch_buffer).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
NPP_SUCCESS



-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsMeanStdDevGetBufferSize_64f_Ctx(size_t nLength, size_t *hpBufferSize,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsMeanStdDevGetBufferSize_64f_Ctx)

-
Device scratch buffer size (in bytes) for nppsMeanStdDev_64f.

- Parameters
-
**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**hpBufferSize**– Required buffer size. Important: hpBufferSize is a*host pointer.*[Scratch Buffer and Host Pointer](https://docs.nvidia.com/introduction.html#general_conventions_lb_1general_scratch_buffer).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
NPP_SUCCESS



-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsMeanStdDevGetBufferSize_16s32s_Sfs_Ctx(size_t nLength, size_t *hpBufferSize,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsMeanStdDevGetBufferSize_16s32s_Sfs_Ctx)

-
Device scratch buffer size (in bytes) for nppsMeanStdDev_16s32s_Sfs_Ctx.

- Parameters
-
**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**hpBufferSize**– Required buffer size. Important: hpBufferSize is a*host pointer.*[Scratch Buffer and Host Pointer](https://docs.nvidia.com/introduction.html#general_conventions_lb_1general_scratch_buffer).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
NPP_SUCCESS



-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsMeanStdDevGetBufferSize_16s_Sfs_Ctx(size_t nLength, size_t *hpBufferSize,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsMeanStdDevGetBufferSize_16s_Sfs_Ctx)

-
Device scratch buffer size (in bytes) for nppsMeanStdDev_16s_Sfs_Ctx.

- Parameters
-
**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**hpBufferSize**– Required buffer size. Important: hpBufferSize is a*host pointer.*[Scratch Buffer and Host Pointer](https://docs.nvidia.com/introduction.html#general_conventions_lb_1general_scratch_buffer).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
NPP_SUCCESS



-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsMeanStdDev_32f_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc, size_t nLength,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pMean,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pStdDev,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDeviceBuffer,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsMeanStdDev_32f_Ctx)

-
32-bit float vector mean and standard deviation method

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**pMean**– Device memory pointer to the output mean value.**pStdDev**– Device memory pointer to the output standard deviation value.**pDeviceBuffer**– Pointer to the required device memory allocation,[Scratch Buffer and Host Pointer](https://docs.nvidia.com/introduction.html#general_conventions_lb_1general_scratch_buffer). Use[nppsMeanStdDevGetBufferSize_32f_Ctx](https://docs.nvidia.com#group__signal__mean__and__standard__deviation_1gaac012d449b620091154360027f8184bf)to determine the minimum number of bytes required.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsMeanStdDev_64f_Ctx(const[Npp64f](https://docs.nvidia.com/nppdefs.html#c.Npp64f)*pSrc, size_t nLength,[Npp64f](https://docs.nvidia.com/nppdefs.html#c.Npp64f)*pMean,[Npp64f](https://docs.nvidia.com/nppdefs.html#c.Npp64f)*pStdDev,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDeviceBuffer,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsMeanStdDev_64f_Ctx)

-
64-bit float vector mean and standard deviation method

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**pMean**– Device memory pointer to the output mean value.**pStdDev**– Device memory pointer to the output standard deviation value.**pDeviceBuffer**– Pointer to the required device memory allocation,[Scratch Buffer and Host Pointer](https://docs.nvidia.com/introduction.html#general_conventions_lb_1general_scratch_buffer). Use[nppsMeanStdDevGetBufferSize_64f_Ctx](https://docs.nvidia.com#group__signal__mean__and__standard__deviation_1gaced12fb9965e5cd8d5cfd5a70437b624)to determine the minimum number of bytes required.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsMeanStdDev_16s32s_Sfs_Ctx(const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrc, size_t nLength,[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pMean,[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pStdDev, int nScaleFactor,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDeviceBuffer,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsMeanStdDev_16s32s_Sfs_Ctx)

-
16-bit float vector mean and standard deviation method (return values are 32-bit)

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**pMean**– Device memory pointer to the output mean value.**pStdDev**– Device memory pointer to the output standard deviation value.**nScaleFactor**–[Integer Result Scaling](https://docs.nvidia.com/introduction.html#general_conventions_lb_1integer_result_scaling).**pDeviceBuffer**– Pointer to the required device memory allocation,[Scratch Buffer and Host Pointer](https://docs.nvidia.com/introduction.html#general_conventions_lb_1general_scratch_buffer). Use[nppsMeanStdDevGetBufferSize_16s32s_Sfs_Ctx](https://docs.nvidia.com#group__signal__mean__and__standard__deviation_1ga92e66bfe80ef3815688e94a11f8f667c)to determine the minimum number of bytes required.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsMeanStdDev_16s_Sfs_Ctx(const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrc, size_t nLength,[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pMean,[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pStdDev, int nScaleFactor,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDeviceBuffer,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsMeanStdDev_16s_Sfs_Ctx)

-
16-bit float vector mean and standard deviation method (return values are also 16-bit)

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**pMean**– Device memory pointer to the output mean value.**pStdDev**– Device memory pointer to the output standard deviation value.**nScaleFactor**–[Integer Result Scaling](https://docs.nvidia.com/introduction.html#general_conventions_lb_1integer_result_scaling).**pDeviceBuffer**– Pointer to the required device memory allocation,[Scratch Buffer and Host Pointer](https://docs.nvidia.com/introduction.html#general_conventions_lb_1general_scratch_buffer). Use[nppsMeanStdDevGetBufferSize_16s_Sfs_Ctx](https://docs.nvidia.com#group__signal__mean__and__standard__deviation_1ga060755776eb1eacd3a1b2a8b0447df6e)to determine the minimum number of bytes required.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


## Signal MinMax[](https://docs.nvidia.com#signal-minmax)

### Minimum Maximum[](https://docs.nvidia.com#group__signal__min__max_1signal_min_max)

Performs the maximum and the minimum operation on the samples of a signal.

Functions

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsMinMaxGetBufferSize_8u_Ctx(size_t nLength, size_t *hpBufferSize,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsMinMaxGetBufferSize_8u_Ctx)

-
Device-buffer size (in bytes) for nppsMinMax_8u.

- Parameters
-
**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**hpBufferSize**– Required buffer size. Important: hpBufferSize is a*host pointer.***nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
NPP_SUCCESS



-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsMinMaxGetBufferSize_16s_Ctx(size_t nLength, size_t *hpBufferSize,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsMinMaxGetBufferSize_16s_Ctx)

-
Device-buffer size (in bytes) for nppsMinMax_16s.

- Parameters
-
**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**hpBufferSize**– Required buffer size. Important: hpBufferSize is a*host pointer.***nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
NPP_SUCCESS



-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsMinMaxGetBufferSize_16u_Ctx(size_t nLength, size_t *hpBufferSize,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsMinMaxGetBufferSize_16u_Ctx)

-
Device-buffer size (in bytes) for nppsMinMax_16u.

- Parameters
-
**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**hpBufferSize**– Required buffer size. Important: hpBufferSize is a*host pointer.***nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
NPP_SUCCESS



-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsMinMaxGetBufferSize_32s_Ctx(size_t nLength, size_t *hpBufferSize,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsMinMaxGetBufferSize_32s_Ctx)

-
Device-buffer size (in bytes) for nppsMinMax_32s.

- Parameters
-
**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**hpBufferSize**– Required buffer size. Important: hpBufferSize is a*host pointer.***nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
NPP_SUCCESS



-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsMinMaxGetBufferSize_32u_Ctx(size_t nLength, size_t *hpBufferSize,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsMinMaxGetBufferSize_32u_Ctx)

-
Device-buffer size (in bytes) for nppsMinMax_32u.

- Parameters
-
**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**hpBufferSize**– Required buffer size. Important: hpBufferSize is a*host pointer.***nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
NPP_SUCCESS



-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsMinMaxGetBufferSize_32f_Ctx(size_t nLength, size_t *hpBufferSize,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsMinMaxGetBufferSize_32f_Ctx)

-
Device-buffer size (in bytes) for nppsMinMax_32f.

- Parameters
-
**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**hpBufferSize**– Required buffer size. Important: hpBufferSize is a*host pointer.***nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
NPP_SUCCESS



-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsMinMaxGetBufferSize_64f_Ctx(size_t nLength, size_t *hpBufferSize,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsMinMaxGetBufferSize_64f_Ctx)

-
Device-buffer size (in bytes) for nppsMinMax_64f.

- Parameters
-
**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**hpBufferSize**– Required buffer size. Important: hpBufferSize is a*host pointer.***nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
NPP_SUCCESS



-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsMinMax_8u_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, size_t nLength,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pMin,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pMax,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDeviceBuffer,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsMinMax_8u_Ctx)

-
8-bit char vector min and max method

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**pMin**– Device memory pointer to the min output result.**pMax**– Device memory pointer to the max output result.**pDeviceBuffer**– Pointer to the required device memory allocation,[Scratch Buffer and Host Pointer](https://docs.nvidia.com/introduction.html#general_conventions_lb_1general_scratch_buffer). Use[nppsMinMaxGetBufferSize_8u_Ctx](https://docs.nvidia.com#group__signal__min__max_1ga54eb3ff3f18f36d3b83728aeabdc96ff)to determine the minimum number of bytes required.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsMinMax_16s_Ctx(const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrc, size_t nLength,[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pMin,[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pMax,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDeviceBuffer,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsMinMax_16s_Ctx)

-
16-bit signed short vector min and max method

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**pMin**– Device memory pointer to the min output result.**pMax**– Device memory pointer to the max output result.**pDeviceBuffer**– Pointer to the required device memory allocation,[Scratch Buffer and Host Pointer](https://docs.nvidia.com/introduction.html#general_conventions_lb_1general_scratch_buffer). Use[nppsMinMaxGetBufferSize_16s_Ctx](https://docs.nvidia.com#group__signal__min__max_1ga159ee7751f2b6d519f81cf1420c2d4e6)to determine the minimum number of bytes required.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsMinMax_16u_Ctx(const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrc, size_t nLength,[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pMin,[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pMax,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDeviceBuffer,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsMinMax_16u_Ctx)

-
16-bit unsigned short vector min and max method

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**pMin**– Device memory pointer to the min output result.**pMax**– Device memory pointer to the max output result.**pDeviceBuffer**– Pointer to the required device memory allocation,[Scratch Buffer and Host Pointer](https://docs.nvidia.com/introduction.html#general_conventions_lb_1general_scratch_buffer). Use[nppsMinMaxGetBufferSize_16u_Ctx](https://docs.nvidia.com#group__signal__min__max_1ga705597efc52169c1264e914dd51f27c6)to determine the minimum number of bytes required.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsMinMax_32u_Ctx(const[Npp32u](https://docs.nvidia.com/nppdefs.html#c.Npp32u)*pSrc, size_t nLength,[Npp32u](https://docs.nvidia.com/nppdefs.html#c.Npp32u)*pMin,[Npp32u](https://docs.nvidia.com/nppdefs.html#c.Npp32u)*pMax,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDeviceBuffer,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsMinMax_32u_Ctx)

-
32-bit unsigned int vector min and max method

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**pMin**– Device memory pointer to the min output result.**pMax**– Device memory pointer to the max output result.**pDeviceBuffer**– Pointer to the required device memory allocation,[Scratch Buffer and Host Pointer](https://docs.nvidia.com/introduction.html#general_conventions_lb_1general_scratch_buffer). Use[nppsMinMaxGetBufferSize_32u_Ctx](https://docs.nvidia.com#group__signal__min__max_1ga32e0a8fcd3c9d86bb707931d13badaee)to determine the minimum number of bytes required.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsMinMax_32s_Ctx(const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pSrc, size_t nLength,[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pMin,[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pMax,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDeviceBuffer,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsMinMax_32s_Ctx)

-
32-bit signed int vector min and max method

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**pMin**– Device memory pointer to the min output result.**pMax**– Device memory pointer to the max output result.**pDeviceBuffer**– Pointer to the required device memory allocation,[Scratch Buffer and Host Pointer](https://docs.nvidia.com/introduction.html#general_conventions_lb_1general_scratch_buffer). Use[nppsMinMaxGetBufferSize_32s_Ctx](https://docs.nvidia.com#group__signal__min__max_1ga4f53de294f71cf4a633ba160d019c355)to determine the minimum number of bytes required.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsMinMax_32f_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc, size_t nLength,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pMin,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pMax,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDeviceBuffer,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsMinMax_32f_Ctx)

-
32-bit float vector min and max method

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**pMin**– Device memory pointer to the min output result.**pMax**– Device memory pointer to the max output result.**pDeviceBuffer**– Pointer to the required device memory allocation,[Scratch Buffer and Host Pointer](https://docs.nvidia.com/introduction.html#general_conventions_lb_1general_scratch_buffer). Use[nppsMinMaxGetBufferSize_32f_Ctx](https://docs.nvidia.com#group__signal__min__max_1ga80335e9ce703a25d9a33d32a269f4c09)to determine the minimum number of bytes required.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsMinMax_64f_Ctx(const[Npp64f](https://docs.nvidia.com/nppdefs.html#c.Npp64f)*pSrc, size_t nLength,[Npp64f](https://docs.nvidia.com/nppdefs.html#c.Npp64f)*pMin,[Npp64f](https://docs.nvidia.com/nppdefs.html#c.Npp64f)*pMax,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDeviceBuffer,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsMinMax_64f_Ctx)

-
64-bit double vector min and max method

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**pMin**– Device memory pointer to the min output result.**pMax**– Device memory pointer to the max output result.**pDeviceBuffer**– Pointer to the required device memory allocation,[Scratch Buffer and Host Pointer](https://docs.nvidia.com/introduction.html#general_conventions_lb_1general_scratch_buffer). Use[nppsMinMaxGetBufferSize_64f_Ctx](https://docs.nvidia.com#group__signal__min__max_1ga77200743763c75fdde1bfdc3c25a0eb2)to determine the minimum number of bytes required.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsMinMaxIndxGetBufferSize_8u_Ctx(size_t nLength, size_t *hpBufferSize,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsMinMaxIndxGetBufferSize_8u_Ctx)

-
Device-buffer size (in bytes) for nppsMinMaxIndx_8u.

- Parameters
-
**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**hpBufferSize**– Required buffer size. Important: hpBufferSize is a*host pointer.***nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
NPP_SUCCESS



-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsMinMaxIndxGetBufferSize_16s_Ctx(size_t nLength, size_t *hpBufferSize,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsMinMaxIndxGetBufferSize_16s_Ctx)

-
Device-buffer size (in bytes) for nppsMinMaxIndx_16s.

- Parameters
-
**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**hpBufferSize**– Required buffer size. Important: hpBufferSize is a*host pointer.***nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
NPP_SUCCESS



-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsMinMaxIndxGetBufferSize_16u_Ctx(size_t nLength, size_t *hpBufferSize,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsMinMaxIndxGetBufferSize_16u_Ctx)

-
Device-buffer size (in bytes) for nppsMinMaxIndx_16u.

- Parameters
-
**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**hpBufferSize**– Required buffer size. Important: hpBufferSize is a*host pointer.***nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
NPP_SUCCESS



-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsMinMaxIndxGetBufferSize_32s_Ctx(size_t nLength, size_t *hpBufferSize,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsMinMaxIndxGetBufferSize_32s_Ctx)

-
Device-buffer size (in bytes) for nppsMinMaxIndx_32s.

- Parameters
-
**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**hpBufferSize**– Required buffer size. Important: hpBufferSize is a*host pointer.***nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
NPP_SUCCESS



-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsMinMaxIndxGetBufferSize_32u_Ctx(size_t nLength, size_t *hpBufferSize,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsMinMaxIndxGetBufferSize_32u_Ctx)

-
Device-buffer size (in bytes) for nppsMinMaxIndx_32u.

- Parameters
-
**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**hpBufferSize**– Required buffer size. Important: hpBufferSize is a*host pointer.***nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
NPP_SUCCESS



-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsMinMaxIndxGetBufferSize_32f_Ctx(size_t nLength, size_t *hpBufferSize,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsMinMaxIndxGetBufferSize_32f_Ctx)

-
Device-buffer size (in bytes) for nppsMinMaxIndx_32f.

- Parameters
-
**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**hpBufferSize**– Required buffer size. Important: hpBufferSize is a*host pointer.***nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
NPP_SUCCESS



-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsMinMaxIndxGetBufferSize_64f_Ctx(size_t nLength, size_t *hpBufferSize,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsMinMaxIndxGetBufferSize_64f_Ctx)

-
Device-buffer size (in bytes) for nppsMinMaxIndx_64f.

- Parameters
-
**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**hpBufferSize**– Required buffer size. Important: hpBufferSize is a*host pointer.***nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
NPP_SUCCESS



-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsMinMaxIndx_8u_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, size_t nLength,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pMin, int *pMinIndx,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pMax, int *pMaxIndx,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDeviceBuffer,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsMinMaxIndx_8u_Ctx)

-
8-bit char vector min and max with indices method

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**pMin**– Device memory pointer to the min output result.**pMinIndx**– Device memory pointer to the index of the first min value.**pMax**– Device memory pointer to the max output result.**pMaxIndx**– Device memory pointer to the index of the first max value.**pDeviceBuffer**– Pointer to the required device memory allocation,[Scratch Buffer and Host Pointer](https://docs.nvidia.com/introduction.html#general_conventions_lb_1general_scratch_buffer). Use[nppsMinMaxIndxGetBufferSize_8u_Ctx](https://docs.nvidia.com#group__signal__min__max_1ga4ce6c3cee73f2560d9c6a7aca3aac9ba)to determine the minimum number of bytes required.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsMinMaxIndx_16s_Ctx(const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrc, size_t nLength,[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pMin, int *pMinIndx,[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pMax, int *pMaxIndx,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDeviceBuffer,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsMinMaxIndx_16s_Ctx)

-
16-bit signed short vector min and max with indices method

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**pMin**– Device memory pointer to the min output result.**pMinIndx**– Device memory pointer to the index of the first min value.**pMax**– Device memory pointer to the max output result.**pMaxIndx**– Device memory pointer to the index of the first max value.**pDeviceBuffer**– Pointer to the required device memory allocation,[Scratch Buffer and Host Pointer](https://docs.nvidia.com/introduction.html#general_conventions_lb_1general_scratch_buffer). Use[nppsMinMaxIndxGetBufferSize_16s_Ctx](https://docs.nvidia.com#group__signal__min__max_1ga05a8c40b41a01a1c4e412876e93d644e)to determine the minimum number of bytes required.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsMinMaxIndx_16u_Ctx(const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrc, size_t nLength,[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pMin, int *pMinIndx,[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pMax, int *pMaxIndx,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDeviceBuffer,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsMinMaxIndx_16u_Ctx)

-
16-bit unsigned short vector min and max with indices method

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**pMin**– Device memory pointer to the min output result.**pMinIndx**– Device memory pointer to the index of the first min value.**pMax**– Device memory pointer to the max output result.**pMaxIndx**– Device memory pointer to the index of the first max value.**pDeviceBuffer**– Pointer to the required device memory allocation,[Scratch Buffer and Host Pointer](https://docs.nvidia.com/introduction.html#general_conventions_lb_1general_scratch_buffer). Use[nppsMinMaxIndxGetBufferSize_16u_Ctx](https://docs.nvidia.com#group__signal__min__max_1gaa76f899b0bc16245d32551caeb6981fd)to determine the minimum number of bytes required.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsMinMaxIndx_32s_Ctx(const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pSrc, size_t nLength,[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pMin, int *pMinIndx,[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pMax, int *pMaxIndx,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDeviceBuffer,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsMinMaxIndx_32s_Ctx)

-
32-bit signed short vector min and max with indices method

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**pMin**– Device memory pointer to the min output result.**pMinIndx**– Device memory pointer to the index of the first min value.**pMax**– Device memory pointer to the max output result.**pMaxIndx**– Device memory pointer to the index of the first max value.**pDeviceBuffer**– Pointer to the required device memory allocation,[Scratch Buffer and Host Pointer](https://docs.nvidia.com/introduction.html#general_conventions_lb_1general_scratch_buffer). Use[nppsMinMaxIndxGetBufferSize_32s_Ctx](https://docs.nvidia.com#group__signal__min__max_1ga4941a354f31117b427afa98c10dff33d)to determine the minimum number of bytes required.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsMinMaxIndx_32u_Ctx(const[Npp32u](https://docs.nvidia.com/nppdefs.html#c.Npp32u)*pSrc, size_t nLength,[Npp32u](https://docs.nvidia.com/nppdefs.html#c.Npp32u)*pMin, int *pMinIndx,[Npp32u](https://docs.nvidia.com/nppdefs.html#c.Npp32u)*pMax, int *pMaxIndx,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDeviceBuffer,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsMinMaxIndx_32u_Ctx)

-
32-bit unsigned short vector min and max with indices method

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**pMin**– Device memory pointer to the min output result.**pMinIndx**– Device memory pointer to the index of the first min value.**pMax**– Device memory pointer to the max output result.**pMaxIndx**– Device memory pointer to the index of the first max value.**pDeviceBuffer**– Pointer to the required device memory allocation,[Scratch Buffer and Host Pointer](https://docs.nvidia.com/introduction.html#general_conventions_lb_1general_scratch_buffer). Use[nppsMinMaxIndxGetBufferSize_32u_Ctx](https://docs.nvidia.com#group__signal__min__max_1ga69cfcc13209504540be8d2e362bbd1a4)to determine the minimum number of bytes required.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsMinMaxIndx_32f_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc, size_t nLength,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pMin, int *pMinIndx,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pMax, int *pMaxIndx,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDeviceBuffer,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsMinMaxIndx_32f_Ctx)

-
32-bit float vector min and max with indices method

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**pMin**– Device memory pointer to the min output result.**pMinIndx**– Device memory pointer to the index of the first min value.**pMax**– Device memory pointer to the max output result.**pMaxIndx**– Device memory pointer to the index of the first max value.**pDeviceBuffer**– Pointer to the required device memory allocation,[Scratch Buffer and Host Pointer](https://docs.nvidia.com/introduction.html#general_conventions_lb_1general_scratch_buffer). Use[nppsMinMaxIndxGetBufferSize_32f_Ctx](https://docs.nvidia.com#group__signal__min__max_1ga1d706527ca49a84cdaf075d3421358c3)to determine the minimum number of bytes required.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsMinMaxIndx_64f_Ctx(const[Npp64f](https://docs.nvidia.com/nppdefs.html#c.Npp64f)*pSrc, size_t nLength,[Npp64f](https://docs.nvidia.com/nppdefs.html#c.Npp64f)*pMin, int *pMinIndx,[Npp64f](https://docs.nvidia.com/nppdefs.html#c.Npp64f)*pMax, int *pMaxIndx,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDeviceBuffer,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsMinMaxIndx_64f_Ctx)

-
64-bit float vector min and max with indices method

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**pMin**– Device memory pointer to the min output result.**pMinIndx**– Device memory pointer to the index of the first min value.**pMax**– Device memory pointer to the max output result.**pMaxIndx**– Device memory pointer to the index of the first max value.**pDeviceBuffer**– Pointer to the required device memory allocation,[Scratch Buffer and Host Pointer](https://docs.nvidia.com/introduction.html#general_conventions_lb_1general_scratch_buffer). Use[nppsMinMaxIndxGetBufferSize_64f_Ctx](https://docs.nvidia.com#group__signal__min__max_1ga11a2b3ae47d3536a0021306831abef86)to determine the minimum number of bytes required.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


## Signal Norms[](https://docs.nvidia.com#signal-norms)

### Signal Norm Inf[](https://docs.nvidia.com#signal-norm-inf)

#### Infinity Norm[](https://docs.nvidia.com#group__signal__infinity__norm_1signal_infinity_norm)

Performs the infinity norm on the samples of a signal.

Functions

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsNormInfGetBufferSize_32f_Ctx(size_t nLength, size_t *hpBufferSize,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsNormInfGetBufferSize_32f_Ctx)

-
Device-buffer size (in bytes) for nppsNorm_Inf_32f.

- Parameters
-
**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**hpBufferSize**– Required buffer size. Important: hpBufferSize is a*host pointer.***nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
NPP_SUCCESS



-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsNorm_Inf_32f_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc, size_t nLength,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pNorm,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDeviceBuffer,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsNorm_Inf_32f_Ctx)

-
32-bit float vector C norm method

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**pNorm**– Device memory pointer to the norm result.**pDeviceBuffer**– Pointer to the required device memory allocation,[Scratch Buffer and Host Pointer](https://docs.nvidia.com/introduction.html#general_conventions_lb_1general_scratch_buffer). Use[nppsNormInfGetBufferSize_32f_Ctx](https://docs.nvidia.com#group__signal__infinity__norm_1ga946d37010e440311ff64ebb5d76be819)to determine the minimum number of bytes required.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsNormInfGetBufferSize_64f_Ctx(size_t nLength, size_t *hpBufferSize,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsNormInfGetBufferSize_64f_Ctx)

-
Device-buffer size (in bytes) for nppsNorm_Inf_64f_Ctx.

- Parameters
-
**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**hpBufferSize**– Required buffer size. Important: hpBufferSize is a*host pointer.***nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
NPP_SUCCESS



-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsNorm_Inf_64f_Ctx(const[Npp64f](https://docs.nvidia.com/nppdefs.html#c.Npp64f)*pSrc, size_t nLength,[Npp64f](https://docs.nvidia.com/nppdefs.html#c.Npp64f)*pNorm,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDeviceBuffer,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsNorm_Inf_64f_Ctx)

-
64-bit float vector C norm method

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**pNorm**– Device memory pointer to the norm result.**pDeviceBuffer**– Pointer to the required device memory allocation,[Scratch Buffer and Host Pointer](https://docs.nvidia.com/introduction.html#general_conventions_lb_1general_scratch_buffer). Use[nppsNormInfGetBufferSize_64f_Ctx](https://docs.nvidia.com#group__signal__infinity__norm_1gaddd93257a42937141d220c90e59b188f)to determine the minimum number of bytes required.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsNormInfGetBufferSize_16s32f_Ctx(size_t nLength, size_t *hpBufferSize,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsNormInfGetBufferSize_16s32f_Ctx)

-
Device-buffer size (in bytes) for nppsNorm_Inf_16s32f_Ctx.

- Parameters
-
**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**hpBufferSize**– Required buffer size. Important: hpBufferSize is a*host pointer.***nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
NPP_SUCCESS



-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsNorm_Inf_16s32f_Ctx(const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrc, size_t nLength,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pNorm,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDeviceBuffer,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsNorm_Inf_16s32f_Ctx)

-
16-bit signed short integer vector C norm method, return value is 32-bit float.

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**pNorm**– Device memory pointer to the norm result.**pDeviceBuffer**– Pointer to the required device memory allocation,[Scratch Buffer and Host Pointer](https://docs.nvidia.com/introduction.html#general_conventions_lb_1general_scratch_buffer). Use[nppsNormInfGetBufferSize_16s32f_Ctx](https://docs.nvidia.com#group__signal__infinity__norm_1ga8a8c95088c7a2194cc5b81c3920e6424)to determine the minimum number of bytes required.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsNormInfGetBufferSize_32fc32f_Ctx(size_t nLength, size_t *hpBufferSize,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsNormInfGetBufferSize_32fc32f_Ctx)

-
Device-buffer size (in bytes) for nppsNorm_Inf_32fc32f_Ctx.

- Parameters
-
**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**hpBufferSize**– Required buffer size. Important: hpBufferSize is a*host pointer.***nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
NPP_SUCCESS



-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsNorm_Inf_32fc32f_Ctx(const[Npp32fc](https://docs.nvidia.com/nppdefs.html#c.Npp32fc)*pSrc, size_t nLength,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pNorm,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDeviceBuffer,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsNorm_Inf_32fc32f_Ctx)

-
32-bit float complex vector C norm method, return value is 32-bit float.

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**pNorm**– Device memory pointer to the norm result.**pDeviceBuffer**– Pointer to the required device memory allocation,[Scratch Buffer and Host Pointer](https://docs.nvidia.com/introduction.html#general_conventions_lb_1general_scratch_buffer). Use[nppsNormInfGetBufferSize_32fc32f_Ctx](https://docs.nvidia.com#group__signal__infinity__norm_1ga3bf190ed23765c1b4378f9b4662a202b)to determine the minimum number of bytes required.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsNormInfGetBufferSize_64fc64f_Ctx(size_t nLength, size_t *hpBufferSize,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsNormInfGetBufferSize_64fc64f_Ctx)

-
Device-buffer size (in bytes) for nppsNorm_Inf_64fc64f.

- Parameters
-
**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**hpBufferSize**– Required buffer size. Important: hpBufferSize is a*host pointer.***nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
NPP_SUCCESS



-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsNorm_Inf_64fc64f_Ctx(const[Npp64fc](https://docs.nvidia.com/nppdefs.html#c.Npp64fc)*pSrc, size_t nLength,[Npp64f](https://docs.nvidia.com/nppdefs.html#c.Npp64f)*pNorm,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDeviceBuffer,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsNorm_Inf_64fc64f_Ctx)

-
64-bit float complex vector C norm method, return value is 64-bit float.

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**pNorm**– Device memory pointer to the norm result.**pDeviceBuffer**– Pointer to the required device memory allocation,[Scratch Buffer and Host Pointer](https://docs.nvidia.com/introduction.html#general_conventions_lb_1general_scratch_buffer). Use[nppsNormInfGetBufferSize_64fc64f_Ctx](https://docs.nvidia.com#group__signal__infinity__norm_1gaeb1a34716dfb6a1c93bb933d3b19311b)to determine the minimum number of bytes required.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsNormInfGetBufferSize_16s32s_Sfs_Ctx(size_t nLength, size_t *hpBufferSize,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsNormInfGetBufferSize_16s32s_Sfs_Ctx)

-
Device-buffer size (in bytes) for nppsNorm_Inf_16s32s_Sfs_Ctx.

- Parameters
-
**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**hpBufferSize**– Required buffer size. Important: hpBufferSize is a*host pointer.***nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
NPP_SUCCESS



-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsNorm_Inf_16s32s_Sfs_Ctx(const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrc, size_t nLength,[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pNorm, int nScaleFactor,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDeviceBuffer,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsNorm_Inf_16s32s_Sfs_Ctx)

-
16-bit signed short integer vector C norm method, return value is 32-bit signed integer.

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**pNorm**– Device memory pointer to the norm result.**nScaleFactor**–[Integer Result Scaling](https://docs.nvidia.com/introduction.html#general_conventions_lb_1integer_result_scaling).**pDeviceBuffer**– Pointer to the required device memory allocation,[Scratch Buffer and Host Pointer](https://docs.nvidia.com/introduction.html#general_conventions_lb_1general_scratch_buffer). Use[nppsNormInfGetBufferSize_16s32s_Sfs_Ctx](https://docs.nvidia.com#group__signal__infinity__norm_1ga111df5b38eae60495bf554a33afa4e6a)to determine the minimum number of bytes required.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


### Signal Norm L1[](https://docs.nvidia.com#signal-norm-l1)

#### L1 Norm[](https://docs.nvidia.com#group__signal__L1__norm_1signal_L1_norm)

Performs the L1 norm on the samples of a signal.

Functions

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsNormL1GetBufferSize_32f_Ctx(size_t nLength, size_t *hpBufferSize,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsNormL1GetBufferSize_32f_Ctx)

-
Device-buffer size (in bytes) for nppsNorm_L1_32f.

- Parameters
-
**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**hpBufferSize**– Required buffer size. Important: hpBufferSize is a*host pointer.***nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
NPP_SUCCESS



-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsNorm_L1_32f_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc, size_t nLength,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pNorm,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDeviceBuffer,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsNorm_L1_32f_Ctx)

-
32-bit float vector L1 norm method

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**pNorm**– Device memory pointer to the norm result.**pDeviceBuffer**– Pointer to the required device memory allocation,[Scratch Buffer and Host Pointer](https://docs.nvidia.com/introduction.html#general_conventions_lb_1general_scratch_buffer). Use[nppsNormL1GetBufferSize_32f_Ctx](https://docs.nvidia.com#group__signal__l1__norm_1gaa899ad58fce9d0aafd3dfb2bf46358db)to determine the minimum number of bytes required.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsNormL1GetBufferSize_64f_Ctx(size_t nLength, size_t *hpBufferSize,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsNormL1GetBufferSize_64f_Ctx)

-
Device-buffer size (in bytes) for nppsNorm_L1_64f_Ctx.

- Parameters
-
**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**hpBufferSize**– Required buffer size. Important: hpBufferSize is a*host pointer.***nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
NPP_SUCCESS



-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsNorm_L1_64f_Ctx(const[Npp64f](https://docs.nvidia.com/nppdefs.html#c.Npp64f)*pSrc, size_t nLength,[Npp64f](https://docs.nvidia.com/nppdefs.html#c.Npp64f)*pNorm,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDeviceBuffer,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsNorm_L1_64f_Ctx)

-
64-bit float vector L1 norm method

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**pNorm**– Device memory pointer to the norm result.**pDeviceBuffer**– Pointer to the required device memory allocation,[Scratch Buffer and Host Pointer](https://docs.nvidia.com/introduction.html#general_conventions_lb_1general_scratch_buffer). Use[nppsNormL1GetBufferSize_64f_Ctx](https://docs.nvidia.com#group__signal__l1__norm_1ga8b06432ec552d9406886e626b4011b67)to determine the minimum number of bytes required.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsNormL1GetBufferSize_16s32f_Ctx(size_t nLength, size_t *hpBufferSize,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsNormL1GetBufferSize_16s32f_Ctx)

-
Device-buffer size (in bytes) for nppsNorm_L1_16s32f_Ctx.

- Parameters
-
**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**hpBufferSize**– Required buffer size. Important: hpBufferSize is a*host pointer.***nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
NPP_SUCCESS



-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsNorm_L1_16s32f_Ctx(const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrc, size_t nLength,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pNorm,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDeviceBuffer,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsNorm_L1_16s32f_Ctx)

-
16-bit signed short integer vector L1 norm method, return value is 32-bit float.

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**pNorm**– Device memory pointer to the L1 norm result.**pDeviceBuffer**– Pointer to the required device memory allocation,[Scratch Buffer and Host Pointer](https://docs.nvidia.com/introduction.html#general_conventions_lb_1general_scratch_buffer). Use[nppsNormL1GetBufferSize_16s32f_Ctx](https://docs.nvidia.com#group__signal__l1__norm_1ga6781fd7e0f4e05feeaa5d3ed2f4e4a78)to determine the minimum number of bytes required.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsNormL1GetBufferSize_32fc64f_Ctx(size_t nLength, size_t *hpBufferSize,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsNormL1GetBufferSize_32fc64f_Ctx)

-
Device-buffer size (in bytes) for nppsNorm_L1_32fc64f_Ctx.

- Parameters
-
**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**hpBufferSize**– Required buffer size. Important: hpBufferSize is a*host pointer.***nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
NPP_SUCCESS



-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsNorm_L1_32fc64f_Ctx(const[Npp32fc](https://docs.nvidia.com/nppdefs.html#c.Npp32fc)*pSrc, size_t nLength,[Npp64f](https://docs.nvidia.com/nppdefs.html#c.Npp64f)*pNorm,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDeviceBuffer,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsNorm_L1_32fc64f_Ctx)

-
32-bit float complex vector L1 norm method, return value is 64-bit float.

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**pNorm**– Device memory pointer to the norm result.**pDeviceBuffer**– Pointer to the required device memory allocation,[Scratch Buffer and Host Pointer](https://docs.nvidia.com/introduction.html#general_conventions_lb_1general_scratch_buffer). Use[nppsNormL1GetBufferSize_32fc64f_Ctx](https://docs.nvidia.com#group__signal__l1__norm_1gaf4ed2d2a7c05f2726365027df52ddce7)to determine the minimum number of bytes required.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsNormL1GetBufferSize_64fc64f_Ctx(size_t nLength, size_t *hpBufferSize,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsNormL1GetBufferSize_64fc64f_Ctx)

-
Device-buffer size (in bytes) for nppsNorm_L1_64fc64f.

- Parameters
-
**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**hpBufferSize**– Required buffer size. Important: hpBufferSize is a*host pointer.***nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
NPP_SUCCESS



-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsNorm_L1_64fc64f_Ctx(const[Npp64fc](https://docs.nvidia.com/nppdefs.html#c.Npp64fc)*pSrc, size_t nLength,[Npp64f](https://docs.nvidia.com/nppdefs.html#c.Npp64f)*pNorm,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDeviceBuffer,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsNorm_L1_64fc64f_Ctx)

-
64-bit float complex vector L1 norm method, return value is 64-bit float.

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**pNorm**– Device memory pointer to the norm result.**pDeviceBuffer**– Pointer to the required device memory allocation,[Scratch Buffer and Host Pointer](https://docs.nvidia.com/introduction.html#general_conventions_lb_1general_scratch_buffer). Use[nppsNormL1GetBufferSize_64fc64f_Ctx](https://docs.nvidia.com#group__signal__l1__norm_1gabd09306be8823934a5573ffc50a766f8)to determine the minimum number of bytes required.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsNormL1GetBufferSize_16s32s_Sfs_Ctx(size_t nLength, size_t *hpBufferSize,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsNormL1GetBufferSize_16s32s_Sfs_Ctx)

-
Device-buffer size (in bytes) for nppsNorm_L1_16s32s_Sfs_Ctx.

- Parameters
-
**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**hpBufferSize**– Required buffer size. Important: hpBufferSize is a*host pointer.***nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
NPP_SUCCESS



-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsNorm_L1_16s32s_Sfs_Ctx(const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrc, size_t nLength,[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pNorm, int nScaleFactor,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDeviceBuffer,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsNorm_L1_16s32s_Sfs_Ctx)

-
16-bit signed short integer vector L1 norm method, return value is 32-bit signed integer.

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**pNorm**– Device memory pointer to the norm result.**nScaleFactor**–[Integer Result Scaling](https://docs.nvidia.com/introduction.html#general_conventions_lb_1integer_result_scaling).**pDeviceBuffer**– Pointer to the required device memory allocation,[Scratch Buffer and Host Pointer](https://docs.nvidia.com/introduction.html#general_conventions_lb_1general_scratch_buffer). Use[nppsNormL1GetBufferSize_16s32s_Sfs_Ctx](https://docs.nvidia.com#group__signal__l1__norm_1ga0de837a287316801e23265e84ea7f609)to determine the minimum number of bytes required.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsNormL1GetBufferSize_16s64s_Sfs_Ctx(size_t nLength, size_t *hpBufferSize,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsNormL1GetBufferSize_16s64s_Sfs_Ctx)

-
Device-buffer size (in bytes) for nppsNorm_L1_16s64s_Sfs_Ctx.

- Parameters
-
**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**hpBufferSize**– Required buffer size. Important: hpBufferSize is a*host pointer.***nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
NPP_SUCCESS



-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsNorm_L1_16s64s_Sfs_Ctx(const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrc, size_t nLength,[Npp64s](https://docs.nvidia.com/nppdefs.html#c.Npp64s)*pNorm, int nScaleFactor,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDeviceBuffer,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsNorm_L1_16s64s_Sfs_Ctx)

-
16-bit signed short integer vector L1 norm method, return value is 64-bit signed integer.

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**pNorm**– Device memory pointer to the norm result.**nScaleFactor**–[Integer Result Scaling](https://docs.nvidia.com/introduction.html#general_conventions_lb_1integer_result_scaling).**pDeviceBuffer**– Pointer to the required device memory allocation,[Scratch Buffer and Host Pointer](https://docs.nvidia.com/introduction.html#general_conventions_lb_1general_scratch_buffer). Use[nppsNormL1GetBufferSize_16s64s_Sfs_Ctx](https://docs.nvidia.com#group__signal__l1__norm_1gac8141f647995286e84fff557aa09b7bc)to determine the minimum number of bytes required.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


### Signal Norm L2[](https://docs.nvidia.com#signal-norm-l2)

#### L2 Norm[](https://docs.nvidia.com#group__signal__L2__norm_1signal_L2_norm)

Performs the L2 norm on the samples of a signal.

Functions

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsNormL2GetBufferSize_32f_Ctx(size_t nLength, size_t *hpBufferSize,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsNormL2GetBufferSize_32f_Ctx)

-
Device-buffer size (in bytes) for nppsNorm_L2_32f_Ctx.

- Parameters
-
**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**hpBufferSize**– Required buffer size. Important: hpBufferSize is a*host pointer.***nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
NPP_SUCCESS



-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsNorm_L2_32f_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc, size_t nLength,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pNorm,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDeviceBuffer,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsNorm_L2_32f_Ctx)

-
32-bit float vector L2 norm method

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**pNorm**– Device memory pointer to the norm result.**pDeviceBuffer**– Pointer to the required device memory allocation,[Scratch Buffer and Host Pointer](https://docs.nvidia.com/introduction.html#general_conventions_lb_1general_scratch_buffer). Use[nppsNormL2GetBufferSize_32f_Ctx](https://docs.nvidia.com#group__signal__l2__norm_1ga92717e690c21670d6005d9c8f575b581)to determine the minimum number of bytes required.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsNormL2GetBufferSize_64f_Ctx(size_t nLength, size_t *hpBufferSize,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsNormL2GetBufferSize_64f_Ctx)

-
Device-buffer size (in bytes) for nppsNorm_L2_64f_Ctx.

- Parameters
-
**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**hpBufferSize**– Required buffer size. Important: hpBufferSize is a*host pointer.***nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
NPP_SUCCESS



-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsNorm_L2_64f_Ctx(const[Npp64f](https://docs.nvidia.com/nppdefs.html#c.Npp64f)*pSrc, size_t nLength,[Npp64f](https://docs.nvidia.com/nppdefs.html#c.Npp64f)*pNorm,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDeviceBuffer,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsNorm_L2_64f_Ctx)

-
64-bit float vector L2 norm method

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**pNorm**– Device memory pointer to the norm result.**pDeviceBuffer**– Pointer to the required device memory allocation,[Scratch Buffer and Host Pointer](https://docs.nvidia.com/introduction.html#general_conventions_lb_1general_scratch_buffer). Use[nppsNormL2GetBufferSize_64f_Ctx](https://docs.nvidia.com#group__signal__l2__norm_1ga6cefe18602345acf30b8df550713b6fc)to determine the minimum number of bytes required.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsNormL2GetBufferSize_16s32f_Ctx(size_t nLength, size_t *hpBufferSize,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsNormL2GetBufferSize_16s32f_Ctx)

-
Device-buffer size (in bytes) for nppsNorm_L2_16s32f_Ctx.

- Parameters
-
**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**hpBufferSize**– Required buffer size. Important: hpBufferSize is a*host pointer.***nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
NPP_SUCCESS



-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsNorm_L2_16s32f_Ctx(const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrc, size_t nLength,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pNorm,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDeviceBuffer,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsNorm_L2_16s32f_Ctx)

-
16-bit signed short integer vector L2 norm method, return value is 32-bit float.

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**pNorm**– Device memory pointer to the norm result.**pDeviceBuffer**– Pointer to the required device memory allocation,[Scratch Buffer and Host Pointer](https://docs.nvidia.com/introduction.html#general_conventions_lb_1general_scratch_buffer). Use[nppsNormL2GetBufferSize_16s32f_Ctx](https://docs.nvidia.com#group__signal__l2__norm_1gac6645688a2a4b2edfd3a288ed8587564)to determine the minimum number of bytes required.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsNormL2GetBufferSize_32fc64f_Ctx(size_t nLength, size_t *hpBufferSize,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsNormL2GetBufferSize_32fc64f_Ctx)

-
Device-buffer size (in bytes) for nppsNorm_L2_32fc64f_Ctx.

- Parameters
-
**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**hpBufferSize**– Required buffer size. Important: hpBufferSize is a*host pointer.***nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
NPP_SUCCESS



-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsNorm_L2_32fc64f_Ctx(const[Npp32fc](https://docs.nvidia.com/nppdefs.html#c.Npp32fc)*pSrc, size_t nLength,[Npp64f](https://docs.nvidia.com/nppdefs.html#c.Npp64f)*pNorm,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDeviceBuffer,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsNorm_L2_32fc64f_Ctx)

-
32-bit float complex vector L2 norm method, return value is 64-bit float.

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**pNorm**– Device memory pointer to the norm result.**pDeviceBuffer**– Pointer to the required device memory allocation,[Scratch Buffer and Host Pointer](https://docs.nvidia.com/introduction.html#general_conventions_lb_1general_scratch_buffer). Use[nppsNormL2GetBufferSize_32fc64f_Ctx](https://docs.nvidia.com#group__signal__l2__norm_1ga343d7d82cec61ec76ee1b6781bc8d744)to determine the minimum number of bytes required.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsNormL2GetBufferSize_64fc64f_Ctx(size_t nLength, size_t *hpBufferSize,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsNormL2GetBufferSize_64fc64f_Ctx)

-
Device-buffer size (in bytes) for nppsNorm_L2_64fc64f_Ctx.

- Parameters
-
**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**hpBufferSize**– Required buffer size. Important: hpBufferSize is a*host pointer.***nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
NPP_SUCCESS



-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsNorm_L2_64fc64f_Ctx(const[Npp64fc](https://docs.nvidia.com/nppdefs.html#c.Npp64fc)*pSrc, size_t nLength,[Npp64f](https://docs.nvidia.com/nppdefs.html#c.Npp64f)*pNorm,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDeviceBuffer,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsNorm_L2_64fc64f_Ctx)

-
64-bit float complex vector L2 norm method, return value is 64-bit float.

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**pNorm**– Device memory pointer to the norm result.**pDeviceBuffer**– Pointer to the required device memory allocation,[Scratch Buffer and Host Pointer](https://docs.nvidia.com/introduction.html#general_conventions_lb_1general_scratch_buffer). Use[nppsNormL2GetBufferSize_64fc64f_Ctx](https://docs.nvidia.com#group__signal__l2__norm_1ga4692b55b32661bd671d947d5b3480bbe)to determine the minimum number of bytes required.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsNormL2GetBufferSize_16s32s_Sfs_Ctx(size_t nLength, size_t *hpBufferSize,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsNormL2GetBufferSize_16s32s_Sfs_Ctx)

-
Device-buffer size (in bytes) for nppsNorm_L2_16s32s_Sfs_Ctx.

- Parameters
-
**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**hpBufferSize**– Required buffer size. Important: hpBufferSize is a*host pointer.***nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
NPP_SUCCESS



-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsNorm_L2_16s32s_Sfs_Ctx(const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrc, size_t nLength,[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pNorm, int nScaleFactor,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDeviceBuffer,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsNorm_L2_16s32s_Sfs_Ctx)

-
16-bit signed short integer vector L2 norm method, return value is 32-bit signed integer.

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**pNorm**– Device memory pointer to the norm result.**nScaleFactor**–[Integer Result Scaling](https://docs.nvidia.com/introduction.html#general_conventions_lb_1integer_result_scaling).**pDeviceBuffer**– Pointer to the required device memory allocation,[Scratch Buffer and Host Pointer](https://docs.nvidia.com/introduction.html#general_conventions_lb_1general_scratch_buffer). Use[nppsNormL2GetBufferSize_16s32s_Sfs_Ctx](https://docs.nvidia.com#group__signal__l2__norm_1ga3747060c1e067d549eba93b72cb50316)to determine the minimum number of bytes required.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsNormL2SqrGetBufferSize_16s64s_Sfs_Ctx(size_t nLength, size_t *hpBufferSize,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsNormL2SqrGetBufferSize_16s64s_Sfs_Ctx)

-
Device-buffer size (in bytes) for nppsNorm_L2Sqr_16s64s_Sfs_Ctx.

- Parameters
-
**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**hpBufferSize**– Required buffer size. Important: hpBufferSize is a*host pointer.***nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
NPP_SUCCESS



-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsNorm_L2Sqr_16s64s_Sfs_Ctx(const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrc, size_t nLength,[Npp64s](https://docs.nvidia.com/nppdefs.html#c.Npp64s)*pNorm, int nScaleFactor,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDeviceBuffer,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsNorm_L2Sqr_16s64s_Sfs_Ctx)

-
16-bit signed short integer vector L2 Square norm method, return value is 64-bit signed integer.

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**pNorm**– Device memory pointer to the norm result.**nScaleFactor**–[Integer Result Scaling](https://docs.nvidia.com/introduction.html#general_conventions_lb_1integer_result_scaling).**pDeviceBuffer**– Pointer to the required device memory allocation,[Scratch Buffer and Host Pointer](https://docs.nvidia.com/introduction.html#general_conventions_lb_1general_scratch_buffer). Use[nppsNormL2SqrGetBufferSize_16s64s_Sfs_Ctx](https://docs.nvidia.com#group__signal__l2__norm_1gab354e5e06bbd08a453abfcf6b7a56c72)to determine the minimum number of bytes required.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


### Signal Norm Inf NormDiff[](https://docs.nvidia.com#signal-norm-inf-normdiff)

#### Infinity Norm Diff[](https://docs.nvidia.com#group__signal__infinity__norm__diff_1signal_infinity_norm_diff)

Performs the infinity norm on the samples of two input signals’ difference.

Functions

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsNormDiffInfGetBufferSize_32f_Ctx(size_t nLength, size_t *hpBufferSize,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsNormDiffInfGetBufferSize_32f_Ctx)

-
Device-buffer size (in bytes) for nppsNormDiff_Inf_32f.

- Parameters
-
**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**hpBufferSize**– Required buffer size. Important: hpBufferSize is a*host pointer.***nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
NPP_SUCCESS



-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsNormDiff_Inf_32f_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc1, const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc2, size_t nLength,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pNorm,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDeviceBuffer,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsNormDiff_Inf_32f_Ctx)

-
32-bit float C norm method on two vectors’ difference

- Parameters
-
**pSrc1**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pSrc2**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**pNorm**– Device memory pointer to the norm result.**pDeviceBuffer**– Pointer to the required device memory allocation,[Scratch Buffer and Host Pointer](https://docs.nvidia.com/introduction.html#general_conventions_lb_1general_scratch_buffer). Use[nppsNormDiffInfGetBufferSize_32f_Ctx](https://docs.nvidia.com#group__signal__infinity__norm__diff_1ga1280978910c3154c87dfe53fc491fae1)to determine the minimum number of bytes required.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsNormDiffInfGetBufferSize_64f_Ctx(size_t nLength, size_t *hpBufferSize,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsNormDiffInfGetBufferSize_64f_Ctx)

-
Device-buffer size (in bytes) for nppsNormDiff_Inf_64f_Ctx.

- Parameters
-
**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**hpBufferSize**– Required buffer size. Important: hpBufferSize is a*host pointer.***nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
NPP_SUCCESS



-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsNormDiff_Inf_64f_Ctx(const[Npp64f](https://docs.nvidia.com/nppdefs.html#c.Npp64f)*pSrc1, const[Npp64f](https://docs.nvidia.com/nppdefs.html#c.Npp64f)*pSrc2, size_t nLength,[Npp64f](https://docs.nvidia.com/nppdefs.html#c.Npp64f)*pNorm,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDeviceBuffer,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsNormDiff_Inf_64f_Ctx)

-
64-bit float C norm method on two vectors’ difference

- Parameters
-
**pSrc1**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pSrc2**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**pNorm**– Device memory pointer to the norm result.**pDeviceBuffer**– Pointer to the required device memory allocation,[Scratch Buffer and Host Pointer](https://docs.nvidia.com/introduction.html#general_conventions_lb_1general_scratch_buffer). Use[nppsNormDiffInfGetBufferSize_64f_Ctx](https://docs.nvidia.com#group__signal__infinity__norm__diff_1ga02d8ad71c75cf4cb698bdbf76f7f1c0f)to determine the minimum number of bytes required.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsNormDiffInfGetBufferSize_16s32f_Ctx(size_t nLength, size_t *hpBufferSize,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsNormDiffInfGetBufferSize_16s32f_Ctx)

-
Device-buffer size (in bytes) for nppsNormDiff_Inf_16s32f_Ctx.

- Parameters
-
**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**hpBufferSize**– Required buffer size. Important: hpBufferSize is a*host pointer.***nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
NPP_SUCCESS



-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsNormDiff_Inf_16s32f_Ctx(const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrc1, const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrc2, size_t nLength,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pNorm,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDeviceBuffer,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsNormDiff_Inf_16s32f_Ctx)

-
16-bit signed short integer C norm method on two vectors’ difference, return value is 32-bit float.

- Parameters
-
**pSrc1**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pSrc2**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**pNorm**– Device memory pointer to the norm result.**pDeviceBuffer**– Pointer to the required device memory allocation,[Scratch Buffer and Host Pointer](https://docs.nvidia.com/introduction.html#general_conventions_lb_1general_scratch_buffer). Use[nppsNormDiffInfGetBufferSize_16s32f_Ctx](https://docs.nvidia.com#group__signal__infinity__norm__diff_1ga70b0af0ccb3f43d26300cd50715dc90f)to determine the minimum number of bytes required.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsNormDiffInfGetBufferSize_32fc32f_Ctx(size_t nLength, size_t *hpBufferSize,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsNormDiffInfGetBufferSize_32fc32f_Ctx)

-
Device-buffer size (in bytes) for nppsNormDiff_Inf_32fc32f_Ctx.

- Parameters
-
**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**hpBufferSize**– Required buffer size. Important: hpBufferSize is a*host pointer.***nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
NPP_SUCCESS



-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsNormDiff_Inf_32fc32f_Ctx(const[Npp32fc](https://docs.nvidia.com/nppdefs.html#c.Npp32fc)*pSrc1, const[Npp32fc](https://docs.nvidia.com/nppdefs.html#c.Npp32fc)*pSrc2, size_t nLength,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pNorm,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDeviceBuffer,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsNormDiff_Inf_32fc32f_Ctx)

-
32-bit float complex C norm method on two vectors’ difference, return value is 32-bit float.

- Parameters
-
**pSrc1**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pSrc2**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**pNorm**– Device memory pointer to the norm result.**pDeviceBuffer**– Pointer to the required device memory allocation,[Scratch Buffer and Host Pointer](https://docs.nvidia.com/introduction.html#general_conventions_lb_1general_scratch_buffer). Use[nppsNormDiffInfGetBufferSize_32fc32f_Ctx](https://docs.nvidia.com#group__signal__infinity__norm__diff_1ga01d22eac38f8e95dadf1f05dac469a3b)to determine the minimum number of bytes required.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsNormDiffInfGetBufferSize_64fc64f_Ctx(size_t nLength, size_t *hpBufferSize,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsNormDiffInfGetBufferSize_64fc64f_Ctx)

-
Device-buffer size (in bytes) for nppsNormDiff_Inf_64fc64f_Ctx.

- Parameters
-
**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**hpBufferSize**– Required buffer size. Important: hpBufferSize is a*host pointer.***nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
NPP_SUCCESS



-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsNormDiff_Inf_64fc64f_Ctx(const[Npp64fc](https://docs.nvidia.com/nppdefs.html#c.Npp64fc)*pSrc1, const[Npp64fc](https://docs.nvidia.com/nppdefs.html#c.Npp64fc)*pSrc2, size_t nLength,[Npp64f](https://docs.nvidia.com/nppdefs.html#c.Npp64f)*pNorm,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDeviceBuffer,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsNormDiff_Inf_64fc64f_Ctx)

-
64-bit float complex C norm method on two vectors’ difference, return value is 64-bit float.

- Parameters
-
**pSrc1**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pSrc2**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**pNorm**– Device memory pointer to the norm result.**pDeviceBuffer**– Pointer to the required device memory allocation,[Scratch Buffer and Host Pointer](https://docs.nvidia.com/introduction.html#general_conventions_lb_1general_scratch_buffer). Use[nppsNormDiffInfGetBufferSize_64fc64f_Ctx](https://docs.nvidia.com#group__signal__infinity__norm__diff_1ga7c92eeb3f834f55d5b7813c6d4838b87)to determine the minimum number of bytes required.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsNormDiffInfGetBufferSize_16s32s_Sfs_Ctx(size_t nLength, size_t *hpBufferSize,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsNormDiffInfGetBufferSize_16s32s_Sfs_Ctx)

-
Device-buffer size (in bytes) for nppsNormDiff_Inf_16s32s_Sfs_Ctx.

- Parameters
-
**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**hpBufferSize**– Required buffer size. Important: hpBufferSize is a*host pointer.***nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
NPP_SUCCESS



-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsNormDiff_Inf_16s32s_Sfs_Ctx(const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrc1, const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrc2, size_t nLength,[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pNorm, int nScaleFactor,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDeviceBuffer,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsNormDiff_Inf_16s32s_Sfs_Ctx)

-
16-bit signed short integer C norm method on two vectors’ difference, return value is 32-bit signed integer.

- Parameters
-
**pSrc1**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pSrc2**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**pNorm**– Device memory pointer to the norm result.**nScaleFactor**–[Integer Result Scaling](https://docs.nvidia.com/introduction.html#general_conventions_lb_1integer_result_scaling).**pDeviceBuffer**– Pointer to the required device memory allocation,[Scratch Buffer and Host Pointer](https://docs.nvidia.com/introduction.html#general_conventions_lb_1general_scratch_buffer). Use[nppsNormDiffInfGetBufferSize_16s32s_Sfs_Ctx](https://docs.nvidia.com#group__signal__infinity__norm__diff_1ga8969d15afda1b78db089b8bf476224a1)to determine the minimum number of bytes required.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


### Signal Norm L1 NormDiff[](https://docs.nvidia.com#signal-norm-l1-normdiff)

#### L1 Norm Diff[](https://docs.nvidia.com#group__signal__L1__norm__diff_1signal_L1_norm_diff)

Performs the L1 norm on the samples of two input signals’ difference.

Functions

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsNormDiffL1GetBufferSize_32f_Ctx(size_t nLength, size_t *hpBufferSize,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsNormDiffL1GetBufferSize_32f_Ctx)

-
Device-buffer size (in bytes) for nppsNormDiff_L1_32f.

- Parameters
-
**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**hpBufferSize**– Required buffer size. Important: hpBufferSize is a*host pointer.***nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
NPP_SUCCESS



-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsNormDiff_L1_32f_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc1, const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc2, size_t nLength,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pNorm,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDeviceBuffer,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsNormDiff_L1_32f_Ctx)

-
32-bit float L1 norm method on two vectors’ difference

- Parameters
-
**pSrc1**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pSrc2**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**pNorm**– Device memory pointer to the norm result.**pDeviceBuffer**– Pointer to the required device memory allocation,[Scratch Buffer and Host Pointer](https://docs.nvidia.com/introduction.html#general_conventions_lb_1general_scratch_buffer). Use[nppsNormDiffL1GetBufferSize_32f_Ctx](https://docs.nvidia.com#group__signal__l1__norm__diff_1ga2de651f5976e8b30f1631a755fa23628)to determine the minimum number of bytes required.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsNormDiffL1GetBufferSize_64f_Ctx(size_t nLength, size_t *hpBufferSize,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsNormDiffL1GetBufferSize_64f_Ctx)

-
Device-buffer size (in bytes) for nppsNormDiff_L1_64f_Ctx.

- Parameters
-
**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**hpBufferSize**– Required buffer size. Important: hpBufferSize is a*host pointer.***nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
NPP_SUCCESS



-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsNormDiff_L1_64f_Ctx(const[Npp64f](https://docs.nvidia.com/nppdefs.html#c.Npp64f)*pSrc1, const[Npp64f](https://docs.nvidia.com/nppdefs.html#c.Npp64f)*pSrc2, size_t nLength,[Npp64f](https://docs.nvidia.com/nppdefs.html#c.Npp64f)*pNorm,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDeviceBuffer,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsNormDiff_L1_64f_Ctx)

-
64-bit float L1 norm method on two vectors’ difference

- Parameters
-
**pSrc1**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pSrc2**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**pNorm**– Device memory pointer to the norm result.**pDeviceBuffer**– Pointer to the required device memory allocation,[Scratch Buffer and Host Pointer](https://docs.nvidia.com/introduction.html#general_conventions_lb_1general_scratch_buffer). Use[nppsNormDiffL1GetBufferSize_64f_Ctx](https://docs.nvidia.com#group__signal__l1__norm__diff_1ga209d4096be4ae5eae7150ff65a924685)to determine the minimum number of bytes required.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsNormDiffL1GetBufferSize_16s32f_Ctx(size_t nLength, size_t *hpBufferSize,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsNormDiffL1GetBufferSize_16s32f_Ctx)

-
Device-buffer size (in bytes) for nppsNormDiff_L1_16s32f_Ctx.

- Parameters
-
**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**hpBufferSize**– Required buffer size. Important: hpBufferSize is a*host pointer.***nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
NPP_SUCCESS



-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsNormDiff_L1_16s32f_Ctx(const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrc1, const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrc2, size_t nLength,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pNorm,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDeviceBuffer,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsNormDiff_L1_16s32f_Ctx)

-
16-bit signed short integer L1 norm method on two vectors’ difference, return value is 32-bit float.

- Parameters
-
**pSrc1**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pSrc2**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**pNorm**– Device memory pointer to the L1 norm result.**pDeviceBuffer**– Pointer to the required device memory allocation,[Scratch Buffer and Host Pointer](https://docs.nvidia.com/introduction.html#general_conventions_lb_1general_scratch_buffer). Use[nppsNormDiffL1GetBufferSize_16s32f_Ctx](https://docs.nvidia.com#group__signal__l1__norm__diff_1ga959324081920d990ef669eb68ec56521)to determine the minimum number of bytes required.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsNormDiffL1GetBufferSize_32fc64f_Ctx(size_t nLength, size_t *hpBufferSize,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsNormDiffL1GetBufferSize_32fc64f_Ctx)

-
Device-buffer size (in bytes) for nppsNormDiff_L1_32fc64f_Ctx.

- Parameters
-
**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**hpBufferSize**– Required buffer size. Important: hpBufferSize is a*host pointer.***nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
NPP_SUCCESS



-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsNormDiff_L1_32fc64f_Ctx(const[Npp32fc](https://docs.nvidia.com/nppdefs.html#c.Npp32fc)*pSrc1, const[Npp32fc](https://docs.nvidia.com/nppdefs.html#c.Npp32fc)*pSrc2, size_t nLength,[Npp64f](https://docs.nvidia.com/nppdefs.html#c.Npp64f)*pNorm,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDeviceBuffer,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsNormDiff_L1_32fc64f_Ctx)

-
32-bit float complex L1 norm method on two vectors’ difference, return value is 64-bit float.

- Parameters
-
**pSrc1**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pSrc2**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**pNorm**– Device memory pointer to the norm result.**pDeviceBuffer**– Pointer to the required device memory allocation,[Scratch Buffer and Host Pointer](https://docs.nvidia.com/introduction.html#general_conventions_lb_1general_scratch_buffer). Use[nppsNormDiffL1GetBufferSize_32fc64f_Ctx](https://docs.nvidia.com#group__signal__l1__norm__diff_1ga8913f2e621c12c0068e2e909d787aa88)to determine the minimum number of bytes required.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsNormDiffL1GetBufferSize_64fc64f_Ctx(size_t nLength, size_t *hpBufferSize,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsNormDiffL1GetBufferSize_64fc64f_Ctx)

-
Device-buffer size (in bytes) for nppsNormDiff_L1_64fc64f_Ctx.

- Parameters
-
**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**hpBufferSize**– Required buffer size. Important: hpBufferSize is a*host pointer.***nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
NPP_SUCCESS



-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsNormDiff_L1_64fc64f_Ctx(const[Npp64fc](https://docs.nvidia.com/nppdefs.html#c.Npp64fc)*pSrc1, const[Npp64fc](https://docs.nvidia.com/nppdefs.html#c.Npp64fc)*pSrc2, size_t nLength,[Npp64f](https://docs.nvidia.com/nppdefs.html#c.Npp64f)*pNorm,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDeviceBuffer,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsNormDiff_L1_64fc64f_Ctx)

-
64-bit float complex L1 norm method on two vectors’ difference, return value is 64-bit float.

- Parameters
-
**pSrc1**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pSrc2**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**pNorm**– Device memory pointer to the norm result.**pDeviceBuffer**– Pointer to the required device memory allocation,[Scratch Buffer and Host Pointer](https://docs.nvidia.com/introduction.html#general_conventions_lb_1general_scratch_buffer). Use[nppsNormDiffL1GetBufferSize_64fc64f_Ctx](https://docs.nvidia.com#group__signal__l1__norm__diff_1gab0736dcdc167dd01ab5d683f7e015962)to determine the minimum number of bytes required.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsNormDiffL1GetBufferSize_16s32s_Sfs_Ctx(size_t nLength, size_t *hpBufferSize,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsNormDiffL1GetBufferSize_16s32s_Sfs_Ctx)

-
Device-buffer size (in bytes) for nppsNormDiff_L1_16s32s_Sfs_Ctx.

- Parameters
-
**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**hpBufferSize**– Required buffer size. Important: hpBufferSize is a*host pointer.***nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
NPP_SUCCESS



-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsNormDiff_L1_16s32s_Sfs_Ctx(const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrc1, const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrc2, size_t nLength,[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pNorm, int nScaleFactor,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDeviceBuffer,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsNormDiff_L1_16s32s_Sfs_Ctx)

-
16-bit signed short integer L1 norm method on two vectors’ difference, return value is 32-bit signed integer.

- Parameters
-
**pSrc1**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pSrc2**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer)..**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**pNorm**– Device memory pointer to the norm result.**nScaleFactor**–[Integer Result Scaling](https://docs.nvidia.com/introduction.html#general_conventions_lb_1integer_result_scaling).**pDeviceBuffer**– Pointer to the required device memory allocation,[Scratch Buffer and Host Pointer](https://docs.nvidia.com/introduction.html#general_conventions_lb_1general_scratch_buffer). Use[nppsNormDiffL1GetBufferSize_16s32s_Sfs_Ctx](https://docs.nvidia.com#group__signal__l1__norm__diff_1gae921a6cae3e9a58dab7d04c7f33d1715)to determine the minimum number of bytes required.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsNormDiffL1GetBufferSize_16s64s_Sfs_Ctx(size_t nLength, size_t *hpBufferSize,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsNormDiffL1GetBufferSize_16s64s_Sfs_Ctx)

-
Device-buffer size (in bytes) for nppsNormDiff_L1_16s64s_Sfs_Ctx.

- Parameters
-
**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**hpBufferSize**– Required buffer size. Important: hpBufferSize is a*host pointer.***nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
NPP_SUCCESS



-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsNormDiff_L1_16s64s_Sfs_Ctx(const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrc1, const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrc2, size_t nLength,[Npp64s](https://docs.nvidia.com/nppdefs.html#c.Npp64s)*pNorm, int nScaleFactor,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDeviceBuffer,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsNormDiff_L1_16s64s_Sfs_Ctx)

-
16-bit signed short integer L1 norm method on two vectors’ difference, return value is 64-bit signed integer.

- Parameters
-
**pSrc1**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pSrc2**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**pNorm**– Device memory pointer to the norm result.**nScaleFactor**–[Integer Result Scaling](https://docs.nvidia.com/introduction.html#general_conventions_lb_1integer_result_scaling).**pDeviceBuffer**– Pointer to the required device memory allocation,[Scratch Buffer and Host Pointer](https://docs.nvidia.com/introduction.html#general_conventions_lb_1general_scratch_buffer). Use[nppsNormDiffL1GetBufferSize_16s64s_Sfs_Ctx](https://docs.nvidia.com#group__signal__l1__norm__diff_1ga08d07307ac177a2832f628cc1df64e5f)to determine the minimum number of bytes required.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


### Signal Norm L2 NormDiff[](https://docs.nvidia.com#signal-norm-l2-normdiff)

#### L2 Norm Diff[](https://docs.nvidia.com#group__signal__L2__norm__diff_1signal_L2_norm_diff)

Performs the L2 norm on the samples of two input signals’ difference.

Functions

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsNormDiffL2GetBufferSize_32f_Ctx(size_t nLength, size_t *hpBufferSize,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsNormDiffL2GetBufferSize_32f_Ctx)

-
Device-buffer size (in bytes) for nppsNormDiff_L2_32f_Ctx.

- Parameters
-
**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**hpBufferSize**– Required buffer size. Important: hpBufferSize is a*host pointer.***nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
NPP_SUCCESS



-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsNormDiff_L2_32f_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc1, const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc2, size_t nLength,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pNorm,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDeviceBuffer,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsNormDiff_L2_32f_Ctx)

-
32-bit float L2 norm method on two vectors’ difference

- Parameters
-
**pSrc1**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pSrc2**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**pNorm**– Device memory pointer to the norm result.**pDeviceBuffer**– Pointer to the required device memory allocation,[Scratch Buffer and Host Pointer](https://docs.nvidia.com/introduction.html#general_conventions_lb_1general_scratch_buffer). Use[nppsNormDiffL2GetBufferSize_32f_Ctx](https://docs.nvidia.com#group__signal__l2__norm__diff_1ga420a1b3a25f09d5277cbc3412728d011)to determine the minimum number of bytes required.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsNormDiffL2GetBufferSize_64f_Ctx(size_t nLength, size_t *hpBufferSize,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsNormDiffL2GetBufferSize_64f_Ctx)

-
Device-buffer size (in bytes) for nppsNormDiff_L2_64f_Ctx.

- Parameters
-
**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**hpBufferSize**– Required buffer size. Important: hpBufferSize is a*host pointer.***nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
NPP_SUCCESS



-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsNormDiff_L2_64f_Ctx(const[Npp64f](https://docs.nvidia.com/nppdefs.html#c.Npp64f)*pSrc1, const[Npp64f](https://docs.nvidia.com/nppdefs.html#c.Npp64f)*pSrc2, size_t nLength,[Npp64f](https://docs.nvidia.com/nppdefs.html#c.Npp64f)*pNorm,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDeviceBuffer,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsNormDiff_L2_64f_Ctx)

-
64-bit float L2 norm method on two vectors’ difference

- Parameters
-
**pSrc1**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pSrc2**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**pNorm**– Device memory pointer to the norm result.**pDeviceBuffer**– Pointer to the required device memory allocation,[Scratch Buffer and Host Pointer](https://docs.nvidia.com/introduction.html#general_conventions_lb_1general_scratch_buffer). Use[nppsNormDiffL2GetBufferSize_64f_Ctx](https://docs.nvidia.com#group__signal__l2__norm__diff_1gaa9ea54b7ec340fb45f3ffc8c516db62c)to determine the minimum number of bytes required.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsNormDiffL2GetBufferSize_16s32f_Ctx(size_t nLength, size_t *hpBufferSize,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsNormDiffL2GetBufferSize_16s32f_Ctx)

-
Device-buffer size (in bytes) for nppsNormDiff_L2_16s32f_Ctx.

- Parameters
-
**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**hpBufferSize**– Required buffer size. Important: hpBufferSize is a*host pointer.***nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
NPP_SUCCESS



-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsNormDiff_L2_16s32f_Ctx(const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrc1, const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrc2, size_t nLength,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pNorm,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDeviceBuffer,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsNormDiff_L2_16s32f_Ctx)

-
16-bit signed short integer L2 norm method on two vectors’ difference, return value is 32-bit float.

- Parameters
-
**pSrc1**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pSrc2**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**pNorm**– Device memory pointer to the norm result.**pDeviceBuffer**– Pointer to the required device memory allocation,[Scratch Buffer and Host Pointer](https://docs.nvidia.com/introduction.html#general_conventions_lb_1general_scratch_buffer). Use[nppsNormDiffL2GetBufferSize_16s32f_Ctx](https://docs.nvidia.com#group__signal__l2__norm__diff_1ga48c6adb8b344723eca5f66ab91a0e06c)to determine the minimum number of bytes required.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsNormDiffL2GetBufferSize_32fc64f_Ctx(size_t nLength, size_t *hpBufferSize,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsNormDiffL2GetBufferSize_32fc64f_Ctx)

-
Device-buffer size (in bytes) for nppsNormDiff_L2_32fc64f_Ctx.

- Parameters
-
**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**hpBufferSize**– Required buffer size. Important: hpBufferSize is a*host pointer.***nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
NPP_SUCCESS



-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsNormDiff_L2_32fc64f_Ctx(const[Npp32fc](https://docs.nvidia.com/nppdefs.html#c.Npp32fc)*pSrc1, const[Npp32fc](https://docs.nvidia.com/nppdefs.html#c.Npp32fc)*pSrc2, size_t nLength,[Npp64f](https://docs.nvidia.com/nppdefs.html#c.Npp64f)*pNorm,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDeviceBuffer,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsNormDiff_L2_32fc64f_Ctx)

-
32-bit float complex L2 norm method on two vectors’ difference, return value is 64-bit float.

- Parameters
-
**pSrc1**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pSrc2**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**pNorm**– Device memory pointer to the norm result.**pDeviceBuffer**– Pointer to the required device memory allocation,[Scratch Buffer and Host Pointer](https://docs.nvidia.com/introduction.html#general_conventions_lb_1general_scratch_buffer). Use[nppsNormDiffL2GetBufferSize_32fc64f_Ctx](https://docs.nvidia.com#group__signal__l2__norm__diff_1ga890f164816f47dc1ab9497bd589650d3)to determine the minimum number of bytes required.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsNormDiffL2GetBufferSize_64fc64f_Ctx(size_t nLength, size_t *hpBufferSize,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsNormDiffL2GetBufferSize_64fc64f_Ctx)

-
Device-buffer size (in bytes) for nppsNormDiff_L2_64fc64f_Ctx.

- Parameters
-
**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**hpBufferSize**– Required buffer size. Important: hpBufferSize is a*host pointer.***nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
NPP_SUCCESS



-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsNormDiff_L2_64fc64f_Ctx(const[Npp64fc](https://docs.nvidia.com/nppdefs.html#c.Npp64fc)*pSrc1, const[Npp64fc](https://docs.nvidia.com/nppdefs.html#c.Npp64fc)*pSrc2, size_t nLength,[Npp64f](https://docs.nvidia.com/nppdefs.html#c.Npp64f)*pNorm,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDeviceBuffer,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsNormDiff_L2_64fc64f_Ctx)

-
64-bit float complex L2 norm method on two vectors’ difference, return value is 64-bit float.

- Parameters
-
**pSrc1**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pSrc2**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**pNorm**– Device memory pointer to the norm result.**pDeviceBuffer**– Pointer to the required device memory allocation,[Scratch Buffer and Host Pointer](https://docs.nvidia.com/introduction.html#general_conventions_lb_1general_scratch_buffer). Use[nppsNormDiffL2GetBufferSize_64fc64f_Ctx](https://docs.nvidia.com#group__signal__l2__norm__diff_1gaaec9ac0635fed117b80e8394bb89b16c)to determine the minimum number of bytes required.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsNormDiffL2GetBufferSize_16s32s_Sfs_Ctx(size_t nLength, size_t *hpBufferSize,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsNormDiffL2GetBufferSize_16s32s_Sfs_Ctx)

-
Device-buffer size (in bytes) for nppsNormDiff_L2_16s32s_Sfs_Ctx.

- Parameters
-
**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**hpBufferSize**– Required buffer size. Important: hpBufferSize is a*host pointer.***nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
NPP_SUCCESS



-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsNormDiff_L2_16s32s_Sfs_Ctx(const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrc1, const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrc2, size_t nLength,[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pNorm, int nScaleFactor,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDeviceBuffer,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsNormDiff_L2_16s32s_Sfs_Ctx)

-
16-bit signed short integer L2 norm method on two vectors’ difference, return value is 32-bit signed integer.

- Parameters
-
**pSrc1**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pSrc2**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**pNorm**– Device memory pointer to the norm result.**nScaleFactor**–[Integer Result Scaling](https://docs.nvidia.com/introduction.html#general_conventions_lb_1integer_result_scaling).**pDeviceBuffer**– Pointer to the required device memory allocation,[Scratch Buffer and Host Pointer](https://docs.nvidia.com/introduction.html#general_conventions_lb_1general_scratch_buffer). Use[nppsNormDiffL2GetBufferSize_16s32s_Sfs_Ctx](https://docs.nvidia.com#group__signal__l2__norm__diff_1ga71007b38d7402d25eaed706e261138a8)to determine the minimum number of bytes required.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsNormDiffL2SqrGetBufferSize_16s64s_Sfs_Ctx(size_t nLength, size_t *hpBufferSize,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsNormDiffL2SqrGetBufferSize_16s64s_Sfs_Ctx)

-
Device-buffer size (in bytes) for nppsNormDiff_L2Sqr_16s64s_Sfs_Ctx.

- Parameters
-
**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**hpBufferSize**– Required buffer size. Important: hpBufferSize is a*host pointer.***nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
NPP_SUCCESS



-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsNormDiff_L2Sqr_16s64s_Sfs_Ctx(const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrc1, const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrc2, size_t nLength,[Npp64s](https://docs.nvidia.com/nppdefs.html#c.Npp64s)*pNorm, int nScaleFactor,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDeviceBuffer,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsNormDiff_L2Sqr_16s64s_Sfs_Ctx)

-
16-bit signed short integer L2 Square norm method on two vectors’ difference, return value is 64-bit signed integer.

- Parameters
-
**pSrc1**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pSrc2**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**pNorm**– Device memory pointer to the norm result.**nScaleFactor**–[Integer Result Scaling](https://docs.nvidia.com/introduction.html#general_conventions_lb_1integer_result_scaling).**pDeviceBuffer**– Pointer to the required device memory allocation,[Scratch Buffer and Host Pointer](https://docs.nvidia.com/introduction.html#general_conventions_lb_1general_scratch_buffer). Use[nppsNormDiffL2SqrGetBufferSize_16s64s_Sfs_Ctx](https://docs.nvidia.com#group__signal__l2__norm__diff_1gadc87037c52252cb4ea399223080ae0d1)to determine the minimum number of bytes required.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


## Signal Dot Product[](https://docs.nvidia.com#signal-dot-product)

### Dot Product[](https://docs.nvidia.com#group__signal__dot__product_1signal_dot_product)

Performs the dot product operation on the samples of two input signals.

Functions

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsDotProdGetBufferSize_32f_Ctx(size_t nLength, size_t *hpBufferSize,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsDotProdGetBufferSize_32f_Ctx)

-
Device-buffer size (in bytes) for nppsDotProd_32f_Ctx.

- Parameters
-
**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**hpBufferSize**– Required buffer size. Important: hpBufferSize is a*host pointer.***nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
NPP_SUCCESS



-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsDotProd_32f_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc1, const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc2, size_t nLength,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pDp,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDeviceBuffer,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsDotProd_32f_Ctx)

-
32-bit float dot product method, return value is 32-bit float.

- Parameters
-
**pSrc1**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pSrc2**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**pDp**– Device memory pointer to the dot product result.**pDeviceBuffer**– Pointer to the required device memory allocation,[Scratch Buffer and Host Pointer](https://docs.nvidia.com/introduction.html#general_conventions_lb_1general_scratch_buffer). Use[nppsDotProdGetBufferSize_32f_Ctx](https://docs.nvidia.com#group__signal__dot__product_1ga9b572445400fbdf711dc60e01b6c9edc)to determine the minimum number of bytes required.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsDotProdGetBufferSize_32fc_Ctx(size_t nLength, size_t *hpBufferSize,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsDotProdGetBufferSize_32fc_Ctx)

-
Device-buffer size (in bytes) for nppsDotProd_32fc_Ctx.

- Parameters
-
**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**hpBufferSize**– Required buffer size. Important: hpBufferSize is a*host pointer.***nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
NPP_SUCCESS



-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsDotProd_32fc_Ctx(const[Npp32fc](https://docs.nvidia.com/nppdefs.html#c.Npp32fc)*pSrc1, const[Npp32fc](https://docs.nvidia.com/nppdefs.html#c.Npp32fc)*pSrc2, size_t nLength,[Npp32fc](https://docs.nvidia.com/nppdefs.html#c.Npp32fc)*pDp,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDeviceBuffer,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsDotProd_32fc_Ctx)

-
32-bit float complex dot product method, return value is 32-bit float complex.

- Parameters
-
**pSrc1**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pSrc2**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**pDp**– Device memory pointer to the dot product result.**pDeviceBuffer**– Pointer to the required device memory allocation,[Scratch Buffer and Host Pointer](https://docs.nvidia.com/introduction.html#general_conventions_lb_1general_scratch_buffer). Use[nppsDotProdGetBufferSize_32fc_Ctx](https://docs.nvidia.com#group__signal__dot__product_1ga4a44aa96799fdf1e4332966e81464f5c)to determine the minimum number of bytes required.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsDotProdGetBufferSize_32f32fc_Ctx(size_t nLength, size_t *hpBufferSize,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsDotProdGetBufferSize_32f32fc_Ctx)

-
Device-buffer size (in bytes) for nppsDotProd_32f32fc_Ctx.

- Parameters
-
**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**hpBufferSize**– Required buffer size. Important: hpBufferSize is a*host pointer.***nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
NPP_SUCCESS



-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsDotProd_32f32fc_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc1, const[Npp32fc](https://docs.nvidia.com/nppdefs.html#c.Npp32fc)*pSrc2, size_t nLength,[Npp32fc](https://docs.nvidia.com/nppdefs.html#c.Npp32fc)*pDp,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDeviceBuffer,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsDotProd_32f32fc_Ctx)

-
32-bit float and 32-bit float complex dot product method, return value is 32-bit float complex.

- Parameters
-
**pSrc1**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pSrc2**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**pDp**– Device memory pointer to the dot product result.**pDeviceBuffer**– Pointer to the required device memory allocation,[Scratch Buffer and Host Pointer](https://docs.nvidia.com/introduction.html#general_conventions_lb_1general_scratch_buffer). Use[nppsDotProdGetBufferSize_32f32fc_Ctx](https://docs.nvidia.com#group__signal__dot__product_1ga1d18141ef66d7f98942c27e0b134e07f)to determine the minimum number of bytes required.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsDotProdGetBufferSize_32f64f_Ctx(size_t nLength, size_t *hpBufferSize,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsDotProdGetBufferSize_32f64f_Ctx)

-
Device-buffer size (in bytes) for nppsDotProd_32f64f_Ctx.

- Parameters
-
**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**hpBufferSize**– Required buffer size. Important: hpBufferSize is a*host pointer.***nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
NPP_SUCCESS



-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsDotProd_32f64f_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc1, const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc2, size_t nLength,[Npp64f](https://docs.nvidia.com/nppdefs.html#c.Npp64f)*pDp,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDeviceBuffer,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsDotProd_32f64f_Ctx)

-
32-bit float dot product method, return value is 64-bit float.

- Parameters
-
**pSrc1**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pSrc2**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**pDp**– Device memory pointer to the dot product result.**pDeviceBuffer**– Pointer to the required device memory allocation,[Scratch Buffer and Host Pointer](https://docs.nvidia.com/introduction.html#general_conventions_lb_1general_scratch_buffer). Use[nppsDotProdGetBufferSize_32f64f_Ctx](https://docs.nvidia.com#group__signal__dot__product_1gaf895e9b1d7ae5baad29a51d4ccfae858)to determine the minimum number of bytes required.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsDotProdGetBufferSize_32fc64fc_Ctx(size_t nLength, size_t *hpBufferSize,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsDotProdGetBufferSize_32fc64fc_Ctx)

-
Device-buffer size (in bytes) for nppsDotProd_32fc64fc_Ctx.

- Parameters
-
**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**hpBufferSize**– Required buffer size. Important: hpBufferSize is a*host pointer.***nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
NPP_SUCCESS



-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsDotProd_32fc64fc_Ctx(const[Npp32fc](https://docs.nvidia.com/nppdefs.html#c.Npp32fc)*pSrc1, const[Npp32fc](https://docs.nvidia.com/nppdefs.html#c.Npp32fc)*pSrc2, size_t nLength,[Npp64fc](https://docs.nvidia.com/nppdefs.html#c.Npp64fc)*pDp,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDeviceBuffer,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsDotProd_32fc64fc_Ctx)

-
32-bit float complex dot product method, return value is 64-bit float complex.

- Parameters
-
**pSrc1**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pSrc2**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**pDp**– Device memory pointer to the dot product result.**pDeviceBuffer**– Pointer to the required device memory allocation,[Scratch Buffer and Host Pointer](https://docs.nvidia.com/introduction.html#general_conventions_lb_1general_scratch_buffer). Use[nppsDotProdGetBufferSize_32fc64fc_Ctx](https://docs.nvidia.com#group__signal__dot__product_1gabce4f9ec427ece7cf775ddf97b12cc04)to determine the minimum number of bytes required.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsDotProdGetBufferSize_32f32fc64fc_Ctx(size_t nLength, size_t *hpBufferSize,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsDotProdGetBufferSize_32f32fc64fc_Ctx)

-
Device-buffer size (in bytes) for nppsDotProd_32f32fc64fc_Ctx.

- Parameters
-
**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**hpBufferSize**– Required buffer size. Important: hpBufferSize is a*host pointer.***nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
NPP_SUCCESS



-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsDotProd_32f32fc64fc_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc1, const[Npp32fc](https://docs.nvidia.com/nppdefs.html#c.Npp32fc)*pSrc2, size_t nLength,[Npp64fc](https://docs.nvidia.com/nppdefs.html#c.Npp64fc)*pDp,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDeviceBuffer,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsDotProd_32f32fc64fc_Ctx)

-
32-bit float and 32-bit float complex dot product method, return value is 64-bit float complex.

- Parameters
-
**pSrc1**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pSrc2**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**pDp**– Device memory pointer to the dot product result.**pDeviceBuffer**– Pointer to the required device memory allocation,[Scratch Buffer and Host Pointer](https://docs.nvidia.com/introduction.html#general_conventions_lb_1general_scratch_buffer). Use[nppsDotProdGetBufferSize_32f32fc64fc_Ctx](https://docs.nvidia.com#group__signal__dot__product_1ga73debc3e23047d7d77dcf520d84c9baa)to determine the minimum number of bytes required.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsDotProdGetBufferSize_64f_Ctx(size_t nLength, size_t *hpBufferSize,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsDotProdGetBufferSize_64f_Ctx)

-
Device-buffer size (in bytes) for nppsDotProd_64f_Ctx.

- Parameters
-
**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**hpBufferSize**– Required buffer size. Important: hpBufferSize is a*host pointer.***nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
NPP_SUCCESS



-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsDotProd_64f_Ctx(const[Npp64f](https://docs.nvidia.com/nppdefs.html#c.Npp64f)*pSrc1, const[Npp64f](https://docs.nvidia.com/nppdefs.html#c.Npp64f)*pSrc2, size_t nLength,[Npp64f](https://docs.nvidia.com/nppdefs.html#c.Npp64f)*pDp,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDeviceBuffer,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsDotProd_64f_Ctx)

-
64-bit float dot product method, return value is 64-bit float.

- Parameters
-
**pSrc1**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pSrc2**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**pDp**– Device memory pointer to the dot product result.**pDeviceBuffer**– Pointer to the required device memory allocation,[Scratch Buffer and Host Pointer](https://docs.nvidia.com/introduction.html#general_conventions_lb_1general_scratch_buffer). Use[nppsDotProdGetBufferSize_64f_Ctx](https://docs.nvidia.com#group__signal__dot__product_1gaa58697f626c188f4168ae4013e26857d)to determine the minimum number of bytes required.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsDotProdGetBufferSize_64fc_Ctx(size_t nLength, size_t *hpBufferSize,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsDotProdGetBufferSize_64fc_Ctx)

-
Device-buffer size (in bytes) for nppsDotProd_64fc_Ctx.

- Parameters
-
**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**hpBufferSize**– Required buffer size. Important: hpBufferSize is a*host pointer.***nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
NPP_SUCCESS



-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsDotProd_64fc_Ctx(const[Npp64fc](https://docs.nvidia.com/nppdefs.html#c.Npp64fc)*pSrc1, const[Npp64fc](https://docs.nvidia.com/nppdefs.html#c.Npp64fc)*pSrc2, size_t nLength,[Npp64fc](https://docs.nvidia.com/nppdefs.html#c.Npp64fc)*pDp,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDeviceBuffer,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsDotProd_64fc_Ctx)

-
64-bit float complex dot product method, return value is 64-bit float complex.

- Parameters
-
**pSrc1**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pSrc2**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**pDp**– Device memory pointer to the dot product result.**pDeviceBuffer**– Pointer to the required device memory allocation,[Scratch Buffer and Host Pointer](https://docs.nvidia.com/introduction.html#general_conventions_lb_1general_scratch_buffer). Use[nppsDotProdGetBufferSize_64fc_Ctx](https://docs.nvidia.com#group__signal__dot__product_1gac2ea90d1291df49d7a15b3f21439b461)to determine the minimum number of bytes required.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsDotProdGetBufferSize_64f64fc_Ctx(size_t nLength, size_t *hpBufferSize,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsDotProdGetBufferSize_64f64fc_Ctx)

-
Device-buffer size (in bytes) for nppsDotProd_64f64fc_Ctx.

- Parameters
-
**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**hpBufferSize**– Required buffer size. Important: hpBufferSize is a*host pointer.***nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
NPP_SUCCESS



-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsDotProd_64f64fc_Ctx(const[Npp64f](https://docs.nvidia.com/nppdefs.html#c.Npp64f)*pSrc1, const[Npp64fc](https://docs.nvidia.com/nppdefs.html#c.Npp64fc)*pSrc2, size_t nLength,[Npp64fc](https://docs.nvidia.com/nppdefs.html#c.Npp64fc)*pDp,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDeviceBuffer,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsDotProd_64f64fc_Ctx)

-
64-bit float and 64-bit float complex dot product method, return value is 64-bit float complex.

- Parameters
-
**pSrc1**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pSrc2**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**pDp**– Device memory pointer to the dot product result.**pDeviceBuffer**– Pointer to the required device memory allocation,[Scratch Buffer and Host Pointer](https://docs.nvidia.com/introduction.html#general_conventions_lb_1general_scratch_buffer). Use[nppsDotProdGetBufferSize_64f64fc_Ctx](https://docs.nvidia.com#group__signal__dot__product_1gac4a7df7b98a094a264c9298674ec8d0a)to determine the minimum number of bytes required.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsDotProdGetBufferSize_16s64s_Ctx(size_t nLength, size_t *hpBufferSize,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsDotProdGetBufferSize_16s64s_Ctx)

-
Device-buffer size (in bytes) for nppsDotProd_16s64s_Ctx.

- Parameters
-
**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**hpBufferSize**– Required buffer size. Important: hpBufferSize is a*host pointer.***nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
NPP_SUCCESS



-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsDotProd_16s64s_Ctx(const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrc1, const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrc2, size_t nLength,[Npp64s](https://docs.nvidia.com/nppdefs.html#c.Npp64s)*pDp,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDeviceBuffer,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsDotProd_16s64s_Ctx)

-
16-bit signed short integer dot product method, return value is 64-bit signed integer.

- Parameters
-
**pSrc1**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pSrc2**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**pDp**– Device memory pointer to the dot product result.**pDeviceBuffer**– Pointer to the required device memory allocation,[Scratch Buffer and Host Pointer](https://docs.nvidia.com/introduction.html#general_conventions_lb_1general_scratch_buffer). Use[nppsDotProdGetBufferSize_16s64s_Ctx](https://docs.nvidia.com#group__signal__dot__product_1gac027d60a57ec818d49272f99d7152ca4)to determine the minimum number of bytes required.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsDotProdGetBufferSize_16sc64sc_Ctx(size_t nLength, size_t *hpBufferSize,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsDotProdGetBufferSize_16sc64sc_Ctx)

-
Device-buffer size (in bytes) for nppsDotProd_16sc64sc_Ctx.

- Parameters
-
**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**hpBufferSize**– Required buffer size. Important: hpBufferSize is a*host pointer.***nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
NPP_SUCCESS



-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsDotProd_16sc64sc_Ctx(const[Npp16sc](https://docs.nvidia.com/nppdefs.html#c.Npp16sc)*pSrc1, const[Npp16sc](https://docs.nvidia.com/nppdefs.html#c.Npp16sc)*pSrc2, size_t nLength,[Npp64sc](https://docs.nvidia.com/nppdefs.html#c.Npp64sc)*pDp,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDeviceBuffer,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsDotProd_16sc64sc_Ctx)

-
16-bit signed short integer complex dot product method, return value is 64-bit signed integer complex.

- Parameters
-
**pSrc1**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pSrc2**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**pDp**– Device memory pointer to the dot product result.**pDeviceBuffer**– Pointer to the required device memory allocation,[Scratch Buffer and Host Pointer](https://docs.nvidia.com/introduction.html#general_conventions_lb_1general_scratch_buffer). Use[nppsDotProdGetBufferSize_16sc64sc_Ctx](https://docs.nvidia.com#group__signal__dot__product_1ga8885cb8f3ec25b84ae9cc64dd1ef105e)to determine the minimum number of bytes required.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsDotProdGetBufferSize_16s16sc64sc_Ctx(size_t nLength, size_t *hpBufferSize,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsDotProdGetBufferSize_16s16sc64sc_Ctx)

-
Device-buffer size (in bytes) for nppsDotProd_16s16sc64sc_Ctx.

- Parameters
-
**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**hpBufferSize**– Required buffer size. Important: hpBufferSize is a*host pointer.***nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
NPP_SUCCESS



-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsDotProd_16s16sc64sc_Ctx(const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrc1, const[Npp16sc](https://docs.nvidia.com/nppdefs.html#c.Npp16sc)*pSrc2, size_t nLength,[Npp64sc](https://docs.nvidia.com/nppdefs.html#c.Npp64sc)*pDp,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDeviceBuffer,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsDotProd_16s16sc64sc_Ctx)

-
16-bit signed short integer and 16-bit signed short integer short dot product method, return value is 64-bit signed integer complex.

- Parameters
-
**pSrc1**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pSrc2**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**pDp**– Device memory pointer to the dot product result.**pDeviceBuffer**– Pointer to the required device memory allocation,[Scratch Buffer and Host Pointer](https://docs.nvidia.com/introduction.html#general_conventions_lb_1general_scratch_buffer). Use[nppsDotProdGetBufferSize_16s16sc64sc_Ctx](https://docs.nvidia.com#group__signal__dot__product_1ga0a000e287ea104c65ebf81fa0a81174f)to determine the minimum number of bytes required.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsDotProdGetBufferSize_16s32f_Ctx(size_t nLength, size_t *hpBufferSize,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsDotProdGetBufferSize_16s32f_Ctx)

-
Device-buffer size (in bytes) for nppsDotProd_16s32f_Ctx.

- Parameters
-
**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**hpBufferSize**– Required buffer size. Important: hpBufferSize is a*host pointer.***nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
NPP_SUCCESS



-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsDotProd_16s32f_Ctx(const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrc1, const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrc2, size_t nLength,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pDp,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDeviceBuffer,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsDotProd_16s32f_Ctx)

-
16-bit signed short integer dot product method, return value is 32-bit float.

- Parameters
-
**pSrc1**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pSrc2**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**pDp**– Device memory pointer to the dot product result.**pDeviceBuffer**– Pointer to the required device memory allocation,[Scratch Buffer and Host Pointer](https://docs.nvidia.com/introduction.html#general_conventions_lb_1general_scratch_buffer). Use[nppsDotProdGetBufferSize_16s32f_Ctx](https://docs.nvidia.com#group__signal__dot__product_1gad439ac22a2ba38b6c61916dc0ba8f08c)to determine the minimum number of bytes required.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsDotProdGetBufferSize_16sc32fc_Ctx(size_t nLength, size_t *hpBufferSize,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsDotProdGetBufferSize_16sc32fc_Ctx)

-
Device-buffer size (in bytes) for nppsDotProd_16sc32fc_Ctx.

- Parameters
-
**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**hpBufferSize**– Required buffer size. Important: hpBufferSize is a*host pointer.***nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
NPP_SUCCESS



-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsDotProd_16sc32fc_Ctx(const[Npp16sc](https://docs.nvidia.com/nppdefs.html#c.Npp16sc)*pSrc1, const[Npp16sc](https://docs.nvidia.com/nppdefs.html#c.Npp16sc)*pSrc2, size_t nLength,[Npp32fc](https://docs.nvidia.com/nppdefs.html#c.Npp32fc)*pDp,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDeviceBuffer,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsDotProd_16sc32fc_Ctx)

-
16-bit signed short integer complex dot product method, return value is 32-bit float complex.

- Parameters
-
**pSrc1**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pSrc2**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**pDp**– Device memory pointer to the dot product result.**pDeviceBuffer**– Pointer to the required device memory allocation,[Scratch Buffer and Host Pointer](https://docs.nvidia.com/introduction.html#general_conventions_lb_1general_scratch_buffer). Use[nppsDotProdGetBufferSize_16sc32fc_Ctx](https://docs.nvidia.com#group__signal__dot__product_1gaf6cd60c9ca967278dc2eeddda3be57d2)to determine the minimum number of bytes required.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsDotProdGetBufferSize_16s16sc32fc_Ctx(size_t nLength, size_t *hpBufferSize,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsDotProdGetBufferSize_16s16sc32fc_Ctx)

-
Device-buffer size (in bytes) for nppsDotProd_16s16sc32fc_Ctx.

- Parameters
-
**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**hpBufferSize**– Required buffer size. Important: hpBufferSize is a*host pointer.***nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
NPP_SUCCESS



-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsDotProd_16s16sc32fc_Ctx(const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrc1, const[Npp16sc](https://docs.nvidia.com/nppdefs.html#c.Npp16sc)*pSrc2, size_t nLength,[Npp32fc](https://docs.nvidia.com/nppdefs.html#c.Npp32fc)*pDp,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDeviceBuffer,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsDotProd_16s16sc32fc_Ctx)

-
16-bit signed short integer and 16-bit signed short integer complex dot product method, return value is 32-bit float complex.

- Parameters
-
**pSrc1**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pSrc2**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**pDp**– Device memory pointer to the dot product result.**pDeviceBuffer**– Pointer to the required device memory allocation,[Scratch Buffer and Host Pointer](https://docs.nvidia.com/introduction.html#general_conventions_lb_1general_scratch_buffer). Use[nppsDotProdGetBufferSize_16s16sc32fc_Ctx](https://docs.nvidia.com#group__signal__dot__product_1gaa91f22994b3ae0da8c2cdc3a9a0dbed7)to determine the minimum number of bytes required.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsDotProdGetBufferSize_16s_Sfs_Ctx(size_t nLength, size_t *hpBufferSize,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsDotProdGetBufferSize_16s_Sfs_Ctx)

-
Device-buffer size (in bytes) for nppsDotProd_16s_Sfs_Ctx.

- Parameters
-
**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**hpBufferSize**– Required buffer size. Important: hpBufferSize is a*host pointer.***nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
NPP_SUCCESS



-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsDotProd_16s_Sfs_Ctx(const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrc1, const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrc2, size_t nLength,[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pDp, int nScaleFactor,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDeviceBuffer,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsDotProd_16s_Sfs_Ctx)

-
16-bit signed short integer dot product method, return value is 16-bit signed short integer.

- Parameters
-
**pSrc1**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pSrc2**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**pDp**– Device memory pointer to the dot product result.**nScaleFactor**–[Integer Result Scaling](https://docs.nvidia.com/introduction.html#general_conventions_lb_1integer_result_scaling).**pDeviceBuffer**– Pointer to the required device memory allocation,[Scratch Buffer and Host Pointer](https://docs.nvidia.com/introduction.html#general_conventions_lb_1general_scratch_buffer). Use[nppsDotProdGetBufferSize_16s_Sfs_Ctx](https://docs.nvidia.com#group__signal__dot__product_1gad593c5b5013015658ba91b64c88d05ea)to determine the minimum number of bytes required.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsDotProdGetBufferSize_16sc_Sfs_Ctx(size_t nLength, size_t *hpBufferSize,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsDotProdGetBufferSize_16sc_Sfs_Ctx)

-
Device-buffer size (in bytes) for nppsDotProd_16sc_Sfs_Ctx.

- Parameters
-
**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**hpBufferSize**– Required buffer size. Important: hpBufferSize is a*host pointer.***nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
NPP_SUCCESS



-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsDotProd_16sc_Sfs_Ctx(const[Npp16sc](https://docs.nvidia.com/nppdefs.html#c.Npp16sc)*pSrc1, const[Npp16sc](https://docs.nvidia.com/nppdefs.html#c.Npp16sc)*pSrc2, size_t nLength,[Npp16sc](https://docs.nvidia.com/nppdefs.html#c.Npp16sc)*pDp, int nScaleFactor,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDeviceBuffer,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsDotProd_16sc_Sfs_Ctx)

-
16-bit signed short integer complex dot product method, return value is 16-bit signed short integer complex.

- Parameters
-
**pSrc1**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pSrc2**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**pDp**– Device memory pointer to the dot product result.**nScaleFactor**–[Integer Result Scaling](https://docs.nvidia.com/introduction.html#general_conventions_lb_1integer_result_scaling).**pDeviceBuffer**– Pointer to the required device memory allocation,[Scratch Buffer and Host Pointer](https://docs.nvidia.com/introduction.html#general_conventions_lb_1general_scratch_buffer). Use[nppsDotProdGetBufferSize_16sc_Sfs_Ctx](https://docs.nvidia.com#group__signal__dot__product_1gac218952309f5e3c72eeddbd983082725)to determine the minimum number of bytes required.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsDotProdGetBufferSize_32s_Sfs_Ctx(size_t nLength, size_t *hpBufferSize,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsDotProdGetBufferSize_32s_Sfs_Ctx)

-
Device-buffer size (in bytes) for nppsDotProd_32s_Sfs_Ctx.

- Parameters
-
**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**hpBufferSize**– Required buffer size. Important: hpBufferSize is a*host pointer.***nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
NPP_SUCCESS



-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsDotProd_32s_Sfs_Ctx(const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pSrc1, const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pSrc2, size_t nLength,[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pDp, int nScaleFactor,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDeviceBuffer,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsDotProd_32s_Sfs_Ctx)

-
32-bit signed integer dot product method, return value is 32-bit signed integer.

- Parameters
-
**pSrc1**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pSrc2**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**pDp**– Device memory pointer to the dot product result.**nScaleFactor**–[Integer Result Scaling](https://docs.nvidia.com/introduction.html#general_conventions_lb_1integer_result_scaling).**pDeviceBuffer**– Pointer to the required device memory allocation,[Scratch Buffer and Host Pointer](https://docs.nvidia.com/introduction.html#general_conventions_lb_1general_scratch_buffer). Use[nppsDotProdGetBufferSize_32s_Sfs_Ctx](https://docs.nvidia.com#group__signal__dot__product_1gac9b0516a2be7ef8d2aab82d73f5d598b)to determine the minimum number of bytes required.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsDotProdGetBufferSize_32sc_Sfs_Ctx(size_t nLength, size_t *hpBufferSize,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsDotProdGetBufferSize_32sc_Sfs_Ctx)

-
Device-buffer size (in bytes) for nppsDotProd_32sc_Sfs_Ctx.

- Parameters
-
**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**hpBufferSize**– Required buffer size. Important: hpBufferSize is a*host pointer.***nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
NPP_SUCCESS



-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsDotProd_32sc_Sfs_Ctx(const[Npp32sc](https://docs.nvidia.com/nppdefs.html#c.Npp32sc)*pSrc1, const[Npp32sc](https://docs.nvidia.com/nppdefs.html#c.Npp32sc)*pSrc2, size_t nLength,[Npp32sc](https://docs.nvidia.com/nppdefs.html#c.Npp32sc)*pDp, int nScaleFactor,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDeviceBuffer,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsDotProd_32sc_Sfs_Ctx)

-
32-bit signed integer complex dot product method, return value is 32-bit signed integer complex.

- Parameters
-
**pSrc1**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pSrc2**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**pDp**– Device memory pointer to the dot product result.**nScaleFactor**–[Integer Result Scaling](https://docs.nvidia.com/introduction.html#general_conventions_lb_1integer_result_scaling).**pDeviceBuffer**– Pointer to the required device memory allocation,[Scratch Buffer and Host Pointer](https://docs.nvidia.com/introduction.html#general_conventions_lb_1general_scratch_buffer). Use[nppsDotProdGetBufferSize_32sc_Sfs_Ctx](https://docs.nvidia.com#group__signal__dot__product_1gaa487465296323e7b36c68406e6c5cf71)to determine the minimum number of bytes required.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsDotProdGetBufferSize_16s32s_Sfs_Ctx(size_t nLength, size_t *hpBufferSize,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsDotProdGetBufferSize_16s32s_Sfs_Ctx)

-
Device-buffer size (in bytes) for nppsDotProd_16s32s_Sfs_Ctx.

- Parameters
-
**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**hpBufferSize**– Required buffer size. Important: hpBufferSize is a*host pointer.***nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
NPP_SUCCESS



-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsDotProd_16s32s_Sfs_Ctx(const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrc1, const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrc2, size_t nLength,[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pDp, int nScaleFactor,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDeviceBuffer,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsDotProd_16s32s_Sfs_Ctx)

-
16-bit signed short integer dot product method, return value is 32-bit signed integer.

- Parameters
-
**pSrc1**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pSrc2**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**pDp**– Device memory pointer to the dot product result.**nScaleFactor**–[Integer Result Scaling](https://docs.nvidia.com/introduction.html#general_conventions_lb_1integer_result_scaling).**pDeviceBuffer**– Pointer to the required device memory allocation,[Scratch Buffer and Host Pointer](https://docs.nvidia.com/introduction.html#general_conventions_lb_1general_scratch_buffer). Use[nppsDotProdGetBufferSize_16s32s_Sfs_Ctx](https://docs.nvidia.com#group__signal__dot__product_1ga742d3829b87e46e229416d6db1e563ae)to determine the minimum number of bytes required.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsDotProdGetBufferSize_16s16sc32sc_Sfs_Ctx(size_t nLength, size_t *hpBufferSize,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsDotProdGetBufferSize_16s16sc32sc_Sfs_Ctx)

-
Device-buffer size (in bytes) for nppsDotProd_16s16sc32sc_Sfs_Ctx.

- Parameters
-
**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**hpBufferSize**– Required buffer size. Important: hpBufferSize is a*host pointer.***nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
NPP_SUCCESS



-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsDotProd_16s16sc32sc_Sfs_Ctx(const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrc1, const[Npp16sc](https://docs.nvidia.com/nppdefs.html#c.Npp16sc)*pSrc2, size_t nLength,[Npp32sc](https://docs.nvidia.com/nppdefs.html#c.Npp32sc)*pDp, int nScaleFactor,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDeviceBuffer,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsDotProd_16s16sc32sc_Sfs_Ctx)

-
16-bit signed short integer and 16-bit signed short integer complex dot product method, return value is 32-bit signed integer complex.

- Parameters
-
**pSrc1**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pSrc2**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**pDp**– Device memory pointer to the dot product result.**nScaleFactor**–[Integer Result Scaling](https://docs.nvidia.com/introduction.html#general_conventions_lb_1integer_result_scaling).**pDeviceBuffer**– Pointer to the required device memory allocation,[Scratch Buffer and Host Pointer](https://docs.nvidia.com/introduction.html#general_conventions_lb_1general_scratch_buffer). Use[nppsDotProdGetBufferSize_16s16sc32sc_Sfs_Ctx](https://docs.nvidia.com#group__signal__dot__product_1gad80a1bf5816260611c5575a7753a4cbd)to determine the minimum number of bytes required.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsDotProdGetBufferSize_16s32s32s_Sfs_Ctx(size_t nLength, size_t *hpBufferSize,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsDotProdGetBufferSize_16s32s32s_Sfs_Ctx)

-
Device-buffer size (in bytes) for nppsDotProd_16s32s32s_Sfs_Ctx.

- Parameters
-
**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**hpBufferSize**– Required buffer size. Important: hpBufferSize is a*host pointer.***nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
NPP_SUCCESS



-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsDotProd_16s32s32s_Sfs_Ctx(const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrc1, const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pSrc2, size_t nLength,[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pDp, int nScaleFactor,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDeviceBuffer,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsDotProd_16s32s32s_Sfs_Ctx)

-
16-bit signed short integer and 32-bit signed integer dot product method, return value is 32-bit signed integer.

- Parameters
-
**pSrc1**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pSrc2**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**pDp**– Device memory pointer to the dot product result.**nScaleFactor**–[Integer Result Scaling](https://docs.nvidia.com/introduction.html#general_conventions_lb_1integer_result_scaling).**pDeviceBuffer**– Pointer to the required device memory allocation,[Scratch Buffer and Host Pointer](https://docs.nvidia.com/introduction.html#general_conventions_lb_1general_scratch_buffer). Use[nppsDotProdGetBufferSize_16s32s32s_Sfs_Ctx](https://docs.nvidia.com#group__signal__dot__product_1gaea0744b3835058ff329903f9f65b2553)to determine the minimum number of bytes required.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsDotProdGetBufferSize_16s16sc_Sfs_Ctx(size_t nLength, size_t *hpBufferSize,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsDotProdGetBufferSize_16s16sc_Sfs_Ctx)

-
Device-buffer size (in bytes) for nppsDotProd_16s16sc_Sfs_Ctx.

- Parameters
-
**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**hpBufferSize**– Required buffer size. Important: hpBufferSize is a*host pointer.***nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
NPP_SUCCESS



-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsDotProd_16s16sc_Sfs_Ctx(const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrc1, const[Npp16sc](https://docs.nvidia.com/nppdefs.html#c.Npp16sc)*pSrc2, size_t nLength,[Npp16sc](https://docs.nvidia.com/nppdefs.html#c.Npp16sc)*pDp, int nScaleFactor,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDeviceBuffer,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsDotProd_16s16sc_Sfs_Ctx)

-
16-bit signed short integer and 16-bit signed short integer complex dot product method, return value is 16-bit signed short integer complex.

- Parameters
-
**pSrc1**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pSrc2**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**pDp**– Device memory pointer to the dot product result.**nScaleFactor**–[Integer Result Scaling](https://docs.nvidia.com/introduction.html#general_conventions_lb_1integer_result_scaling).**pDeviceBuffer**– Pointer to the required device memory allocation,[Scratch Buffer and Host Pointer](https://docs.nvidia.com/introduction.html#general_conventions_lb_1general_scratch_buffer). Use[nppsDotProdGetBufferSize_16s16sc_Sfs_Ctx](https://docs.nvidia.com#group__signal__dot__product_1gab449f438d33c54fdc47edc4efd4df057)to determine the minimum number of bytes required.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsDotProdGetBufferSize_16sc32sc_Sfs_Ctx(size_t nLength, size_t *hpBufferSize,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsDotProdGetBufferSize_16sc32sc_Sfs_Ctx)

-
Device-buffer size (in bytes) for nppsDotProd_16sc32sc_Sfs_Ctx.

- Parameters
-
**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**hpBufferSize**– Required buffer size. Important: hpBufferSize is a*host pointer.***nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
NPP_SUCCESS



-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsDotProd_16sc32sc_Sfs_Ctx(const[Npp16sc](https://docs.nvidia.com/nppdefs.html#c.Npp16sc)*pSrc1, const[Npp16sc](https://docs.nvidia.com/nppdefs.html#c.Npp16sc)*pSrc2, size_t nLength,[Npp32sc](https://docs.nvidia.com/nppdefs.html#c.Npp32sc)*pDp, int nScaleFactor,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDeviceBuffer,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsDotProd_16sc32sc_Sfs_Ctx)

-
16-bit signed short integer complex dot product method, return value is 32-bit signed integer complex.

- Parameters
-
**pSrc1**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pSrc2**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**pDp**– Device memory pointer to the dot product result.**nScaleFactor**–[Integer Result Scaling](https://docs.nvidia.com/introduction.html#general_conventions_lb_1integer_result_scaling).**pDeviceBuffer**– Pointer to the required device memory allocation,[Scratch Buffer and Host Pointer](https://docs.nvidia.com/introduction.html#general_conventions_lb_1general_scratch_buffer). Use[nppsDotProdGetBufferSize_16sc32sc_Sfs_Ctx](https://docs.nvidia.com#group__signal__dot__product_1gac1e25bc5a935cceb06d88c532141b1c4)to determine the minimum number of bytes required.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsDotProdGetBufferSize_32s32sc_Sfs_Ctx(size_t nLength, size_t *hpBufferSize,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsDotProdGetBufferSize_32s32sc_Sfs_Ctx)

-
Device-buffer size (in bytes) for nppsDotProd_32s32sc_Sfs_Ctx.

- Parameters
-
**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**hpBufferSize**– Required buffer size. Important: hpBufferSize is a*host pointer.***nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
NPP_SUCCESS



-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsDotProd_32s32sc_Sfs_Ctx(const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pSrc1, const[Npp32sc](https://docs.nvidia.com/nppdefs.html#c.Npp32sc)*pSrc2, size_t nLength,[Npp32sc](https://docs.nvidia.com/nppdefs.html#c.Npp32sc)*pDp, int nScaleFactor,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDeviceBuffer,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsDotProd_32s32sc_Sfs_Ctx)

-
32-bit signed short integer and 32-bit signed short integer complex dot product method, return value is 32-bit signed integer complex.

- Parameters
-
**pSrc1**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pSrc2**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**pDp**– Device memory pointer to the dot product result.**nScaleFactor**–[Integer Result Scaling](https://docs.nvidia.com/introduction.html#general_conventions_lb_1integer_result_scaling).**pDeviceBuffer**– Pointer to the required device memory allocation,[Scratch Buffer and Host Pointer](https://docs.nvidia.com/introduction.html#general_conventions_lb_1general_scratch_buffer). Use[nppsDotProdGetBufferSize_32s32sc_Sfs_Ctx](https://docs.nvidia.com#group__signal__dot__product_1gad4682e6e37b576a977b705c4e0d0f00d)to determine the minimum number of bytes required.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


## Signal Count In Range[](https://docs.nvidia.com#signal-count-in-range)

### Count In Range[](https://docs.nvidia.com#group__signal__count__in__range_1signal_count_in_range)

Calculates the number of elements from specified range in the samples of a signal.

Functions

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsCountInRangeGetBufferSize_32s_Ctx(size_t nLength, size_t *hpBufferSize,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsCountInRangeGetBufferSize_32s_Ctx)

-
Device-buffer size (in bytes) for nppsCountInRange_32s.

- Parameters
-
**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**hpBufferSize**– Required buffer size. Important: hpBufferSize is a*host pointer.***nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
NPP_SUCCESS



-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsCountInRange_32s_Ctx(const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pSrc, size_t nLength, int *pCounts,[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)nLowerBound,[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)nUpperBound,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDeviceBuffer,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsCountInRange_32s_Ctx)

-
Computes the number of elements whose values fall into the specified range on a 32-bit signed integer array.

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**pCounts**– Device memory pointer to the number of elements.**nLowerBound**– Lower bound of the specified range.**nUpperBound**– Upper bound of the specified range.**pDeviceBuffer**– Pointer to the required device memory allocation,[Scratch Buffer and Host Pointer](https://docs.nvidia.com/introduction.html#general_conventions_lb_1general_scratch_buffer). Use[nppsCountInRangeGetBufferSize_32s_Ctx](https://docs.nvidia.com#group__signal__count__in__range_1ga4e9863b3ebeb4db1114db9f612ded8b1)to determine the minimum number of bytes required.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


## Signal Count Zero Crossings[](https://docs.nvidia.com#signal-count-zero-crossings)

### Count Zero Crossings[](https://docs.nvidia.com#group__signal__count__zero__crossings_1signal_count_zero_crossings)

Calculates the number of zero crossings in a signal.

Functions

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsZeroCrossingGetBufferSize_16s32f_Ctx(size_t nLength, size_t *hpBufferSize,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsZeroCrossingGetBufferSize_16s32f_Ctx)

-
Device-buffer size (in bytes) for nppsZeroCrossing_16s32f_Ctx.

- Parameters
-
**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**hpBufferSize**– Required buffer size. Important: hpBufferSize is a*host pointer.***nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
NPP_SUCCESS



-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsZeroCrossing_16s32f_Ctx(const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrc, size_t nLength,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pValZC,[NppsZCType](https://docs.nvidia.com/nppdefs.html#c.NppsZCType)tZCType,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDeviceBuffer,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsZeroCrossing_16s32f_Ctx)

-
16-bit signed short integer zero crossing method, return value is 32-bit floating point.

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**pValZC**– Device memory pointer to the output result.**tZCType**– Type of the zero crossing measure: nppZCR, nppZCXor or nppZCC.**pDeviceBuffer**– Pointer to the required device memory allocation,[Scratch Buffer and Host Pointer](https://docs.nvidia.com/introduction.html#general_conventions_lb_1general_scratch_buffer). Use[nppsZeroCrossingGetBufferSize_16s32f_Ctx](https://docs.nvidia.com#group__signal__count__zero__crossings_1ga572d124c9f6120ac6f456824044d28e3)to determine the minimum number of bytes required.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsZeroCrossingGetBufferSize_32f_Ctx(size_t nLength, size_t *hpBufferSize,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsZeroCrossingGetBufferSize_32f_Ctx)

-
Device-buffer size (in bytes) for nppsZeroCrossing_32f_Ctx.

- Parameters
-
**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**hpBufferSize**– Required buffer size. Important: hpBufferSize is a*host pointer.***nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
NPP_SUCCESS



-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsZeroCrossing_32f_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc, size_t nLength,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pValZC,[NppsZCType](https://docs.nvidia.com/nppdefs.html#c.NppsZCType)tZCType,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDeviceBuffer,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsZeroCrossing_32f_Ctx)

-
32-bit floating-point zero crossing method, return value is 32-bit floating point.

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**pValZC**– Device memory pointer to the output result.**tZCType**– Type of the zero crossing measure: nppZCR, nppZCXor or nppZCC.**pDeviceBuffer**– Pointer to the required device memory allocation,[Scratch Buffer and Host Pointer](https://docs.nvidia.com/introduction.html#general_conventions_lb_1general_scratch_buffer). Use[nppsZeroCrossingGetBufferSize_32f_Ctx](https://docs.nvidia.com#group__signal__count__zero__crossings_1gada56bba7a871f1fb75c459b42311ae33)to determine the minimum number of bytes required.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


## Signal Maximum Error[](https://docs.nvidia.com#signal-maximum-error)

### MaximumError[](https://docs.nvidia.com#group__signal__maximum__error_1signal_maximum_error)

Primitives for computing the maximum error between two signals. Given two signals \(pSrc1\) and \(pSrc2\) both with length \(N\), the maximum error is defined as the largest absolute difference between the corresponding elements of two signals.

If the signal is in complex format, the absolute value of the complex number is used.

Functions

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsMaximumError_8u_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc1, const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc2, size_t nLength,[Npp64f](https://docs.nvidia.com/nppdefs.html#c.Npp64f)*pDst,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDeviceBuffer,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsMaximumError_8u_Ctx)

-
8-bit unsigned char maximum method.

- Parameters
-
**pSrc1**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pSrc2**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**pDst**– Device memory pointer to the error result.**pDeviceBuffer**– Pointer to the required device memory allocation,[Scratch Buffer and Host Pointer](https://docs.nvidia.com/introduction.html#general_conventions_lb_1general_scratch_buffer). Use[nppsMaximumErrorGetBufferSize_8u_Ctx](https://docs.nvidia.com#group__signal__maximum__error_1ga42c8d5b010ca6611278d5ce4cfde5911)to determine the minimum number of bytes required.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsMaximumError_8s_Ctx(const[Npp8s](https://docs.nvidia.com/nppdefs.html#c.Npp8s)*pSrc1, const[Npp8s](https://docs.nvidia.com/nppdefs.html#c.Npp8s)*pSrc2, size_t nLength,[Npp64f](https://docs.nvidia.com/nppdefs.html#c.Npp64f)*pDst,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDeviceBuffer,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsMaximumError_8s_Ctx)

-
8-bit signed char maximum method.

- Parameters
-
**pSrc1**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pSrc2**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**pDst**– Device memory pointer to the error result.**pDeviceBuffer**– Pointer to the required device memory allocation,[Scratch Buffer and Host Pointer](https://docs.nvidia.com/introduction.html#general_conventions_lb_1general_scratch_buffer). Use[nppsMaximumErrorGetBufferSize_8s_Ctx](https://docs.nvidia.com#group__signal__maximum__error_1gaad1cdae5e3348611feff0dd49355a928)to determine the minimum number of bytes required.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsMaximumError_16u_Ctx(const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrc1, const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrc2, size_t nLength,[Npp64f](https://docs.nvidia.com/nppdefs.html#c.Npp64f)*pDst,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDeviceBuffer,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsMaximumError_16u_Ctx)

-
16-bit unsigned short integer maximum method.

- Parameters
-
**pSrc1**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pSrc2**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**pDst**– Device memory pointer to the error result.**pDeviceBuffer**– Pointer to the required device memory allocation,[Scratch Buffer and Host Pointer](https://docs.nvidia.com/introduction.html#general_conventions_lb_1general_scratch_buffer). Use[nppsMaximumErrorGetBufferSize_16u_Ctx](https://docs.nvidia.com#group__signal__maximum__error_1ga62ee51edd45b51f6e08baadfdf54ca87)to determine the minimum number of bytes required.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsMaximumError_16s_Ctx(const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrc1, const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrc2, size_t nLength,[Npp64f](https://docs.nvidia.com/nppdefs.html#c.Npp64f)*pDst,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDeviceBuffer,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsMaximumError_16s_Ctx)

-
16-bit signed short integer maximum method.

- Parameters
-
**pSrc1**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pSrc2**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**pDst**– Device memory pointer to the error result.**pDeviceBuffer**– Pointer to the required device memory allocation,[Scratch Buffer and Host Pointer](https://docs.nvidia.com/introduction.html#general_conventions_lb_1general_scratch_buffer). Use[nppsMaximumErrorGetBufferSize_16s_Ctx](https://docs.nvidia.com#group__signal__maximum__error_1gaeedf17a4a9bc8f1c9619faecfbccc470)to determine the minimum number of bytes required.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsMaximumError_16sc_Ctx(const[Npp16sc](https://docs.nvidia.com/nppdefs.html#c.Npp16sc)*pSrc1, const[Npp16sc](https://docs.nvidia.com/nppdefs.html#c.Npp16sc)*pSrc2, size_t nLength,[Npp64f](https://docs.nvidia.com/nppdefs.html#c.Npp64f)*pDst,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDeviceBuffer,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsMaximumError_16sc_Ctx)

-
16-bit unsigned short complex integer maximum method.

- Parameters
-
**pSrc1**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pSrc2**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**pDst**– Device memory pointer to the error result.**pDeviceBuffer**– Pointer to the required device memory allocation,[Scratch Buffer and Host Pointer](https://docs.nvidia.com/introduction.html#general_conventions_lb_1general_scratch_buffer). Use[nppsMaximumErrorGetBufferSize_16sc_Ctx](https://docs.nvidia.com#group__signal__maximum__error_1ga0814f3a7be21a423a565e1bb36fafeca)to determine the minimum number of bytes required.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsMaximumError_32u_Ctx(const[Npp32u](https://docs.nvidia.com/nppdefs.html#c.Npp32u)*pSrc1, const[Npp32u](https://docs.nvidia.com/nppdefs.html#c.Npp32u)*pSrc2, size_t nLength,[Npp64f](https://docs.nvidia.com/nppdefs.html#c.Npp64f)*pDst,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDeviceBuffer,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsMaximumError_32u_Ctx)

-
32-bit unsigned short integer maximum method.

- Parameters
-
**pSrc1**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pSrc2**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**pDst**– Device memory pointer to the error result.**pDeviceBuffer**– Pointer to the required device memory allocation,[Scratch Buffer and Host Pointer](https://docs.nvidia.com/introduction.html#general_conventions_lb_1general_scratch_buffer). Use[nppsMaximumErrorGetBufferSize_32u_Ctx](https://docs.nvidia.com#group__signal__maximum__error_1gad0552a7b91e7bbc07c804c0e6affe1b9)to determine the minimum number of bytes required.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsMaximumError_32s_Ctx(const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pSrc1, const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pSrc2, size_t nLength,[Npp64f](https://docs.nvidia.com/nppdefs.html#c.Npp64f)*pDst,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDeviceBuffer,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsMaximumError_32s_Ctx)

-
32-bit signed short integer maximum method.

- Parameters
-
**pSrc1**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pSrc2**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**pDst**– Device memory pointer to the error result.**pDeviceBuffer**– Pointer to the required device memory allocation,[Scratch Buffer and Host Pointer](https://docs.nvidia.com/introduction.html#general_conventions_lb_1general_scratch_buffer). Use[nppsMaximumErrorGetBufferSize_32s_Ctx](https://docs.nvidia.com#group__signal__maximum__error_1gaedf3e3efbac94cb36d1600ea3d98f393)to determine the minimum number of bytes required.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsMaximumError_32sc_Ctx(const[Npp32sc](https://docs.nvidia.com/nppdefs.html#c.Npp32sc)*pSrc1, const[Npp32sc](https://docs.nvidia.com/nppdefs.html#c.Npp32sc)*pSrc2, size_t nLength,[Npp64f](https://docs.nvidia.com/nppdefs.html#c.Npp64f)*pDst,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDeviceBuffer,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsMaximumError_32sc_Ctx)

-
32-bit unsigned short complex integer maximum method.

- Parameters
-
**pSrc1**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pSrc2**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**pDst**– Device memory pointer to the error result.**pDeviceBuffer**– Pointer to the required device memory allocation,[Scratch Buffer and Host Pointer](https://docs.nvidia.com/introduction.html#general_conventions_lb_1general_scratch_buffer). Use[nppsMaximumErrorGetBufferSize_32sc_Ctx](https://docs.nvidia.com#group__signal__maximum__error_1gab2c20f8c080e33f4a708a2ace86f2be1)to determine the minimum number of bytes required.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsMaximumError_64s_Ctx(const[Npp64s](https://docs.nvidia.com/nppdefs.html#c.Npp64s)*pSrc1, const[Npp64s](https://docs.nvidia.com/nppdefs.html#c.Npp64s)*pSrc2, size_t nLength,[Npp64f](https://docs.nvidia.com/nppdefs.html#c.Npp64f)*pDst,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDeviceBuffer,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsMaximumError_64s_Ctx)

-
64-bit signed short integer maximum method.

- Parameters
-
**pSrc1**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pSrc2**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**pDst**– Device memory pointer to the error result.**pDeviceBuffer**– Pointer to the required device memory allocation,[Scratch Buffer and Host Pointer](https://docs.nvidia.com/introduction.html#general_conventions_lb_1general_scratch_buffer). Use[nppsMaximumErrorGetBufferSize_64s_Ctx](https://docs.nvidia.com#group__signal__maximum__error_1gab6a1053d63fec9a213d7ced3ca9f566f)to determine the minimum number of bytes required.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsMaximumError_64sc_Ctx(const[Npp64sc](https://docs.nvidia.com/nppdefs.html#c.Npp64sc)*pSrc1, const[Npp64sc](https://docs.nvidia.com/nppdefs.html#c.Npp64sc)*pSrc2, size_t nLength,[Npp64f](https://docs.nvidia.com/nppdefs.html#c.Npp64f)*pDst,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDeviceBuffer,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsMaximumError_64sc_Ctx)

-
64-bit unsigned short complex integer maximum method.

- Parameters
-
**pSrc1**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pSrc2**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**pDst**– Device memory pointer to the error result.**pDeviceBuffer**– Pointer to the required device memory allocation,[Scratch Buffer and Host Pointer](https://docs.nvidia.com/introduction.html#general_conventions_lb_1general_scratch_buffer). Use[nppsMaximumErrorGetBufferSize_64sc_Ctx](https://docs.nvidia.com#group__signal__maximum__error_1ga945ef8956828548fa5eaf66f0f28c9bd)to determine the minimum number of bytes required.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsMaximumError_32f_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc1, const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc2, size_t nLength,[Npp64f](https://docs.nvidia.com/nppdefs.html#c.Npp64f)*pDst,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDeviceBuffer,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsMaximumError_32f_Ctx)

-
32-bit floating point maximum method.

- Parameters
-
**pSrc1**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pSrc2**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**pDst**– Device memory pointer to the error result.**pDeviceBuffer**– Pointer to the required device memory allocation,[Scratch Buffer and Host Pointer](https://docs.nvidia.com/introduction.html#general_conventions_lb_1general_scratch_buffer). Use[nppsMaximumErrorGetBufferSize_32f_Ctx](https://docs.nvidia.com#group__signal__maximum__error_1gac0460d4a73a1c09b874555733c269222)to determine the minimum number of bytes required.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsMaximumError_32fc_Ctx(const[Npp32fc](https://docs.nvidia.com/nppdefs.html#c.Npp32fc)*pSrc1, const[Npp32fc](https://docs.nvidia.com/nppdefs.html#c.Npp32fc)*pSrc2, size_t nLength,[Npp64f](https://docs.nvidia.com/nppdefs.html#c.Npp64f)*pDst,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDeviceBuffer,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsMaximumError_32fc_Ctx)

-
32-bit floating point complex maximum method.

- Parameters
-
**pSrc1**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pSrc2**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**pDst**– Device memory pointer to the error result.**pDeviceBuffer**– Pointer to the required device memory allocation,[Scratch Buffer and Host Pointer](https://docs.nvidia.com/introduction.html#general_conventions_lb_1general_scratch_buffer). Use[nppsMaximumErrorGetBufferSize_32fc_Ctx](https://docs.nvidia.com#group__signal__maximum__error_1gaab84113d9b4019e62c92e5465cea434b)to determine the minimum number of bytes required.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsMaximumError_64f_Ctx(const[Npp64f](https://docs.nvidia.com/nppdefs.html#c.Npp64f)*pSrc1, const[Npp64f](https://docs.nvidia.com/nppdefs.html#c.Npp64f)*pSrc2, size_t nLength,[Npp64f](https://docs.nvidia.com/nppdefs.html#c.Npp64f)*pDst,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDeviceBuffer,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsMaximumError_64f_Ctx)

-
64-bit floating point maximum method.

- Parameters
-
**pSrc1**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pSrc2**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**pDst**– Device memory pointer to the error result.**pDeviceBuffer**– Pointer to the required device memory allocation,[Scratch Buffer and Host Pointer](https://docs.nvidia.com/introduction.html#general_conventions_lb_1general_scratch_buffer). Use[nppsMaximumErrorGetBufferSize_64f_Ctx](https://docs.nvidia.com#group__signal__maximum__error_1ga21d75ab3dc66a124272f911432a5de4e)to determine the minimum number of bytes required.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsMaximumError_64fc_Ctx(const[Npp64fc](https://docs.nvidia.com/nppdefs.html#c.Npp64fc)*pSrc1, const[Npp64fc](https://docs.nvidia.com/nppdefs.html#c.Npp64fc)*pSrc2, size_t nLength,[Npp64f](https://docs.nvidia.com/nppdefs.html#c.Npp64f)*pDst,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDeviceBuffer,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsMaximumError_64fc_Ctx)

-
64-bit floating point complex maximum method.

- Parameters
-
**pSrc1**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pSrc2**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**pDst**– Device memory pointer to the error result.**pDeviceBuffer**– Pointer to the required device memory allocation,[Scratch Buffer and Host Pointer](https://docs.nvidia.com/introduction.html#general_conventions_lb_1general_scratch_buffer). Use[nppsMaximumErrorGetBufferSize_64fc_Ctx](https://docs.nvidia.com#group__signal__maximum__error_1gab74ab22b96ee855ad1ddd4dfe692b44f)to determine the minimum number of bytes required.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsMaximumErrorGetBufferSize_8u_Ctx(size_t nLength, size_t *hpBufferSize,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsMaximumErrorGetBufferSize_8u_Ctx)

-
Device-buffer size (in bytes) for nppsMaximumError_8u.

- Parameters
-
**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**hpBufferSize**– Required buffer size. Important: hpBufferSize is a*host pointer.***nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
NPP_SUCCESS



-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsMaximumErrorGetBufferSize_8s_Ctx(size_t nLength, size_t *hpBufferSize,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsMaximumErrorGetBufferSize_8s_Ctx)

-
Device-buffer size (in bytes) for nppsMaximumError_8s.

- Parameters
-
**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**hpBufferSize**– Required buffer size. Important: hpBufferSize is a*host pointer.***nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
NPP_SUCCESS



-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsMaximumErrorGetBufferSize_16u_Ctx(size_t nLength, size_t *hpBufferSize,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsMaximumErrorGetBufferSize_16u_Ctx)

-
Device-buffer size (in bytes) for nppsMaximumError_16u.

- Parameters
-
**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**hpBufferSize**– Required buffer size. Important: hpBufferSize is a*host pointer.***nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
NPP_SUCCESS



-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsMaximumErrorGetBufferSize_16s_Ctx(size_t nLength, size_t *hpBufferSize,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsMaximumErrorGetBufferSize_16s_Ctx)

-
Device-buffer size (in bytes) for nppsMaximumError_16s.

- Parameters
-
**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**hpBufferSize**– Required buffer size. Important: hpBufferSize is a*host pointer.***nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
NPP_SUCCESS



-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsMaximumErrorGetBufferSize_16sc_Ctx(size_t nLength, size_t *hpBufferSize,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsMaximumErrorGetBufferSize_16sc_Ctx)

-
Device-buffer size (in bytes) for nppsMaximumError_16sc.

- Parameters
-
**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**hpBufferSize**– Required buffer size. Important: hpBufferSize is a*host pointer.***nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
NPP_SUCCESS



-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsMaximumErrorGetBufferSize_32u_Ctx(size_t nLength, size_t *hpBufferSize,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsMaximumErrorGetBufferSize_32u_Ctx)

-
Device-buffer size (in bytes) for nppsMaximumError_32u.

- Parameters
-
**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**hpBufferSize**– Required buffer size. Important: hpBufferSize is a*host pointer.***nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
NPP_SUCCESS



-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsMaximumErrorGetBufferSize_32s_Ctx(size_t nLength, size_t *hpBufferSize,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsMaximumErrorGetBufferSize_32s_Ctx)

-
Device-buffer size (in bytes) for nppsMaximumError_32s.

- Parameters
-
**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**hpBufferSize**– Required buffer size. Important: hpBufferSize is a*host pointer.***nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
NPP_SUCCESS



-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsMaximumErrorGetBufferSize_32sc_Ctx(size_t nLength, size_t *hpBufferSize,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsMaximumErrorGetBufferSize_32sc_Ctx)

-
Device-buffer size (in bytes) for nppsMaximumError_32sc.

- Parameters
-
**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**hpBufferSize**– Required buffer size. Important: hpBufferSize is a*host pointer.***nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
NPP_SUCCESS



-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsMaximumErrorGetBufferSize_64s_Ctx(size_t nLength, size_t *hpBufferSize,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsMaximumErrorGetBufferSize_64s_Ctx)

-
Device-buffer size (in bytes) for nppsMaximumError_64s.

- Parameters
-
**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**hpBufferSize**– Required buffer size. Important: hpBufferSize is a*host pointer.***nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
NPP_SUCCESS



-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsMaximumErrorGetBufferSize_64sc_Ctx(size_t nLength, size_t *hpBufferSize,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsMaximumErrorGetBufferSize_64sc_Ctx)

-
Device-buffer size (in bytes) for nppsMaximumError_64sc.

- Parameters
-
**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**hpBufferSize**– Required buffer size. Important: hpBufferSize is a*host pointer.***nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
NPP_SUCCESS



-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsMaximumErrorGetBufferSize_32f_Ctx(size_t nLength, size_t *hpBufferSize,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsMaximumErrorGetBufferSize_32f_Ctx)

-
Device-buffer size (in bytes) for nppsMaximumError_32f.

- Parameters
-
**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**hpBufferSize**– Required buffer size. Important: hpBufferSize is a*host pointer.***nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
NPP_SUCCESS



-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsMaximumErrorGetBufferSize_32fc_Ctx(size_t nLength, size_t *hpBufferSize,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsMaximumErrorGetBufferSize_32fc_Ctx)

-
Device-buffer size (in bytes) for nppsMaximumError_32fc.

- Parameters
-
**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**hpBufferSize**– Required buffer size. Important: hpBufferSize is a*host pointer.***nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
NPP_SUCCESS



-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsMaximumErrorGetBufferSize_64f_Ctx(size_t nLength, size_t *hpBufferSize,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsMaximumErrorGetBufferSize_64f_Ctx)

-
Device-buffer size (in bytes) for nppsMaximumError_64f.

- Parameters
-
**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**hpBufferSize**– Required buffer size. Important: hpBufferSize is a*host pointer.***nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
NPP_SUCCESS



-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsMaximumErrorGetBufferSize_64fc_Ctx(size_t nLength, size_t *hpBufferSize,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsMaximumErrorGetBufferSize_64fc_Ctx)

-
Device-buffer size (in bytes) for nppsMaximumError_64fc.

- Parameters
-
**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**hpBufferSize**– Required buffer size. Important: hpBufferSize is a*host pointer.***nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
NPP_SUCCESS



## Signal Average Error[](https://docs.nvidia.com#signal-average-error)

### AverageError[](https://docs.nvidia.com#group__signal__average__error_1signal_average_error)

Primitives for computing the Average error between two signals. Given two signals \(pSrc1\) and \(pSrc2\) both with length \(N\), the average error is defined as

If the signal is in complex format, the absolute value of the complex number is used.

Functions

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsAverageError_8u_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc1, const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc2, size_t nLength,[Npp64f](https://docs.nvidia.com/nppdefs.html#c.Npp64f)*pDst,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDeviceBuffer,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsAverageError_8u_Ctx)

-
8-bit unsigned char Average method.

- Parameters
-
**pSrc1**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pSrc2**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**pDst**– Device memory pointer to the error result.**pDeviceBuffer**– Pointer to the required device memory allocation,[Scratch Buffer and Host Pointer](https://docs.nvidia.com/introduction.html#general_conventions_lb_1general_scratch_buffer). Use[nppsAverageErrorGetBufferSize_8u_Ctx](https://docs.nvidia.com#group__signal__average__error_1ga3c4edb98784be6426a78446e6420c9a1)to determine the minimum number of bytes required.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsAverageError_8s_Ctx(const[Npp8s](https://docs.nvidia.com/nppdefs.html#c.Npp8s)*pSrc1, const[Npp8s](https://docs.nvidia.com/nppdefs.html#c.Npp8s)*pSrc2, size_t nLength,[Npp64f](https://docs.nvidia.com/nppdefs.html#c.Npp64f)*pDst,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDeviceBuffer,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsAverageError_8s_Ctx)

-
8-bit signed char Average method.

- Parameters
-
**pSrc1**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pSrc2**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**pDst**– Device memory pointer to the error result.**pDeviceBuffer**– Pointer to the required device memory allocation,[Scratch Buffer and Host Pointer](https://docs.nvidia.com/introduction.html#general_conventions_lb_1general_scratch_buffer). Use[nppsAverageErrorGetBufferSize_8s_Ctx](https://docs.nvidia.com#group__signal__average__error_1ga34f3025ae3600ab87bdc73e1aea81548)to determine the minimum number of bytes required.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsAverageError_16u_Ctx(const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrc1, const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrc2, size_t nLength,[Npp64f](https://docs.nvidia.com/nppdefs.html#c.Npp64f)*pDst,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDeviceBuffer,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsAverageError_16u_Ctx)

-
16-bit unsigned short integer Average method.

- Parameters
-
**pSrc1**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pSrc2**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**pDst**– Device memory pointer to the error result.**pDeviceBuffer**– Pointer to the required device memory allocation,[Scratch Buffer and Host Pointer](https://docs.nvidia.com/introduction.html#general_conventions_lb_1general_scratch_buffer). Use[nppsAverageErrorGetBufferSize_16u_Ctx](https://docs.nvidia.com#group__signal__average__error_1gacf8d29201fe8a4cab9ec12dc09146682)to determine the minimum number of bytes required.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsAverageError_16s_Ctx(const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrc1, const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrc2, size_t nLength,[Npp64f](https://docs.nvidia.com/nppdefs.html#c.Npp64f)*pDst,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDeviceBuffer,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsAverageError_16s_Ctx)

-
16-bit signed short integer Average method.

- Parameters
-
**pSrc1**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pSrc2**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**pDst**– Device memory pointer to the error result.**pDeviceBuffer**– Pointer to the required device memory allocation,[Scratch Buffer and Host Pointer](https://docs.nvidia.com/introduction.html#general_conventions_lb_1general_scratch_buffer). Use[nppsAverageErrorGetBufferSize_16s_Ctx](https://docs.nvidia.com#group__signal__average__error_1gaddb85f52ea1de3b8c481cb5fce177c54)to determine the minimum number of bytes required.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsAverageError_16sc_Ctx(const[Npp16sc](https://docs.nvidia.com/nppdefs.html#c.Npp16sc)*pSrc1, const[Npp16sc](https://docs.nvidia.com/nppdefs.html#c.Npp16sc)*pSrc2, size_t nLength,[Npp64f](https://docs.nvidia.com/nppdefs.html#c.Npp64f)*pDst,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDeviceBuffer,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsAverageError_16sc_Ctx)

-
16-bit unsigned short complex integer Average method.

- Parameters
-
**pSrc1**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pSrc2**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**pDst**– Device memory pointer to the error result.**pDeviceBuffer**– Pointer to the required device memory allocation,[Scratch Buffer and Host Pointer](https://docs.nvidia.com/introduction.html#general_conventions_lb_1general_scratch_buffer). Use[nppsAverageErrorGetBufferSize_16sc_Ctx](https://docs.nvidia.com#group__signal__average__error_1ga8ca3d295c923d72847f01035f71a0c89)to determine the minimum number of bytes required.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsAverageError_32u_Ctx(const[Npp32u](https://docs.nvidia.com/nppdefs.html#c.Npp32u)*pSrc1, const[Npp32u](https://docs.nvidia.com/nppdefs.html#c.Npp32u)*pSrc2, size_t nLength,[Npp64f](https://docs.nvidia.com/nppdefs.html#c.Npp64f)*pDst,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDeviceBuffer,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsAverageError_32u_Ctx)

-
32-bit unsigned short integer Average method.

- Parameters
-
**pSrc1**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pSrc2**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**pDst**– Device memory pointer to the error result.**pDeviceBuffer**– Pointer to the required device memory allocation,[Scratch Buffer and Host Pointer](https://docs.nvidia.com/introduction.html#general_conventions_lb_1general_scratch_buffer). Use[nppsAverageErrorGetBufferSize_32u_Ctx](https://docs.nvidia.com#group__signal__average__error_1gabdb0592f3850feb1b408dd23896df6eb)to determine the minimum number of bytes required.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsAverageError_32s_Ctx(const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pSrc1, const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pSrc2, size_t nLength,[Npp64f](https://docs.nvidia.com/nppdefs.html#c.Npp64f)*pDst,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDeviceBuffer,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsAverageError_32s_Ctx)

-
32-bit signed short integer Average method.

- Parameters
-
**pSrc1**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pSrc2**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**pDst**– Device memory pointer to the error result.**pDeviceBuffer**– Pointer to the required device memory allocation,[Scratch Buffer and Host Pointer](https://docs.nvidia.com/introduction.html#general_conventions_lb_1general_scratch_buffer). Use[nppsAverageErrorGetBufferSize_32s_Ctx](https://docs.nvidia.com#group__signal__average__error_1gacf2388d8c75cf1fa9fad5fdc7c50203d)to determine the minimum number of bytes required.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsAverageError_32sc_Ctx(const[Npp32sc](https://docs.nvidia.com/nppdefs.html#c.Npp32sc)*pSrc1, const[Npp32sc](https://docs.nvidia.com/nppdefs.html#c.Npp32sc)*pSrc2, size_t nLength,[Npp64f](https://docs.nvidia.com/nppdefs.html#c.Npp64f)*pDst,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDeviceBuffer,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsAverageError_32sc_Ctx)

-
32-bit unsigned short complex integer Average method.

- Parameters
-
**pSrc1**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pSrc2**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**pDst**– Device memory pointer to the error result.**pDeviceBuffer**– Pointer to the required device memory allocation,[Scratch Buffer and Host Pointer](https://docs.nvidia.com/introduction.html#general_conventions_lb_1general_scratch_buffer). Use[nppsAverageErrorGetBufferSize_32sc_Ctx](https://docs.nvidia.com#group__signal__average__error_1ga70280b668c31d858953bfdf823fa23c7)to determine the minimum number of bytes required.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsAverageError_64s_Ctx(const[Npp64s](https://docs.nvidia.com/nppdefs.html#c.Npp64s)*pSrc1, const[Npp64s](https://docs.nvidia.com/nppdefs.html#c.Npp64s)*pSrc2, size_t nLength,[Npp64f](https://docs.nvidia.com/nppdefs.html#c.Npp64f)*pDst,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDeviceBuffer,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsAverageError_64s_Ctx)

-
64-bit signed short integer Average method.

- Parameters
-
**pSrc1**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pSrc2**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**pDst**– Device memory pointer to the error result.**pDeviceBuffer**– Pointer to the required device memory allocation,[Scratch Buffer and Host Pointer](https://docs.nvidia.com/introduction.html#general_conventions_lb_1general_scratch_buffer). Use[nppsAverageErrorGetBufferSize_64s_Ctx](https://docs.nvidia.com#group__signal__average__error_1ga53c2a5ae1574f67b4f2599d92fa8692e)to determine the minimum number of bytes required.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsAverageError_64sc_Ctx(const[Npp64sc](https://docs.nvidia.com/nppdefs.html#c.Npp64sc)*pSrc1, const[Npp64sc](https://docs.nvidia.com/nppdefs.html#c.Npp64sc)*pSrc2, size_t nLength,[Npp64f](https://docs.nvidia.com/nppdefs.html#c.Npp64f)*pDst,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDeviceBuffer,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsAverageError_64sc_Ctx)

-
64-bit unsigned short complex integer Average method.

- Parameters
-
**pSrc1**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pSrc2**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**pDst**– Device memory pointer to the error result.**pDeviceBuffer**– Pointer to the required device memory allocation,[Scratch Buffer and Host Pointer](https://docs.nvidia.com/introduction.html#general_conventions_lb_1general_scratch_buffer). Use[nppsAverageErrorGetBufferSize_64sc_Ctx](https://docs.nvidia.com#group__signal__average__error_1ga6ede9e2449efa52237a62beafa03fb6c)to determine the minimum number of bytes required.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsAverageError_32f_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc1, const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc2, size_t nLength,[Npp64f](https://docs.nvidia.com/nppdefs.html#c.Npp64f)*pDst,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDeviceBuffer,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsAverageError_32f_Ctx)

-
32-bit floating point Average method.

- Parameters
-
**pSrc1**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pSrc2**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**pDst**– Device memory pointer to the error result.**pDeviceBuffer**– Pointer to the required device memory allocation,[Scratch Buffer and Host Pointer](https://docs.nvidia.com/introduction.html#general_conventions_lb_1general_scratch_buffer). Use[nppsAverageErrorGetBufferSize_32f_Ctx](https://docs.nvidia.com#group__signal__average__error_1ga03aab42f424f3a7740a909eedb712791)to determine the minimum number of bytes required.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsAverageError_32fc_Ctx(const[Npp32fc](https://docs.nvidia.com/nppdefs.html#c.Npp32fc)*pSrc1, const[Npp32fc](https://docs.nvidia.com/nppdefs.html#c.Npp32fc)*pSrc2, size_t nLength,[Npp64f](https://docs.nvidia.com/nppdefs.html#c.Npp64f)*pDst,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDeviceBuffer,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsAverageError_32fc_Ctx)

-
32-bit floating point complex Average method.

- Parameters
-
**pSrc1**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pSrc2**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**pDst**– Device memory pointer to the error result.**pDeviceBuffer**– Pointer to the required device memory allocation,[Scratch Buffer and Host Pointer](https://docs.nvidia.com/introduction.html#general_conventions_lb_1general_scratch_buffer). Use[nppsAverageErrorGetBufferSize_32fc_Ctx](https://docs.nvidia.com#group__signal__average__error_1gae315988537cafaf348174e251727b597)to determine the minimum number of bytes required.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsAverageError_64f_Ctx(const[Npp64f](https://docs.nvidia.com/nppdefs.html#c.Npp64f)*pSrc1, const[Npp64f](https://docs.nvidia.com/nppdefs.html#c.Npp64f)*pSrc2, size_t nLength,[Npp64f](https://docs.nvidia.com/nppdefs.html#c.Npp64f)*pDst,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDeviceBuffer,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsAverageError_64f_Ctx)

-
64-bit floating point Average method.

- Parameters
-
**pSrc1**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pSrc2**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**pDst**– Device memory pointer to the error result.**pDeviceBuffer**– Pointer to the required device memory allocation,[Scratch Buffer and Host Pointer](https://docs.nvidia.com/introduction.html#general_conventions_lb_1general_scratch_buffer). Use[nppsAverageErrorGetBufferSize_64f_Ctx](https://docs.nvidia.com#group__signal__average__error_1gacbfac41b70b80969bc109c611eb22fd2)to determine the minimum number of bytes required.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsAverageError_64fc_Ctx(const[Npp64fc](https://docs.nvidia.com/nppdefs.html#c.Npp64fc)*pSrc1, const[Npp64fc](https://docs.nvidia.com/nppdefs.html#c.Npp64fc)*pSrc2, size_t nLength,[Npp64f](https://docs.nvidia.com/nppdefs.html#c.Npp64f)*pDst,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDeviceBuffer,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsAverageError_64fc_Ctx)

-
64-bit floating point complex Average method.

- Parameters
-
**pSrc1**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pSrc2**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**pDst**– Device memory pointer to the error result.**pDeviceBuffer**– Pointer to the required device memory allocation,[Scratch Buffer and Host Pointer](https://docs.nvidia.com/introduction.html#general_conventions_lb_1general_scratch_buffer). Use[nppsAverageErrorGetBufferSize_64fc_Ctx](https://docs.nvidia.com#group__signal__average__error_1gadebdc878dadf8c1a52fc85691567d936)to determine the minimum number of bytes required.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsAverageErrorGetBufferSize_8u_Ctx(size_t nLength, size_t *hpBufferSize,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsAverageErrorGetBufferSize_8u_Ctx)

-
Device-buffer size (in bytes) for nppsAverageError_8u.

- Parameters
-
**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**hpBufferSize**– Required buffer size. Important: hpBufferSize is a*host pointer.***nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
NPP_SUCCESS



-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsAverageErrorGetBufferSize_8s_Ctx(size_t nLength, size_t *hpBufferSize,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsAverageErrorGetBufferSize_8s_Ctx)

-
Device-buffer size (in bytes) for nppsAverageError_8s.

- Parameters
-
**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**hpBufferSize**– Required buffer size. Important: hpBufferSize is a*host pointer.***nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
NPP_SUCCESS



-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsAverageErrorGetBufferSize_16u_Ctx(size_t nLength, size_t *hpBufferSize,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsAverageErrorGetBufferSize_16u_Ctx)

-
Device-buffer size (in bytes) for nppsAverageError_16u.

- Parameters
-
**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**hpBufferSize**– Required buffer size. Important: hpBufferSize is a*host pointer.***nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
NPP_SUCCESS



-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsAverageErrorGetBufferSize_16s_Ctx(size_t nLength, size_t *hpBufferSize,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsAverageErrorGetBufferSize_16s_Ctx)

-
Device-buffer size (in bytes) for nppsAverageError_16s.

- Parameters
-
**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**hpBufferSize**– Required buffer size. Important: hpBufferSize is a*host pointer.***nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
NPP_SUCCESS



-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsAverageErrorGetBufferSize_16sc_Ctx(size_t nLength, size_t *hpBufferSize,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsAverageErrorGetBufferSize_16sc_Ctx)

-
Device-buffer size (in bytes) for nppsAverageError_16sc.

- Parameters
-
**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**hpBufferSize**– Required buffer size. Important: hpBufferSize is a*host pointer.***nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
NPP_SUCCESS



-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsAverageErrorGetBufferSize_32u_Ctx(size_t nLength, size_t *hpBufferSize,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsAverageErrorGetBufferSize_32u_Ctx)

-
Device-buffer size (in bytes) for nppsAverageError_32u.

- Parameters
-
**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**hpBufferSize**– Required buffer size. Important: hpBufferSize is a*host pointer.***nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
NPP_SUCCESS



-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsAverageErrorGetBufferSize_32s_Ctx(size_t nLength, size_t *hpBufferSize,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsAverageErrorGetBufferSize_32s_Ctx)

-
Device-buffer size (in bytes) for nppsAverageError_32s.

- Parameters
-
**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**hpBufferSize**– Required buffer size. Important: hpBufferSize is a*host pointer.***nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
NPP_SUCCESS



-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsAverageErrorGetBufferSize_32sc_Ctx(size_t nLength, size_t *hpBufferSize,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsAverageErrorGetBufferSize_32sc_Ctx)

-
Device-buffer size (in bytes) for nppsAverageError_32sc.

- Parameters
-
**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**hpBufferSize**– Required buffer size. Important: hpBufferSize is a*host pointer.***nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
NPP_SUCCESS



-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsAverageErrorGetBufferSize_64s_Ctx(size_t nLength, size_t *hpBufferSize,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsAverageErrorGetBufferSize_64s_Ctx)

-
Device-buffer size (in bytes) for nppsAverageError_64s.

- Parameters
-
**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**hpBufferSize**– Required buffer size. Important: hpBufferSize is a*host pointer.***nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
NPP_SUCCESS



-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsAverageErrorGetBufferSize_64sc_Ctx(size_t nLength, size_t *hpBufferSize,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsAverageErrorGetBufferSize_64sc_Ctx)

-
Device-buffer size (in bytes) for nppsAverageError_64sc.

- Parameters
-
**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**hpBufferSize**– Required buffer size. Important: hpBufferSize is a*host pointer.***nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
NPP_SUCCESS



-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsAverageErrorGetBufferSize_32f_Ctx(size_t nLength, size_t *hpBufferSize,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsAverageErrorGetBufferSize_32f_Ctx)

-
Device-buffer size (in bytes) for nppsAverageError_32f.

- Parameters
-
**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**hpBufferSize**– Required buffer size. Important: hpBufferSize is a*host pointer.***nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
NPP_SUCCESS



-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsAverageErrorGetBufferSize_32fc_Ctx(size_t nLength, size_t *hpBufferSize,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsAverageErrorGetBufferSize_32fc_Ctx)

-
Device-buffer size (in bytes) for nppsAverageError_32fc.

- Parameters
-
**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**hpBufferSize**– Required buffer size. Important: hpBufferSize is a*host pointer.***nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
NPP_SUCCESS



-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsAverageErrorGetBufferSize_64f_Ctx(size_t nLength, size_t *hpBufferSize,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsAverageErrorGetBufferSize_64f_Ctx)

-
Device-buffer size (in bytes) for nppsAverageError_64f.

- Parameters
-
**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**hpBufferSize**– Required buffer size. Important: hpBufferSize is a*host pointer.***nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
NPP_SUCCESS



-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsAverageErrorGetBufferSize_64fc_Ctx(size_t nLength, size_t *hpBufferSize,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsAverageErrorGetBufferSize_64fc_Ctx)

-
Device-buffer size (in bytes) for nppsAverageError_64fc.

- Parameters
-
**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**hpBufferSize**– Required buffer size. Important: hpBufferSize is a*host pointer.***nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
NPP_SUCCESS



## Signal Maximum Relative Error[](https://docs.nvidia.com#signal-maximum-relative-error)

### MaximumRelativeError[](https://docs.nvidia.com#group__signal__maximum__relative__error_1signal_maximum_relative_error)

Primitives for computing the MaximumRelative error between two signals. Given two signals \(pSrc1\) and \(pSrc2\) both with length \(N\), the maximum relative error is defined as

If the signal is in complex format, the absolute value of the complex number is used.

Functions

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsMaximumRelativeError_8u_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc1, const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc2, size_t nLength,[Npp64f](https://docs.nvidia.com/nppdefs.html#c.Npp64f)*pDst,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDeviceBuffer,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsMaximumRelativeError_8u_Ctx)

-
8-bit unsigned char MaximumRelative method.

- Parameters
-
**pSrc1**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pSrc2**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**pDst**– Device memory pointer to the error result.**pDeviceBuffer**– Pointer to the required device memory allocation,[Scratch Buffer and Host Pointer](https://docs.nvidia.com/introduction.html#general_conventions_lb_1general_scratch_buffer). Use[nppsMaximumRelativeErrorGetBufferSize_8u_Ctx](https://docs.nvidia.com#group__signal__maximum__relative__error_1ga4063d563adefd518598379055675bf71)to determine the minimum number of bytes required.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsMaximumRelativeError_8s_Ctx(const[Npp8s](https://docs.nvidia.com/nppdefs.html#c.Npp8s)*pSrc1, const[Npp8s](https://docs.nvidia.com/nppdefs.html#c.Npp8s)*pSrc2, size_t nLength,[Npp64f](https://docs.nvidia.com/nppdefs.html#c.Npp64f)*pDst,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDeviceBuffer,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsMaximumRelativeError_8s_Ctx)

-
8-bit signed char MaximumRelative method.

- Parameters
-
**pSrc1**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pSrc2**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**pDst**– Device memory pointer to the error result.**pDeviceBuffer**– Pointer to the required device memory allocation,[Scratch Buffer and Host Pointer](https://docs.nvidia.com/introduction.html#general_conventions_lb_1general_scratch_buffer). Use[nppsMaximumRelativeErrorGetBufferSize_8s_Ctx](https://docs.nvidia.com#group__signal__maximum__relative__error_1ga13a891b37214fed9012e82564d353d31)to determine the minimum number of bytes required.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsMaximumRelativeError_16u_Ctx(const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrc1, const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrc2, size_t nLength,[Npp64f](https://docs.nvidia.com/nppdefs.html#c.Npp64f)*pDst,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDeviceBuffer,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsMaximumRelativeError_16u_Ctx)

-
16-bit unsigned short integer MaximumRelative method.

- Parameters
-
**pSrc1**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pSrc2**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**pDst**– Device memory pointer to the error result.**pDeviceBuffer**– Pointer to the required device memory allocation,[Scratch Buffer and Host Pointer](https://docs.nvidia.com/introduction.html#general_conventions_lb_1general_scratch_buffer). Use[nppsMaximumRelativeErrorGetBufferSize_16u_Ctx](https://docs.nvidia.com#group__signal__maximum__relative__error_1gaf13bf6b36f1bcb05fc813ca42a93de2c)to determine the minimum number of bytes required.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsMaximumRelativeError_16s_Ctx(const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrc1, const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrc2, size_t nLength,[Npp64f](https://docs.nvidia.com/nppdefs.html#c.Npp64f)*pDst,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDeviceBuffer,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsMaximumRelativeError_16s_Ctx)

-
16-bit signed short integer MaximumRelative method.

- Parameters
-
**pSrc1**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pSrc2**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**pDst**– Device memory pointer to the error result.**pDeviceBuffer**– Pointer to the required device memory allocation,[Scratch Buffer and Host Pointer](https://docs.nvidia.com/introduction.html#general_conventions_lb_1general_scratch_buffer). Use[nppsMaximumRelativeErrorGetBufferSize_16s_Ctx](https://docs.nvidia.com#group__signal__maximum__relative__error_1ga86641fac16df9e917eac677809a02f65)to determine the minimum number of bytes required.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsMaximumRelativeError_16sc_Ctx(const[Npp16sc](https://docs.nvidia.com/nppdefs.html#c.Npp16sc)*pSrc1, const[Npp16sc](https://docs.nvidia.com/nppdefs.html#c.Npp16sc)*pSrc2, size_t nLength,[Npp64f](https://docs.nvidia.com/nppdefs.html#c.Npp64f)*pDst,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDeviceBuffer,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsMaximumRelativeError_16sc_Ctx)

-
16-bit unsigned short complex integer MaximumRelative method.

- Parameters
-
**pSrc1**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pSrc2**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**pDst**– Device memory pointer to the error result.**pDeviceBuffer**– Pointer to the required device memory allocation,[Scratch Buffer and Host Pointer](https://docs.nvidia.com/introduction.html#general_conventions_lb_1general_scratch_buffer). Use[nppsMaximumRelativeErrorGetBufferSize_16sc_Ctx](https://docs.nvidia.com#group__signal__maximum__relative__error_1ga1ed02b930b50cb03e11731358392f427)to determine the minimum number of bytes required.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsMaximumRelativeError_32u_Ctx(const[Npp32u](https://docs.nvidia.com/nppdefs.html#c.Npp32u)*pSrc1, const[Npp32u](https://docs.nvidia.com/nppdefs.html#c.Npp32u)*pSrc2, size_t nLength,[Npp64f](https://docs.nvidia.com/nppdefs.html#c.Npp64f)*pDst,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDeviceBuffer,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsMaximumRelativeError_32u_Ctx)

-
32-bit unsigned short integer MaximumRelative method.

- Parameters
-
**pSrc1**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pSrc2**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**pDst**– Device memory pointer to the error result.**pDeviceBuffer**– Pointer to the required device memory allocation,[Scratch Buffer and Host Pointer](https://docs.nvidia.com/introduction.html#general_conventions_lb_1general_scratch_buffer). Use[nppsMaximumRelativeErrorGetBufferSize_32u_Ctx](https://docs.nvidia.com#group__signal__maximum__relative__error_1gad42ac0b106df1cac5b0191e5aa06a90d)to determine the minimum number of bytes required.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsMaximumRelativeError_32s_Ctx(const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pSrc1, const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pSrc2, size_t nLength,[Npp64f](https://docs.nvidia.com/nppdefs.html#c.Npp64f)*pDst,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDeviceBuffer,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsMaximumRelativeError_32s_Ctx)

-
32-bit signed short integer MaximumRelative method.

- Parameters
-
**pSrc1**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pSrc2**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**pDst**– Device memory pointer to the error result.**pDeviceBuffer**– Pointer to the required device memory allocation,[Scratch Buffer and Host Pointer](https://docs.nvidia.com/introduction.html#general_conventions_lb_1general_scratch_buffer). Use[nppsMaximumRelativeErrorGetBufferSize_32s_Ctx](https://docs.nvidia.com#group__signal__maximum__relative__error_1ga7336b2432954c96d4254e91154bb861f)to determine the minimum number of bytes required.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsMaximumRelativeError_32sc_Ctx(const[Npp32sc](https://docs.nvidia.com/nppdefs.html#c.Npp32sc)*pSrc1, const[Npp32sc](https://docs.nvidia.com/nppdefs.html#c.Npp32sc)*pSrc2, size_t nLength,[Npp64f](https://docs.nvidia.com/nppdefs.html#c.Npp64f)*pDst,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDeviceBuffer,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsMaximumRelativeError_32sc_Ctx)

-
32-bit unsigned short complex integer MaximumRelative method.

- Parameters
-
**pSrc1**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pSrc2**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**pDst**– Device memory pointer to the error result.**pDeviceBuffer**– Pointer to the required device memory allocation,[Scratch Buffer and Host Pointer](https://docs.nvidia.com/introduction.html#general_conventions_lb_1general_scratch_buffer). Use[nppsMaximumRelativeErrorGetBufferSize_32sc_Ctx](https://docs.nvidia.com#group__signal__maximum__relative__error_1gaee7142d229fa5b7d667325b7e2617e11)to determine the minimum number of bytes required.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsMaximumRelativeError_64s_Ctx(const[Npp64s](https://docs.nvidia.com/nppdefs.html#c.Npp64s)*pSrc1, const[Npp64s](https://docs.nvidia.com/nppdefs.html#c.Npp64s)*pSrc2, size_t nLength,[Npp64f](https://docs.nvidia.com/nppdefs.html#c.Npp64f)*pDst,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDeviceBuffer,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsMaximumRelativeError_64s_Ctx)

-
64-bit signed short integer MaximumRelative method.

- Parameters
-
**pSrc1**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pSrc2**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**pDst**– Device memory pointer to the error result.**pDeviceBuffer**– Pointer to the required device memory allocation,[Scratch Buffer and Host Pointer](https://docs.nvidia.com/introduction.html#general_conventions_lb_1general_scratch_buffer). Use[nppsMaximumRelativeErrorGetBufferSize_64s_Ctx](https://docs.nvidia.com#group__signal__maximum__relative__error_1ga96556d46ae11eefedee99eb882271fb6)to determine the minimum number of bytes required.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsMaximumRelativeError_64sc_Ctx(const[Npp64sc](https://docs.nvidia.com/nppdefs.html#c.Npp64sc)*pSrc1, const[Npp64sc](https://docs.nvidia.com/nppdefs.html#c.Npp64sc)*pSrc2, size_t nLength,[Npp64f](https://docs.nvidia.com/nppdefs.html#c.Npp64f)*pDst,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDeviceBuffer,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsMaximumRelativeError_64sc_Ctx)

-
64-bit unsigned short complex integer MaximumRelative method.

- Parameters
-
**pSrc1**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pSrc2**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**pDst**– Device memory pointer to the error result.**pDeviceBuffer**– Pointer to the required device memory allocation,[Scratch Buffer and Host Pointer](https://docs.nvidia.com/introduction.html#general_conventions_lb_1general_scratch_buffer). Use[nppsMaximumRelativeErrorGetBufferSize_64sc_Ctx](https://docs.nvidia.com#group__signal__maximum__relative__error_1ga86576ee579c9daa5f0b42e3286dcacaa)to determine the minimum number of bytes required.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsMaximumRelativeError_32f_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc1, const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc2, size_t nLength,[Npp64f](https://docs.nvidia.com/nppdefs.html#c.Npp64f)*pDst,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDeviceBuffer,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsMaximumRelativeError_32f_Ctx)

-
32-bit floating point MaximumRelative method.

- Parameters
-
**pSrc1**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pSrc2**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**pDst**– Device memory pointer to the error result.**pDeviceBuffer**– Pointer to the required device memory allocation,[Scratch Buffer and Host Pointer](https://docs.nvidia.com/introduction.html#general_conventions_lb_1general_scratch_buffer). Use[nppsMaximumRelativeErrorGetBufferSize_32f_Ctx](https://docs.nvidia.com#group__signal__maximum__relative__error_1gafa2db23cb263fdc95ce1ee5929eba989)to determine the minimum number of bytes required.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsMaximumRelativeError_32fc_Ctx(const[Npp32fc](https://docs.nvidia.com/nppdefs.html#c.Npp32fc)*pSrc1, const[Npp32fc](https://docs.nvidia.com/nppdefs.html#c.Npp32fc)*pSrc2, size_t nLength,[Npp64f](https://docs.nvidia.com/nppdefs.html#c.Npp64f)*pDst,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDeviceBuffer,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsMaximumRelativeError_32fc_Ctx)

-
32-bit floating point complex MaximumRelative method.

- Parameters
-
**pSrc1**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pSrc2**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**pDst**– Device memory pointer to the error result.**pDeviceBuffer**– Pointer to the required device memory allocation,[Scratch Buffer and Host Pointer](https://docs.nvidia.com/introduction.html#general_conventions_lb_1general_scratch_buffer). Use[nppsMaximumRelativeErrorGetBufferSize_32fc_Ctx](https://docs.nvidia.com#group__signal__maximum__relative__error_1ga737fd0d86b299ebd6371c2619e2abcc4)to determine the minimum number of bytes required.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsMaximumRelativeError_64f_Ctx(const[Npp64f](https://docs.nvidia.com/nppdefs.html#c.Npp64f)*pSrc1, const[Npp64f](https://docs.nvidia.com/nppdefs.html#c.Npp64f)*pSrc2, size_t nLength,[Npp64f](https://docs.nvidia.com/nppdefs.html#c.Npp64f)*pDst,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDeviceBuffer,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsMaximumRelativeError_64f_Ctx)

-
64-bit floating point MaximumRelative method.

- Parameters
-
**pSrc1**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pSrc2**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**pDst**– Device memory pointer to the error result.**pDeviceBuffer**– Pointer to the required device memory allocation,[Scratch Buffer and Host Pointer](https://docs.nvidia.com/introduction.html#general_conventions_lb_1general_scratch_buffer). Use[nppsMaximumRelativeErrorGetBufferSize_64f_Ctx](https://docs.nvidia.com#group__signal__maximum__relative__error_1gab82163a16ca7e863c70291aea638fa9d)to determine the minimum number of bytes required.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsMaximumRelativeError_64fc_Ctx(const[Npp64fc](https://docs.nvidia.com/nppdefs.html#c.Npp64fc)*pSrc1, const[Npp64fc](https://docs.nvidia.com/nppdefs.html#c.Npp64fc)*pSrc2, size_t nLength,[Npp64f](https://docs.nvidia.com/nppdefs.html#c.Npp64f)*pDst,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDeviceBuffer,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsMaximumRelativeError_64fc_Ctx)

-
64-bit floating point complex MaximumRelative method.

- Parameters
-
**pSrc1**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pSrc2**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**pDst**– Device memory pointer to the error result.**pDeviceBuffer**– Pointer to the required device memory allocation,[Scratch Buffer and Host Pointer](https://docs.nvidia.com/introduction.html#general_conventions_lb_1general_scratch_buffer). Use[nppsMaximumRelativeErrorGetBufferSize_64fc_Ctx](https://docs.nvidia.com#group__signal__maximum__relative__error_1ga2d0c85ec7a947ce29c9f4fedede31c96)to determine the minimum number of bytes required.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsMaximumRelativeErrorGetBufferSize_8u_Ctx(size_t nLength, size_t *hpBufferSize,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsMaximumRelativeErrorGetBufferSize_8u_Ctx)

-
Device-buffer size (in bytes) for nppsMaximumRelativeError_8u.

- Parameters
-
**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**hpBufferSize**– Required buffer size. Important: hpBufferSize is a*host pointer.***nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
NPP_SUCCESS



-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsMaximumRelativeErrorGetBufferSize_8s_Ctx(size_t nLength, size_t *hpBufferSize,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsMaximumRelativeErrorGetBufferSize_8s_Ctx)

-
Device-buffer size (in bytes) for nppsMaximumRelativeError_8s.

- Parameters
-
**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**hpBufferSize**– Required buffer size. Important: hpBufferSize is a*host pointer.***nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
NPP_SUCCESS



-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsMaximumRelativeErrorGetBufferSize_16u_Ctx(size_t nLength, size_t *hpBufferSize,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsMaximumRelativeErrorGetBufferSize_16u_Ctx)

-
Device-buffer size (in bytes) for nppsMaximumRelativeError_16u.

- Parameters
-
**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**hpBufferSize**– Required buffer size. Important: hpBufferSize is a*host pointer.***nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
NPP_SUCCESS



-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsMaximumRelativeErrorGetBufferSize_16s_Ctx(size_t nLength, size_t *hpBufferSize,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsMaximumRelativeErrorGetBufferSize_16s_Ctx)

-
Device-buffer size (in bytes) for nppsMaximumRelativeError_16s.

- Parameters
-
**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**hpBufferSize**– Required buffer size. Important: hpBufferSize is a*host pointer.***nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
NPP_SUCCESS



-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsMaximumRelativeErrorGetBufferSize_16sc_Ctx(size_t nLength, size_t *hpBufferSize,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsMaximumRelativeErrorGetBufferSize_16sc_Ctx)

-
Device-buffer size (in bytes) for nppsMaximumRelativeError_16sc.

- Parameters
-
**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**hpBufferSize**– Required buffer size. Important: hpBufferSize is a*host pointer.***nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
NPP_SUCCESS



-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsMaximumRelativeErrorGetBufferSize_32u_Ctx(size_t nLength, size_t *hpBufferSize,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsMaximumRelativeErrorGetBufferSize_32u_Ctx)

-
Device-buffer size (in bytes) for nppsMaximumRelativeError_32u.

- Parameters
-
**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**hpBufferSize**– Required buffer size. Important: hpBufferSize is a*host pointer.***nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
NPP_SUCCESS



-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsMaximumRelativeErrorGetBufferSize_32s_Ctx(size_t nLength, size_t *hpBufferSize,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsMaximumRelativeErrorGetBufferSize_32s_Ctx)

-
Device-buffer size (in bytes) for nppsMaximumRelativeError_32s.

- Parameters
-
**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**hpBufferSize**– Required buffer size. Important: hpBufferSize is a*host pointer.***nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
NPP_SUCCESS



-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsMaximumRelativeErrorGetBufferSize_32sc_Ctx(size_t nLength, size_t *hpBufferSize,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsMaximumRelativeErrorGetBufferSize_32sc_Ctx)

-
Device-buffer size (in bytes) for nppsMaximumRelativeError_32sc.

- Parameters
-
**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**hpBufferSize**– Required buffer size. Important: hpBufferSize is a*host pointer.***nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
NPP_SUCCESS



-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsMaximumRelativeErrorGetBufferSize_64s_Ctx(size_t nLength, size_t *hpBufferSize,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsMaximumRelativeErrorGetBufferSize_64s_Ctx)

-
Device-buffer size (in bytes) for nppsMaximumRelativeError_64s.

- Parameters
-
**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**hpBufferSize**– Required buffer size. Important: hpBufferSize is a*host pointer.***nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
NPP_SUCCESS



-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsMaximumRelativeErrorGetBufferSize_64sc_Ctx(size_t nLength, size_t *hpBufferSize,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsMaximumRelativeErrorGetBufferSize_64sc_Ctx)

-
Device-buffer size (in bytes) for nppsMaximumRelativeError_64sc.

- Parameters
-
**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**hpBufferSize**– Required buffer size. Important: hpBufferSize is a*host pointer.***nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
NPP_SUCCESS



-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsMaximumRelativeErrorGetBufferSize_32f_Ctx(size_t nLength, size_t *hpBufferSize,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsMaximumRelativeErrorGetBufferSize_32f_Ctx)

-
Device-buffer size (in bytes) for nppsMaximumRelativeError_32f.

- Parameters
-
**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**hpBufferSize**– Required buffer size. Important: hpBufferSize is a*host pointer.***nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
NPP_SUCCESS



-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsMaximumRelativeErrorGetBufferSize_32fc_Ctx(size_t nLength, size_t *hpBufferSize,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsMaximumRelativeErrorGetBufferSize_32fc_Ctx)

-
Device-buffer size (in bytes) for nppsMaximumRelativeError_32fc.

- Parameters
-
**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**hpBufferSize**– Required buffer size. Important: hpBufferSize is a*host pointer.***nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
NPP_SUCCESS



-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsMaximumRelativeErrorGetBufferSize_64f_Ctx(size_t nLength, size_t *hpBufferSize,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsMaximumRelativeErrorGetBufferSize_64f_Ctx)

-
Device-buffer size (in bytes) for nppsMaximumRelativeError_64f.

- Parameters
-
**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**hpBufferSize**– Required buffer size. Important: hpBufferSize is a*host pointer.***nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
NPP_SUCCESS



-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsMaximumRelativeErrorGetBufferSize_64fc_Ctx(size_t nLength, size_t *hpBufferSize,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsMaximumRelativeErrorGetBufferSize_64fc_Ctx)

-
Device-buffer size (in bytes) for nppsMaximumRelativeError_64fc.

- Parameters
-
**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**hpBufferSize**– Required buffer size. Important: hpBufferSize is a*host pointer.***nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
NPP_SUCCESS



## Signal Average Relative Error[](https://docs.nvidia.com#signal-average-relative-error)

### AverageRelativeError[](https://docs.nvidia.com#group__signal__average__relative__error_1signal_average_relative_error)

Primitives for computing the AverageRelative error between two signals. Given two signals \(pSrc1\) and \(pSrc2\) both with length \(N\), the average relative error is defined as

If the signal is in complex format, the absolute value of the complex number is used.

Functions

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsAverageRelativeError_8u_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc1, const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc2, size_t nLength,[Npp64f](https://docs.nvidia.com/nppdefs.html#c.Npp64f)*pDst,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDeviceBuffer,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsAverageRelativeError_8u_Ctx)

-
8-bit unsigned char AverageRelative method.

- Parameters
-
**pSrc1**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pSrc2**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**pDst**– Device memory pointer to the error result.**pDeviceBuffer**– Pointer to the required device memory allocation,[Scratch Buffer and Host Pointer](https://docs.nvidia.com/introduction.html#general_conventions_lb_1general_scratch_buffer). Use[nppsAverageRelativeErrorGetBufferSize_8u_Ctx](https://docs.nvidia.com#group__signal__average__relative__error_1ga71ed81bdd08fafbf238a44c134d358b1)to determine the minimum number of bytes required.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsAverageRelativeError_8s_Ctx(const[Npp8s](https://docs.nvidia.com/nppdefs.html#c.Npp8s)*pSrc1, const[Npp8s](https://docs.nvidia.com/nppdefs.html#c.Npp8s)*pSrc2, size_t nLength,[Npp64f](https://docs.nvidia.com/nppdefs.html#c.Npp64f)*pDst,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDeviceBuffer,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsAverageRelativeError_8s_Ctx)

-
8-bit signed char AverageRelative method.

- Parameters
-
**pSrc1**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pSrc2**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**pDst**– Device memory pointer to the error result.**pDeviceBuffer**– Pointer to the required device memory allocation,[Scratch Buffer and Host Pointer](https://docs.nvidia.com/introduction.html#general_conventions_lb_1general_scratch_buffer). Use[nppsAverageRelativeErrorGetBufferSize_8s_Ctx](https://docs.nvidia.com#group__signal__average__relative__error_1ga49ecc023b7a214d1649f0192c22706c5)to determine the minimum number of bytes required.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsAverageRelativeError_16u_Ctx(const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrc1, const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrc2, size_t nLength,[Npp64f](https://docs.nvidia.com/nppdefs.html#c.Npp64f)*pDst,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDeviceBuffer,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsAverageRelativeError_16u_Ctx)

-
16-bit unsigned short integer AverageRelative method.

- Parameters
-
**pSrc1**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pSrc2**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**pDst**– Device memory pointer to the error result.**pDeviceBuffer**– Pointer to the required device memory allocation,[Scratch Buffer and Host Pointer](https://docs.nvidia.com/introduction.html#general_conventions_lb_1general_scratch_buffer). Use[nppsAverageRelativeErrorGetBufferSize_16u_Ctx](https://docs.nvidia.com#group__signal__average__relative__error_1ga740cdc42c9be4941ac54407631812e50)to determine the minimum number of bytes required.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsAverageRelativeError_16s_Ctx(const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrc1, const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrc2, size_t nLength,[Npp64f](https://docs.nvidia.com/nppdefs.html#c.Npp64f)*pDst,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDeviceBuffer,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsAverageRelativeError_16s_Ctx)

-
16-bit signed short integer AverageRelative method.

- Parameters
-
**pSrc1**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pSrc2**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**pDst**– Device memory pointer to the error result.**pDeviceBuffer**– Pointer to the required device memory allocation,[Scratch Buffer and Host Pointer](https://docs.nvidia.com/introduction.html#general_conventions_lb_1general_scratch_buffer). Use[nppsAverageRelativeErrorGetBufferSize_16s_Ctx](https://docs.nvidia.com#group__signal__average__relative__error_1ga8087543937d0afa7166b2830a3aaf0c5)to determine the minimum number of bytes required.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsAverageRelativeError_16sc_Ctx(const[Npp16sc](https://docs.nvidia.com/nppdefs.html#c.Npp16sc)*pSrc1, const[Npp16sc](https://docs.nvidia.com/nppdefs.html#c.Npp16sc)*pSrc2, size_t nLength,[Npp64f](https://docs.nvidia.com/nppdefs.html#c.Npp64f)*pDst,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDeviceBuffer,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsAverageRelativeError_16sc_Ctx)

-
16-bit unsigned short complex integer AverageRelative method.

- Parameters
-
**pSrc1**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pSrc2**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**pDst**– Device memory pointer to the error result.**pDeviceBuffer**– Pointer to the required device memory allocation,[Scratch Buffer and Host Pointer](https://docs.nvidia.com/introduction.html#general_conventions_lb_1general_scratch_buffer). Use[nppsAverageRelativeErrorGetBufferSize_16sc_Ctx](https://docs.nvidia.com#group__signal__average__relative__error_1ga083886e57a62cf7d9a3314231d8e5fe8)to determine the minimum number of bytes required.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsAverageRelativeError_32u_Ctx(const[Npp32u](https://docs.nvidia.com/nppdefs.html#c.Npp32u)*pSrc1, const[Npp32u](https://docs.nvidia.com/nppdefs.html#c.Npp32u)*pSrc2, size_t nLength,[Npp64f](https://docs.nvidia.com/nppdefs.html#c.Npp64f)*pDst,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDeviceBuffer,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsAverageRelativeError_32u_Ctx)

-
32-bit unsigned short integer AverageRelative method.

- Parameters
-
**pSrc1**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pSrc2**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**pDst**– Device memory pointer to the error result.**pDeviceBuffer**– Pointer to the required device memory allocation,[Scratch Buffer and Host Pointer](https://docs.nvidia.com/introduction.html#general_conventions_lb_1general_scratch_buffer). Use[nppsAverageRelativeErrorGetBufferSize_32u_Ctx](https://docs.nvidia.com#group__signal__average__relative__error_1ga7c13bf1dfcebf2c4548de88d6a331502)to determine the minimum number of bytes required.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsAverageRelativeError_32s_Ctx(const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pSrc1, const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pSrc2, size_t nLength,[Npp64f](https://docs.nvidia.com/nppdefs.html#c.Npp64f)*pDst,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDeviceBuffer,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsAverageRelativeError_32s_Ctx)

-
32-bit signed short integer AverageRelative method.

- Parameters
-
**pSrc1**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pSrc2**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**pDst**– Device memory pointer to the error result.**pDeviceBuffer**– Pointer to the required device memory allocation,[Scratch Buffer and Host Pointer](https://docs.nvidia.com/introduction.html#general_conventions_lb_1general_scratch_buffer). Use[nppsAverageRelativeErrorGetBufferSize_32s_Ctx](https://docs.nvidia.com#group__signal__average__relative__error_1gaf30253dada5acd2b4348c4fcbb695d67)to determine the minimum number of bytes required.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsAverageRelativeError_32sc_Ctx(const[Npp32sc](https://docs.nvidia.com/nppdefs.html#c.Npp32sc)*pSrc1, const[Npp32sc](https://docs.nvidia.com/nppdefs.html#c.Npp32sc)*pSrc2, size_t nLength,[Npp64f](https://docs.nvidia.com/nppdefs.html#c.Npp64f)*pDst,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDeviceBuffer,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsAverageRelativeError_32sc_Ctx)

-
32-bit unsigned short complex integer AverageRelative method.

- Parameters
-
**pSrc1**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pSrc2**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**pDst**– Device memory pointer to the error result.**pDeviceBuffer**– Pointer to the required device memory allocation,[Scratch Buffer and Host Pointer](https://docs.nvidia.com/introduction.html#general_conventions_lb_1general_scratch_buffer). Use[nppsAverageRelativeErrorGetBufferSize_32sc_Ctx](https://docs.nvidia.com#group__signal__average__relative__error_1gad138d5523a19afb532c679f823323102)to determine the minimum number of bytes required.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsAverageRelativeError_64s_Ctx(const[Npp64s](https://docs.nvidia.com/nppdefs.html#c.Npp64s)*pSrc1, const[Npp64s](https://docs.nvidia.com/nppdefs.html#c.Npp64s)*pSrc2, size_t nLength,[Npp64f](https://docs.nvidia.com/nppdefs.html#c.Npp64f)*pDst,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDeviceBuffer,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsAverageRelativeError_64s_Ctx)

-
64-bit signed short integer AverageRelative method.

- Parameters
-
**pSrc1**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pSrc2**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**pDst**– Device memory pointer to the error result.**pDeviceBuffer**– Pointer to the required device memory allocation,[Scratch Buffer and Host Pointer](https://docs.nvidia.com/introduction.html#general_conventions_lb_1general_scratch_buffer). Use[nppsAverageRelativeErrorGetBufferSize_64s_Ctx](https://docs.nvidia.com#group__signal__average__relative__error_1ga8e61f26239e9dcb59eb87eede3805e45)to determine the minimum number of bytes required.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsAverageRelativeError_64sc_Ctx(const[Npp64sc](https://docs.nvidia.com/nppdefs.html#c.Npp64sc)*pSrc1, const[Npp64sc](https://docs.nvidia.com/nppdefs.html#c.Npp64sc)*pSrc2, size_t nLength,[Npp64f](https://docs.nvidia.com/nppdefs.html#c.Npp64f)*pDst,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDeviceBuffer,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsAverageRelativeError_64sc_Ctx)

-
64-bit unsigned short complex integer AverageRelative method.

- Parameters
-
**pSrc1**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pSrc2**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**pDst**– Device memory pointer to the error result.**pDeviceBuffer**– Pointer to the required device memory allocation,[Scratch Buffer and Host Pointer](https://docs.nvidia.com/introduction.html#general_conventions_lb_1general_scratch_buffer). Use[nppsAverageRelativeErrorGetBufferSize_64sc_Ctx](https://docs.nvidia.com#group__signal__average__relative__error_1gaaec333e709012a765e4ee692494e72bb)to determine the minimum number of bytes required.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsAverageRelativeError_32f_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc1, const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc2, size_t nLength,[Npp64f](https://docs.nvidia.com/nppdefs.html#c.Npp64f)*pDst,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDeviceBuffer,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsAverageRelativeError_32f_Ctx)

-
32-bit floating point AverageRelative method.

- Parameters
-
**pSrc1**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pSrc2**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**pDst**– Device memory pointer to the error result.**pDeviceBuffer**– Pointer to the required device memory allocation,[Scratch Buffer and Host Pointer](https://docs.nvidia.com/introduction.html#general_conventions_lb_1general_scratch_buffer). Use[nppsAverageRelativeErrorGetBufferSize_32f_Ctx](https://docs.nvidia.com#group__signal__average__relative__error_1gad8b8838cb98e0f15892d73c2215f5fa0)to determine the minimum number of bytes required.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsAverageRelativeError_32fc_Ctx(const[Npp32fc](https://docs.nvidia.com/nppdefs.html#c.Npp32fc)*pSrc1, const[Npp32fc](https://docs.nvidia.com/nppdefs.html#c.Npp32fc)*pSrc2, size_t nLength,[Npp64f](https://docs.nvidia.com/nppdefs.html#c.Npp64f)*pDst,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDeviceBuffer,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsAverageRelativeError_32fc_Ctx)

-
32-bit floating point complex AverageRelative method.

- Parameters
-
**pSrc1**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pSrc2**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**pDst**– Device memory pointer to the error result.**pDeviceBuffer**– Pointer to the required device memory allocation,[Scratch Buffer and Host Pointer](https://docs.nvidia.com/introduction.html#general_conventions_lb_1general_scratch_buffer). Use[nppsAverageRelativeErrorGetBufferSize_32fc_Ctx](https://docs.nvidia.com#group__signal__average__relative__error_1gaa49b2af75a4ec6f31e871d80ee390d9b)to determine the minimum number of bytes required.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsAverageRelativeError_64f_Ctx(const[Npp64f](https://docs.nvidia.com/nppdefs.html#c.Npp64f)*pSrc1, const[Npp64f](https://docs.nvidia.com/nppdefs.html#c.Npp64f)*pSrc2, size_t nLength,[Npp64f](https://docs.nvidia.com/nppdefs.html#c.Npp64f)*pDst,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDeviceBuffer,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsAverageRelativeError_64f_Ctx)

-
64-bit floating point AverageRelative method.

- Parameters
-
**pSrc1**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pSrc2**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**pDst**– Device memory pointer to the error result.**pDeviceBuffer**– Pointer to the required device memory allocation,[Scratch Buffer and Host Pointer](https://docs.nvidia.com/introduction.html#general_conventions_lb_1general_scratch_buffer). Use[nppsAverageRelativeErrorGetBufferSize_64f_Ctx](https://docs.nvidia.com#group__signal__average__relative__error_1ga711a52b9f21f92dc6193595317bd9715)to determine the minimum number of bytes required.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsAverageRelativeError_64fc_Ctx(const[Npp64fc](https://docs.nvidia.com/nppdefs.html#c.Npp64fc)*pSrc1, const[Npp64fc](https://docs.nvidia.com/nppdefs.html#c.Npp64fc)*pSrc2, size_t nLength,[Npp64f](https://docs.nvidia.com/nppdefs.html#c.Npp64f)*pDst,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDeviceBuffer,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsAverageRelativeError_64fc_Ctx)

-
64-bit floating point complex AverageRelative method.

- Parameters
-
**pSrc1**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pSrc2**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**pDst**– Device memory pointer to the error result.**pDeviceBuffer**– Pointer to the required device memory allocation,[Scratch Buffer and Host Pointer](https://docs.nvidia.com/introduction.html#general_conventions_lb_1general_scratch_buffer). Use[nppsAverageRelativeErrorGetBufferSize_64fc_Ctx](https://docs.nvidia.com#group__signal__average__relative__error_1ga53905917f7b9e0b332972e1ff6bcc237)to determine the minimum number of bytes required.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsAverageRelativeErrorGetBufferSize_8u_Ctx(size_t nLength, size_t *hpBufferSize,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsAverageRelativeErrorGetBufferSize_8u_Ctx)

-
Device-buffer size (in bytes) for nppsAverageRelativeError_8u_Ctx.

- Parameters
-
**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**hpBufferSize**– Required buffer size. Important: hpBufferSize is a*host pointer.***nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
NPP_SUCCESS



-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsAverageRelativeErrorGetBufferSize_8s_Ctx(size_t nLength, size_t *hpBufferSize,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsAverageRelativeErrorGetBufferSize_8s_Ctx)

-
Device-buffer size (in bytes) for nppsAverageRelativeError_8s_Ctx.

- Parameters
-
**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**hpBufferSize**– Required buffer size. Important: hpBufferSize is a*host pointer.***nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
NPP_SUCCESS



-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsAverageRelativeErrorGetBufferSize_16u_Ctx(size_t nLength, size_t *hpBufferSize,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsAverageRelativeErrorGetBufferSize_16u_Ctx)

-
Device-buffer size (in bytes) for nppsAverageRelativeError_16u_Ctx.

- Parameters
-
**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**hpBufferSize**– Required buffer size. Important: hpBufferSize is a*host pointer.***nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
NPP_SUCCESS



-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsAverageRelativeErrorGetBufferSize_16s_Ctx(size_t nLength, size_t *hpBufferSize,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsAverageRelativeErrorGetBufferSize_16s_Ctx)

-
Device-buffer size (in bytes) for nppsAverageRelativeError_16s_Ctx.

- Parameters
-
**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**hpBufferSize**– Required buffer size. Important: hpBufferSize is a*host pointer.***nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
NPP_SUCCESS



-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsAverageRelativeErrorGetBufferSize_16sc_Ctx(size_t nLength, size_t *hpBufferSize,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsAverageRelativeErrorGetBufferSize_16sc_Ctx)

-
Device-buffer size (in bytes) for nppsAverageRelativeError_16sc_Ctx.

- Parameters
-
**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**hpBufferSize**– Required buffer size. Important: hpBufferSize is a*host pointer.***nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
NPP_SUCCESS



-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsAverageRelativeErrorGetBufferSize_32u_Ctx(size_t nLength, size_t *hpBufferSize,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsAverageRelativeErrorGetBufferSize_32u_Ctx)

-
Device-buffer size (in bytes) for nppsAverageRelativeError_32u_Ctx.

- Parameters
-
**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**hpBufferSize**– Required buffer size. Important: hpBufferSize is a*host pointer.***nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
NPP_SUCCESS



-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsAverageRelativeErrorGetBufferSize_32s_Ctx(size_t nLength, size_t *hpBufferSize,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsAverageRelativeErrorGetBufferSize_32s_Ctx)

-
Device-buffer size (in bytes) for nppsAverageRelativeError_32s_Ctx.

- Parameters
-
**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**hpBufferSize**– Required buffer size. Important: hpBufferSize is a*host pointer.***nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
NPP_SUCCESS



-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsAverageRelativeErrorGetBufferSize_32sc_Ctx(size_t nLength, size_t *hpBufferSize,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsAverageRelativeErrorGetBufferSize_32sc_Ctx)

-
Device-buffer size (in bytes) for nppsAverageRelativeError_32sc_Ctx.

- Parameters
-
**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**hpBufferSize**– Required buffer size. Important: hpBufferSize is a*host pointer.***nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
NPP_SUCCESS



-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsAverageRelativeErrorGetBufferSize_64s_Ctx(size_t nLength, size_t *hpBufferSize,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsAverageRelativeErrorGetBufferSize_64s_Ctx)

-
Device-buffer size (in bytes) for nppsAverageRelativeError_64s_Ctx.

- Parameters
-
**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**hpBufferSize**– Required buffer size. Important: hpBufferSize is a*host pointer.***nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
NPP_SUCCESS



-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsAverageRelativeErrorGetBufferSize_64sc_Ctx(size_t nLength, size_t *hpBufferSize,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsAverageRelativeErrorGetBufferSize_64sc_Ctx)

-
Device-buffer size (in bytes) for nppsAverageRelativeError_64sc_Ctx.

- Parameters
-
**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**hpBufferSize**– Required buffer size. Important: hpBufferSize is a*host pointer.***nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
NPP_SUCCESS



-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsAverageRelativeErrorGetBufferSize_32f_Ctx(size_t nLength, size_t *hpBufferSize,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsAverageRelativeErrorGetBufferSize_32f_Ctx)

-
Device-buffer size (in bytes) for nppsAverageRelativeError_32f_Ctx.

- Parameters
-
**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**hpBufferSize**– Required buffer size. Important: hpBufferSize is a*host pointer.***nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
NPP_SUCCESS



-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsAverageRelativeErrorGetBufferSize_32fc_Ctx(size_t nLength, size_t *hpBufferSize,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsAverageRelativeErrorGetBufferSize_32fc_Ctx)

-
Device-buffer size (in bytes) for nppsAverageRelativeError_32fc_Ctx.

- Parameters
-
**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**hpBufferSize**– Required buffer size. Important: hpBufferSize is a*host pointer.***nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
NPP_SUCCESS



-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsAverageRelativeErrorGetBufferSize_64f_Ctx(size_t nLength, size_t *hpBufferSize,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsAverageRelativeErrorGetBufferSize_64f_Ctx)

-
Device-buffer size (in bytes) for nppsAverageRelativeError_64f_Ctx.

- Parameters
-
**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**hpBufferSize**– Required buffer size. Important: hpBufferSize is a*host pointer.***nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
NPP_SUCCESS



-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsAverageRelativeErrorGetBufferSize_64fc_Ctx(size_t nLength, size_t *hpBufferSize,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsAverageRelativeErrorGetBufferSize_64fc_Ctx)

-
Device-buffer size (in bytes) for nppsAverageRelativeError_64fc_Ctx.

- Parameters
-
**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**hpBufferSize**– Required buffer size. Important: hpBufferSize is a*host pointer.***nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
NPP_SUCCESS