source: https://docs.nvidia.com/cuda/npp/signal_conversion_functions.html

# Signal Conversion Functions[](https://docs.nvidia.com#signal-conversion-functions)

Functions that provide conversion and threshold operations.

## Signal Convert[](https://docs.nvidia.com#signal-convert)

### Convert[](https://docs.nvidia.com#group__signal__convert_1signal_convert)

The set of conversion operations available in the library

Convert

Routines for converting the sample-data type of signals.

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsConvert_8s16s_Ctx(const[Npp8s](https://docs.nvidia.com/nppdefs.html#c.Npp8s)*pSrc,[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pDst, size_t nLength,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsConvert_8s16s_Ctx)

-
8-bit signed byte to 16-bit signed short conversion

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsConvert_8s32f_Ctx(const[Npp8s](https://docs.nvidia.com/nppdefs.html#c.Npp8s)*pSrc,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pDst, size_t nLength,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsConvert_8s32f_Ctx)

-
8-bit signed byte to 32-bit floating point number conversion

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsConvert_8u32f_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pDst, size_t nLength,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsConvert_8u32f_Ctx)

-
8-bit unsigned byte to 32-bit floating point number conversion

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsConvert_16s8s_Sfs_Ctx(const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrc,[Npp8s](https://docs.nvidia.com/nppdefs.html#c.Npp8s)*pDst,[Npp32u](https://docs.nvidia.com/nppdefs.html#c.Npp32u)nLength,[NppRoundMode](https://docs.nvidia.com/nppdefs.html#c.NppRoundMode)eRoundMode, int nScaleFactor,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsConvert_16s8s_Sfs_Ctx)

-
16-bit signed short to 8-bit signed byte conversion

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**eRoundMode**–[Rounding Mode Parameter](https://docs.nvidia.com/introduction.html#general_conventions_lb_1rounding_mode_parameter).**nScaleFactor**– nScaleFactor**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsConvert_16s32s_Ctx(const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrc,[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pDst, size_t nLength,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsConvert_16s32s_Ctx)

-
16-bit signed short to 32-bit signed integer conversion

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsConvert_16s32f_Ctx(const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrc,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pDst, size_t nLength,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsConvert_16s32f_Ctx)

-
16-bit signed short to 32-bit floating point number conversion

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsConvert_16u32f_Ctx(const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrc,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pDst, size_t nLength,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsConvert_16u32f_Ctx)

-
16-bit unsigned short to 32-bit floating point number conversion

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsConvert_32s16s_Ctx(const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pSrc,[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pDst, size_t nLength,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsConvert_32s16s_Ctx)

-
32-bit signed integer to 16-bit signed short conversion

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsConvert_32s32f_Ctx(const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pSrc,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pDst, size_t nLength,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsConvert_32s32f_Ctx)

-
32-bit signed integer to 32-bit floating point number conversion

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsConvert_32s64f_Ctx(const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pSrc,[Npp64f](https://docs.nvidia.com/nppdefs.html#c.Npp64f)*pDst, size_t nLength,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsConvert_32s64f_Ctx)

-
32-bit signed integer to 64-bit floating point number conversion

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsConvert_32f64f_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc,[Npp64f](https://docs.nvidia.com/nppdefs.html#c.Npp64f)*pDst, size_t nLength,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsConvert_32f64f_Ctx)

-
32-bit floating point number to 64-bit floating point number conversion

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsConvert_64s64f_Ctx(const[Npp64s](https://docs.nvidia.com/nppdefs.html#c.Npp64s)*pSrc,[Npp64f](https://docs.nvidia.com/nppdefs.html#c.Npp64f)*pDst, size_t nLength,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsConvert_64s64f_Ctx)

-
64-bit signed integer to 64-bit floating point number conversion

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsConvert_64f32f_Ctx(const[Npp64f](https://docs.nvidia.com/nppdefs.html#c.Npp64f)*pSrc,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pDst, size_t nLength,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsConvert_64f32f_Ctx)

-
64-bit floating point number to 32-bit floating point number conversion

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsConvert_16s32f_Sfs_Ctx(const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrc,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pDst, size_t nLength, int nScaleFactor,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsConvert_16s32f_Sfs_Ctx)

-
16-bit signed short to 32-bit floating point number conversion with scaling

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nScaleFactor**–[Integer Result Scaling](https://docs.nvidia.com/introduction.html#general_conventions_lb_1integer_result_scaling).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsConvert_16s64f_Sfs_Ctx(const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrc,[Npp64f](https://docs.nvidia.com/nppdefs.html#c.Npp64f)*pDst, size_t nLength, int nScaleFactor,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsConvert_16s64f_Sfs_Ctx)

-
16-bit signed short to 64-bit floating point number conversion with scaling

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nScaleFactor**–[Integer Result Scaling](https://docs.nvidia.com/introduction.html#general_conventions_lb_1integer_result_scaling).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsConvert_32s16s_Sfs_Ctx(const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pSrc,[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pDst, size_t nLength, int nScaleFactor,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsConvert_32s16s_Sfs_Ctx)

-
32-bit signed integer to 16-bit signed short conversion with scaling

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nScaleFactor**–[Integer Result Scaling](https://docs.nvidia.com/introduction.html#general_conventions_lb_1integer_result_scaling).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsConvert_32s32f_Sfs_Ctx(const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pSrc,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pDst, size_t nLength, int nScaleFactor,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsConvert_32s32f_Sfs_Ctx)

-
32-bit signed integer to 32-bit floating point number conversion with scaling

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nScaleFactor**–[Integer Result Scaling](https://docs.nvidia.com/introduction.html#general_conventions_lb_1integer_result_scaling).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsConvert_32s64f_Sfs_Ctx(const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pSrc,[Npp64f](https://docs.nvidia.com/nppdefs.html#c.Npp64f)*pDst, size_t nLength, int nScaleFactor,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsConvert_32s64f_Sfs_Ctx)

-
32-bit signed integer to 64-bit floating point number conversion with scaling

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nScaleFactor**–[Integer Result Scaling](https://docs.nvidia.com/introduction.html#general_conventions_lb_1integer_result_scaling).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsConvert_32f8s_Sfs_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc,[Npp8s](https://docs.nvidia.com/nppdefs.html#c.Npp8s)*pDst, size_t nLength,[NppRoundMode](https://docs.nvidia.com/nppdefs.html#c.NppRoundMode)eRoundMode, int nScaleFactor,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsConvert_32f8s_Sfs_Ctx)

-
32-bit signed integer to 8-bit signed byte conversion with scaling

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**eRoundMode**–[Rounding Mode Parameter](https://docs.nvidia.com/introduction.html#general_conventions_lb_1rounding_mode_parameter).**nScaleFactor**–[Integer Result Scaling](https://docs.nvidia.com/introduction.html#general_conventions_lb_1integer_result_scaling).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsConvert_32f8u_Sfs_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, size_t nLength,[NppRoundMode](https://docs.nvidia.com/nppdefs.html#c.NppRoundMode)eRoundMode, int nScaleFactor,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsConvert_32f8u_Sfs_Ctx)

-
32-bit floating point number to 8-bit unsigned byte conversion with scaling

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**eRoundMode**–[Rounding Mode Parameter](https://docs.nvidia.com/introduction.html#general_conventions_lb_1rounding_mode_parameter).**nScaleFactor**–[Integer Result Scaling](https://docs.nvidia.com/introduction.html#general_conventions_lb_1integer_result_scaling).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsConvert_32f16s_Sfs_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc,[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pDst, size_t nLength,[NppRoundMode](https://docs.nvidia.com/nppdefs.html#c.NppRoundMode)eRoundMode, int nScaleFactor,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsConvert_32f16s_Sfs_Ctx)

-
32-bit floating point number to 16-bit signed short conversion with scaling

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**eRoundMode**–[Rounding Mode Parameter](https://docs.nvidia.com/introduction.html#general_conventions_lb_1rounding_mode_parameter).**nScaleFactor**–[Integer Result Scaling](https://docs.nvidia.com/introduction.html#general_conventions_lb_1integer_result_scaling).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsConvert_32f16u_Sfs_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc,[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pDst, size_t nLength,[NppRoundMode](https://docs.nvidia.com/nppdefs.html#c.NppRoundMode)eRoundMode, int nScaleFactor,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsConvert_32f16u_Sfs_Ctx)

-
32-bit floating point number to 16-bit unsigned short conversion with scaling

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**eRoundMode**–[Rounding Mode Parameter](https://docs.nvidia.com/introduction.html#general_conventions_lb_1rounding_mode_parameter).**nScaleFactor**–[Integer Result Scaling](https://docs.nvidia.com/introduction.html#general_conventions_lb_1integer_result_scaling).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsConvert_32f32s_Sfs_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc,[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pDst, size_t nLength,[NppRoundMode](https://docs.nvidia.com/nppdefs.html#c.NppRoundMode)eRoundMode, int nScaleFactor,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsConvert_32f32s_Sfs_Ctx)

-
32-bit floating point number to 32-bit signed integer conversion with scaling

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**eRoundMode**–[Rounding Mode Parameter](https://docs.nvidia.com/introduction.html#general_conventions_lb_1rounding_mode_parameter).**nScaleFactor**–[Integer Result Scaling](https://docs.nvidia.com/introduction.html#general_conventions_lb_1integer_result_scaling).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsConvert_64s32s_Sfs_Ctx(const[Npp64s](https://docs.nvidia.com/nppdefs.html#c.Npp64s)*pSrc,[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pDst, size_t nLength,[NppRoundMode](https://docs.nvidia.com/nppdefs.html#c.NppRoundMode)eRoundMode, int nScaleFactor,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsConvert_64s32s_Sfs_Ctx)

-
64-bit signed integer to 32-bit signed integer conversion with scaling

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**eRoundMode**–[Rounding Mode Parameter](https://docs.nvidia.com/introduction.html#general_conventions_lb_1rounding_mode_parameter).**nScaleFactor**–[Integer Result Scaling](https://docs.nvidia.com/introduction.html#general_conventions_lb_1integer_result_scaling).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsConvert_64f16s_Sfs_Ctx(const[Npp64f](https://docs.nvidia.com/nppdefs.html#c.Npp64f)*pSrc,[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pDst, size_t nLength,[NppRoundMode](https://docs.nvidia.com/nppdefs.html#c.NppRoundMode)eRoundMode, int nScaleFactor,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsConvert_64f16s_Sfs_Ctx)

-
64-bit floating point number to 16-bit signed short conversion with scaling

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**eRoundMode**–[Rounding Mode Parameter](https://docs.nvidia.com/introduction.html#general_conventions_lb_1rounding_mode_parameter).**nScaleFactor**–[Integer Result Scaling](https://docs.nvidia.com/introduction.html#general_conventions_lb_1integer_result_scaling).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsConvert_64f32s_Sfs_Ctx(const[Npp64f](https://docs.nvidia.com/nppdefs.html#c.Npp64f)*pSrc,[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pDst, size_t nLength,[NppRoundMode](https://docs.nvidia.com/nppdefs.html#c.NppRoundMode)eRoundMode, int nScaleFactor,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsConvert_64f32s_Sfs_Ctx)

-
64-bit floating point number to 32-bit signed integer conversion with scaling

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**eRoundMode**–[Rounding Mode Parameter](https://docs.nvidia.com/introduction.html#general_conventions_lb_1rounding_mode_parameter).**nScaleFactor**–[Integer Result Scaling](https://docs.nvidia.com/introduction.html#general_conventions_lb_1integer_result_scaling).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsConvert_64f64s_Sfs_Ctx(const[Npp64f](https://docs.nvidia.com/nppdefs.html#c.Npp64f)*pSrc,[Npp64s](https://docs.nvidia.com/nppdefs.html#c.Npp64s)*pDst, size_t nLength,[NppRoundMode](https://docs.nvidia.com/nppdefs.html#c.NppRoundMode)eRoundMode, int nScaleFactor,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsConvert_64f64s_Sfs_Ctx)

-
64-bit floating point number to 64-bit signed integer conversion with scaling

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**eRoundMode**–[Rounding Mode Parameter](https://docs.nvidia.com/introduction.html#general_conventions_lb_1rounding_mode_parameter).**nScaleFactor**–[Integer Result Scaling](https://docs.nvidia.com/introduction.html#general_conventions_lb_1integer_result_scaling).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


## Signal Threshold[](https://docs.nvidia.com#signal-threshold)

### Threshold[](https://docs.nvidia.com#group__signal__threshold_1signal_threshold)

The set of threshold operations available in the library.

Threshold Functions

Performs the threshold operation on the samples of a signal by limiting the sample values by a specified constant value.

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsThreshold_16s_Ctx(const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrc,[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pDst, size_t nLength,[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)nLevel,[NppCmpOp](https://docs.nvidia.com/nppdefs.html#c.NppCmpOp)nRelOp,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsThreshold_16s_Ctx)

-
16-bit signed short signal threshold with constant level.

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nLevel**– Constant threshold value to be used to limit each signal sample**nRelOp**– NppCmpOp type of thresholding operation (NPP_CMP_LESS or NPP_CMP_GREATER only).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsThreshold_16s_I_Ctx([Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrcDst, size_t nLength,[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)nLevel,[NppCmpOp](https://docs.nvidia.com/nppdefs.html#c.NppCmpOp)nRelOp,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsThreshold_16s_I_Ctx)

-
16-bit in place signed short signal threshold with constant level.

- Parameters
-
**pSrcDst**–[In-Place Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1in_place_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nLevel**– Constant threshold value to be used to limit each signal sample**nRelOp**– NppCmpOp type of thresholding operation (NPP_CMP_LESS or NPP_CMP_GREATER only).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsThreshold_16sc_Ctx(const[Npp16sc](https://docs.nvidia.com/nppdefs.html#c.Npp16sc)*pSrc,[Npp16sc](https://docs.nvidia.com/nppdefs.html#c.Npp16sc)*pDst, size_t nLength,[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)nLevel,[NppCmpOp](https://docs.nvidia.com/nppdefs.html#c.NppCmpOp)nRelOp,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsThreshold_16sc_Ctx)

-
16-bit signed short complex number signal threshold with constant level.

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nLevel**– Constant threshold value (real part only and must be greater than 0) to be used to limit each signal sample**nRelOp**– NppCmpOp type of thresholding operation (NPP_CMP_LESS or NPP_CMP_GREATER only).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsThreshold_16sc_I_Ctx([Npp16sc](https://docs.nvidia.com/nppdefs.html#c.Npp16sc)*pSrcDst, size_t nLength,[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)nLevel,[NppCmpOp](https://docs.nvidia.com/nppdefs.html#c.NppCmpOp)nRelOp,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsThreshold_16sc_I_Ctx)

-
16-bit in place signed short complex number signal threshold with constant level.

- Parameters
-
**pSrcDst**–[In-Place Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1in_place_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nLevel**– Constant threshold value (real part only and must be greater than 0) to be used to limit each signal sample**nRelOp**– NppCmpOp type of thresholding operation (NPP_CMP_LESS or NPP_CMP_GREATER only).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsThreshold_32f_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pDst, size_t nLength,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)nLevel,[NppCmpOp](https://docs.nvidia.com/nppdefs.html#c.NppCmpOp)nRelOp,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsThreshold_32f_Ctx)

-
32-bit floating point signal threshold with constant level.

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nLevel**– Constant threshold value to be used to limit each signal sample**nRelOp**– NppCmpOp type of thresholding operation (NPP_CMP_LESS or NPP_CMP_GREATER only).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsThreshold_32f_I_Ctx([Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrcDst, size_t nLength,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)nLevel,[NppCmpOp](https://docs.nvidia.com/nppdefs.html#c.NppCmpOp)nRelOp,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsThreshold_32f_I_Ctx)

-
32-bit in place floating point signal threshold with constant level.

- Parameters
-
**pSrcDst**–[In-Place Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1in_place_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nLevel**– Constant threshold value to be used to limit each signal sample**nRelOp**– NppCmpOp type of thresholding operation (NPP_CMP_LESS or NPP_CMP_GREATER only).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsThreshold_32fc_Ctx(const[Npp32fc](https://docs.nvidia.com/nppdefs.html#c.Npp32fc)*pSrc,[Npp32fc](https://docs.nvidia.com/nppdefs.html#c.Npp32fc)*pDst, size_t nLength,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)nLevel,[NppCmpOp](https://docs.nvidia.com/nppdefs.html#c.NppCmpOp)nRelOp,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsThreshold_32fc_Ctx)

-
32-bit floating point complex number signal threshold with constant level.

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nLevel**– Constant threshold value (real part only and must be greater than 0) to be used to limit each signal sample**nRelOp**– NppCmpOp type of thresholding operation (NPP_CMP_LESS or NPP_CMP_GREATER only).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsThreshold_32fc_I_Ctx([Npp32fc](https://docs.nvidia.com/nppdefs.html#c.Npp32fc)*pSrcDst, size_t nLength,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)nLevel,[NppCmpOp](https://docs.nvidia.com/nppdefs.html#c.NppCmpOp)nRelOp,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsThreshold_32fc_I_Ctx)

-
32-bit in place floating point complex number signal threshold with constant level.

- Parameters
-
**pSrcDst**–[In-Place Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1in_place_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nLevel**– Constant threshold value (real part only and must be greater than 0) to be used to limit each signal sample**nRelOp**– NppCmpOp type of thresholding operation (NPP_CMP_LESS or NPP_CMP_GREATER only).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsThreshold_64f_Ctx(const[Npp64f](https://docs.nvidia.com/nppdefs.html#c.Npp64f)*pSrc,[Npp64f](https://docs.nvidia.com/nppdefs.html#c.Npp64f)*pDst, size_t nLength,[Npp64f](https://docs.nvidia.com/nppdefs.html#c.Npp64f)nLevel,[NppCmpOp](https://docs.nvidia.com/nppdefs.html#c.NppCmpOp)nRelOp,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsThreshold_64f_Ctx)

-
64-bit floating point signal threshold with constant level.

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nLevel**– Constant threshold value to be used to limit each signal sample**nRelOp**– NppCmpOp type of thresholding operation (NPP_CMP_LESS or NPP_CMP_GREATER only).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsThreshold_64f_I_Ctx([Npp64f](https://docs.nvidia.com/nppdefs.html#c.Npp64f)*pSrcDst, size_t nLength,[Npp64f](https://docs.nvidia.com/nppdefs.html#c.Npp64f)nLevel,[NppCmpOp](https://docs.nvidia.com/nppdefs.html#c.NppCmpOp)nRelOp,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsThreshold_64f_I_Ctx)

-
64-bit in place floating point signal threshold with constant level.

- Parameters
-
**pSrcDst**–[In-Place Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1in_place_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nLevel**– Constant threshold value to be used to limit each signal sample**nRelOp**– NppCmpOp type of thresholding operation (NPP_CMP_LESS or NPP_CMP_GREATER only).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsThreshold_64fc_Ctx(const[Npp64fc](https://docs.nvidia.com/nppdefs.html#c.Npp64fc)*pSrc,[Npp64fc](https://docs.nvidia.com/nppdefs.html#c.Npp64fc)*pDst, size_t nLength,[Npp64f](https://docs.nvidia.com/nppdefs.html#c.Npp64f)nLevel,[NppCmpOp](https://docs.nvidia.com/nppdefs.html#c.NppCmpOp)nRelOp,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsThreshold_64fc_Ctx)

-
64-bit floating point complex number signal threshold with constant level.

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nLevel**– Constant threshold value (real part only and must be greater than 0) to be used to limit each signal sample**nRelOp**– NppCmpOp type of thresholding operation (NPP_CMP_LESS or NPP_CMP_GREATER only).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsThreshold_64fc_I_Ctx([Npp64fc](https://docs.nvidia.com/nppdefs.html#c.Npp64fc)*pSrcDst, size_t nLength,[Npp64f](https://docs.nvidia.com/nppdefs.html#c.Npp64f)nLevel,[NppCmpOp](https://docs.nvidia.com/nppdefs.html#c.NppCmpOp)nRelOp,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsThreshold_64fc_I_Ctx)

-
64-bit in place floating point complex number signal threshold with constant level.

- Parameters
-
**pSrcDst**–[In-Place Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1in_place_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nLevel**– Constant threshold value (real part only and must be greater than 0) to be used to limit each signal sample**nRelOp**– NppCmpOp type of thresholding operation (NPP_CMP_LESS or NPP_CMP_GREATER only).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsThreshold_LT_16s_Ctx(const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrc,[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pDst, size_t nLength,[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)nLevel,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsThreshold_LT_16s_Ctx)

-
16-bit signed short signal NPP_CMP_LESS threshold with constant level.

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nLevel**– Constant threshold value to be used to limit each signal sample**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsThreshold_LT_16s_I_Ctx([Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrcDst, size_t nLength,[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)nLevel,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsThreshold_LT_16s_I_Ctx)

-
16-bit in place signed short signal NPP_CMP_LESS threshold with constant level.

- Parameters
-
**pSrcDst**–[In-Place Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1in_place_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nLevel**– Constant threshold value to be used to limit each signal sample**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsThreshold_LT_16sc_Ctx(const[Npp16sc](https://docs.nvidia.com/nppdefs.html#c.Npp16sc)*pSrc,[Npp16sc](https://docs.nvidia.com/nppdefs.html#c.Npp16sc)*pDst, size_t nLength,[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)nLevel,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsThreshold_LT_16sc_Ctx)

-
16-bit signed short complex number signal NPP_CMP_LESS threshold with constant level.

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nLevel**– Constant threshold value (real part only and must be greater than 0) to be used to limit each signal sample**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsThreshold_LT_16sc_I_Ctx([Npp16sc](https://docs.nvidia.com/nppdefs.html#c.Npp16sc)*pSrcDst, size_t nLength,[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)nLevel,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsThreshold_LT_16sc_I_Ctx)

-
16-bit in place signed short complex number signal NPP_CMP_LESS threshold with constant level.

- Parameters
-
**pSrcDst**–[In-Place Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1in_place_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nLevel**– Constant threshold value (real part only and must be greater than 0) to be used to limit each signal sample**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsThreshold_LT_32f_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pDst, size_t nLength,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)nLevel,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsThreshold_LT_32f_Ctx)

-
32-bit floating point signal NPP_CMP_LESS threshold with constant level.

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nLevel**– Constant threshold value to be used to limit each signal sample**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsThreshold_LT_32f_I_Ctx([Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrcDst, size_t nLength,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)nLevel,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsThreshold_LT_32f_I_Ctx)

-
32-bit in place floating point signal NPP_CMP_LESS threshold with constant level.

- Parameters
-
**pSrcDst**–[In-Place Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1in_place_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nLevel**– Constant threshold value to be used to limit each signal sample**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsThreshold_LT_32fc_Ctx(const[Npp32fc](https://docs.nvidia.com/nppdefs.html#c.Npp32fc)*pSrc,[Npp32fc](https://docs.nvidia.com/nppdefs.html#c.Npp32fc)*pDst, size_t nLength,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)nLevel,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsThreshold_LT_32fc_Ctx)

-
32-bit floating point complex number signal NPP_CMP_LESS threshold with constant level.

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nLevel**– Constant threshold value (real part only and must be greater than 0) to be used to limit each signal sample**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsThreshold_LT_32fc_I_Ctx([Npp32fc](https://docs.nvidia.com/nppdefs.html#c.Npp32fc)*pSrcDst, size_t nLength,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)nLevel,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsThreshold_LT_32fc_I_Ctx)

-
32-bit in place floating point complex number signal NPP_CMP_LESS threshold with constant level.

- Parameters
-
**pSrcDst**–[In-Place Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1in_place_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nLevel**– Constant threshold value (real part only and must be greater than 0) to be used to limit each signal sample**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsThreshold_LT_64f_Ctx(const[Npp64f](https://docs.nvidia.com/nppdefs.html#c.Npp64f)*pSrc,[Npp64f](https://docs.nvidia.com/nppdefs.html#c.Npp64f)*pDst, size_t nLength,[Npp64f](https://docs.nvidia.com/nppdefs.html#c.Npp64f)nLevel,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsThreshold_LT_64f_Ctx)

-
64-bit floating point signal NPP_CMP_LESS threshold with constant level.

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nLevel**– Constant threshold value to be used to limit each signal sample**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsThreshold_LT_64f_I_Ctx([Npp64f](https://docs.nvidia.com/nppdefs.html#c.Npp64f)*pSrcDst, size_t nLength,[Npp64f](https://docs.nvidia.com/nppdefs.html#c.Npp64f)nLevel,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsThreshold_LT_64f_I_Ctx)

-
64-bit in place floating point signal NPP_CMP_LESS threshold with constant level.

- Parameters
-
**pSrcDst**–[In-Place Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1in_place_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nLevel**– Constant threshold value to be used to limit each signal sample**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsThreshold_LT_64fc_Ctx(const[Npp64fc](https://docs.nvidia.com/nppdefs.html#c.Npp64fc)*pSrc,[Npp64fc](https://docs.nvidia.com/nppdefs.html#c.Npp64fc)*pDst, size_t nLength,[Npp64f](https://docs.nvidia.com/nppdefs.html#c.Npp64f)nLevel,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsThreshold_LT_64fc_Ctx)

-
64-bit floating point complex number signal NPP_CMP_LESS threshold with constant level.

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nLevel**– Constant threshold value (real part only and must be greater than 0) to be used to limit each signal sample**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsThreshold_LT_64fc_I_Ctx([Npp64fc](https://docs.nvidia.com/nppdefs.html#c.Npp64fc)*pSrcDst, size_t nLength,[Npp64f](https://docs.nvidia.com/nppdefs.html#c.Npp64f)nLevel,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsThreshold_LT_64fc_I_Ctx)

-
64-bit in place floating point complex number signal NPP_CMP_LESS threshold with constant level.

- Parameters
-
**pSrcDst**–[In-Place Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1in_place_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nLevel**– Constant threshold value (real part only and must be greater than 0) to be used to limit each signal sample**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsThreshold_GT_16s_Ctx(const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrc,[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pDst, size_t nLength,[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)nLevel,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsThreshold_GT_16s_Ctx)

-
16-bit signed short signal NPP_CMP_GREATER threshold with constant level.

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nLevel**– Constant threshold value to be used to limit each signal sample**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsThreshold_GT_16s_I_Ctx([Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrcDst, size_t nLength,[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)nLevel,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsThreshold_GT_16s_I_Ctx)

-
16-bit in place signed short signal NPP_CMP_GREATER threshold with constant level.

- Parameters
-
**pSrcDst**–[In-Place Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1in_place_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nLevel**– Constant threshold value to be used to limit each signal sample**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsThreshold_GT_16sc_Ctx(const[Npp16sc](https://docs.nvidia.com/nppdefs.html#c.Npp16sc)*pSrc,[Npp16sc](https://docs.nvidia.com/nppdefs.html#c.Npp16sc)*pDst, size_t nLength,[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)nLevel,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsThreshold_GT_16sc_Ctx)

-
16-bit signed short complex number signal NPP_CMP_GREATER threshold with constant level.

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nLevel**– Constant threshold value (real part only and must be greater than 0) to be used to limit each signal sample**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsThreshold_GT_16sc_I_Ctx([Npp16sc](https://docs.nvidia.com/nppdefs.html#c.Npp16sc)*pSrcDst, size_t nLength,[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)nLevel,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsThreshold_GT_16sc_I_Ctx)

-
16-bit in place signed short complex number signal NPP_CMP_GREATER threshold with constant level.

- Parameters
-
**pSrcDst**–[In-Place Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1in_place_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nLevel**– Constant threshold value (real part only and must be greater than 0) to be used to limit each signal sample**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsThreshold_GT_32f_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pDst, size_t nLength,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)nLevel,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsThreshold_GT_32f_Ctx)

-
32-bit floating point signal NPP_CMP_GREATER threshold with constant level.

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nLevel**– Constant threshold value to be used to limit each signal sample**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsThreshold_GT_32f_I_Ctx([Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrcDst, size_t nLength,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)nLevel,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsThreshold_GT_32f_I_Ctx)

-
32-bit in place floating point signal NPP_CMP_GREATER threshold with constant level.

- Parameters
-
**pSrcDst**–[In-Place Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1in_place_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nLevel**– Constant threshold value to be used to limit each signal sample**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsThreshold_GT_32fc_Ctx(const[Npp32fc](https://docs.nvidia.com/nppdefs.html#c.Npp32fc)*pSrc,[Npp32fc](https://docs.nvidia.com/nppdefs.html#c.Npp32fc)*pDst, size_t nLength,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)nLevel,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsThreshold_GT_32fc_Ctx)

-
32-bit floating point complex number signal NPP_CMP_GREATER threshold with constant level.

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nLevel**– Constant threshold value (real part only and must be greater than 0) to be used to limit each signal sample**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsThreshold_GT_32fc_I_Ctx([Npp32fc](https://docs.nvidia.com/nppdefs.html#c.Npp32fc)*pSrcDst, size_t nLength,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)nLevel,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsThreshold_GT_32fc_I_Ctx)

-
32-bit in place floating point complex number signal NPP_CMP_GREATER threshold with constant level.

- Parameters
-
**pSrcDst**–[In-Place Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1in_place_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nLevel**– Constant threshold value (real part only and must be greater than 0) to be used to limit each signal sample**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsThreshold_GT_64f_Ctx(const[Npp64f](https://docs.nvidia.com/nppdefs.html#c.Npp64f)*pSrc,[Npp64f](https://docs.nvidia.com/nppdefs.html#c.Npp64f)*pDst, size_t nLength,[Npp64f](https://docs.nvidia.com/nppdefs.html#c.Npp64f)nLevel,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsThreshold_GT_64f_Ctx)

-
64-bit floating point signal NPP_CMP_GREATER threshold with constant level.

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nLevel**– Constant threshold value to be used to limit each signal sample**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsThreshold_GT_64f_I_Ctx([Npp64f](https://docs.nvidia.com/nppdefs.html#c.Npp64f)*pSrcDst, size_t nLength,[Npp64f](https://docs.nvidia.com/nppdefs.html#c.Npp64f)nLevel,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsThreshold_GT_64f_I_Ctx)

-
64-bit in place floating point signal NPP_CMP_GREATER threshold with constant level.

- Parameters
-
**pSrcDst**–[In-Place Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1in_place_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nLevel**– Constant threshold value to be used to limit each signal sample**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsThreshold_GT_64fc_Ctx(const[Npp64fc](https://docs.nvidia.com/nppdefs.html#c.Npp64fc)*pSrc,[Npp64fc](https://docs.nvidia.com/nppdefs.html#c.Npp64fc)*pDst, size_t nLength,[Npp64f](https://docs.nvidia.com/nppdefs.html#c.Npp64f)nLevel,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsThreshold_GT_64fc_Ctx)

-
64-bit floating point complex number signal NPP_CMP_GREATER threshold with constant level.

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nLevel**– Constant threshold value (real part only and must be greater than 0) to be used to limit each signal sample**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsThreshold_GT_64fc_I_Ctx([Npp64fc](https://docs.nvidia.com/nppdefs.html#c.Npp64fc)*pSrcDst, size_t nLength,[Npp64f](https://docs.nvidia.com/nppdefs.html#c.Npp64f)nLevel,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsThreshold_GT_64fc_I_Ctx)

-
64-bit in place floating point complex number signal NPP_CMP_GREATER threshold with constant level.

- Parameters
-
**pSrcDst**–[In-Place Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1in_place_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nLevel**– Constant threshold value (real part only and must be greater than 0) to be used to limit each signal sample**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsThreshold_LTVal_16s_Ctx(const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrc,[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pDst, size_t nLength,[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)nLevel,[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)nValue,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsThreshold_LTVal_16s_Ctx)

-
16-bit signed short signal NPP_CMP_LESS threshold with constant level.

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nLevel**– Constant threshold value to be used to limit each signal sample**nValue**– Constant value to replace source value when threshold test is true.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsThreshold_LTVal_16s_I_Ctx([Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrcDst, size_t nLength,[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)nLevel,[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)nValue,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsThreshold_LTVal_16s_I_Ctx)

-
16-bit in place signed short signal NPP_CMP_LESS threshold with constant level.

- Parameters
-
**pSrcDst**–[In-Place Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1in_place_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nLevel**– Constant threshold value to be used to limit each signal sample**nValue**– Constant value to replace source value when threshold test is true.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsThreshold_LTVal_16sc_Ctx(const[Npp16sc](https://docs.nvidia.com/nppdefs.html#c.Npp16sc)*pSrc,[Npp16sc](https://docs.nvidia.com/nppdefs.html#c.Npp16sc)*pDst, size_t nLength,[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)nLevel,[Npp16sc](https://docs.nvidia.com/nppdefs.html#c.Npp16sc)nValue,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsThreshold_LTVal_16sc_Ctx)

-
16-bit signed short complex number signal NPP_CMP_LESS threshold with constant level.

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nLevel**– Constant threshold value (real part only and must be greater than 0) to be used to limit each signal sample**nValue**– Constant value to replace source value when threshold test is true.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsThreshold_LTVal_16sc_I_Ctx([Npp16sc](https://docs.nvidia.com/nppdefs.html#c.Npp16sc)*pSrcDst, size_t nLength,[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)nLevel,[Npp16sc](https://docs.nvidia.com/nppdefs.html#c.Npp16sc)nValue,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsThreshold_LTVal_16sc_I_Ctx)

-
16-bit in place signed short complex number signal NPP_CMP_LESS threshold with constant level.

- Parameters
-
**pSrcDst**–[In-Place Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1in_place_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nLevel**– Constant threshold value (real part only and must be greater than 0) to be used to limit each signal sample**nValue**– Constant value to replace source value when threshold test is true.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsThreshold_LTVal_32f_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pDst, size_t nLength,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)nLevel,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)nValue,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsThreshold_LTVal_32f_Ctx)

-
32-bit floating point signal NPP_CMP_LESS threshold with constant level.

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nLevel**– Constant threshold value to be used to limit each signal sample**nValue**– Constant value to replace source value when threshold test is true.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsThreshold_LTVal_32f_I_Ctx([Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrcDst, size_t nLength,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)nLevel,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)nValue,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsThreshold_LTVal_32f_I_Ctx)

-
32-bit in place floating point signal NPP_CMP_LESS threshold with constant level.

- Parameters
-
**pSrcDst**–[In-Place Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1in_place_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nLevel**– Constant threshold value to be used to limit each signal sample**nValue**– Constant value to replace source value when threshold test is true.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsThreshold_LTVal_32fc_Ctx(const[Npp32fc](https://docs.nvidia.com/nppdefs.html#c.Npp32fc)*pSrc,[Npp32fc](https://docs.nvidia.com/nppdefs.html#c.Npp32fc)*pDst, size_t nLength,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)nLevel,[Npp32fc](https://docs.nvidia.com/nppdefs.html#c.Npp32fc)nValue,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsThreshold_LTVal_32fc_Ctx)

-
32-bit floating point complex number signal NPP_CMP_LESS threshold with constant level.

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nLevel**– Constant threshold value (real part only and must be greater than 0) to be used to limit each signal sample**nValue**– Constant value to replace source value when threshold test is true.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsThreshold_LTVal_32fc_I_Ctx([Npp32fc](https://docs.nvidia.com/nppdefs.html#c.Npp32fc)*pSrcDst, size_t nLength,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)nLevel,[Npp32fc](https://docs.nvidia.com/nppdefs.html#c.Npp32fc)nValue,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsThreshold_LTVal_32fc_I_Ctx)

-
32-bit in place floating point complex number signal NPP_CMP_LESS threshold with constant level.

- Parameters
-
**pSrcDst**–[In-Place Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1in_place_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nLevel**– Constant threshold value (real part only and must be greater than 0) to be used to limit each signal sample**nValue**– Constant value to replace source value when threshold test is true.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsThreshold_LTVal_64f_Ctx(const[Npp64f](https://docs.nvidia.com/nppdefs.html#c.Npp64f)*pSrc,[Npp64f](https://docs.nvidia.com/nppdefs.html#c.Npp64f)*pDst, size_t nLength,[Npp64f](https://docs.nvidia.com/nppdefs.html#c.Npp64f)nLevel,[Npp64f](https://docs.nvidia.com/nppdefs.html#c.Npp64f)nValue,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsThreshold_LTVal_64f_Ctx)

-
64-bit floating point signal NPP_CMP_LESS threshold with constant level.

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nLevel**– Constant threshold value to be used to limit each signal sample**nValue**– Constant value to replace source value when threshold test is true.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsThreshold_LTVal_64f_I_Ctx([Npp64f](https://docs.nvidia.com/nppdefs.html#c.Npp64f)*pSrcDst, size_t nLength,[Npp64f](https://docs.nvidia.com/nppdefs.html#c.Npp64f)nLevel,[Npp64f](https://docs.nvidia.com/nppdefs.html#c.Npp64f)nValue,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsThreshold_LTVal_64f_I_Ctx)

-
64-bit in place floating point signal NPP_CMP_LESS threshold with constant level.

- Parameters
-
**pSrcDst**–[In-Place Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1in_place_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nLevel**– Constant threshold value to be used to limit each signal sample**nValue**– Constant value to replace source value when threshold test is true.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsThreshold_LTVal_64fc_Ctx(const[Npp64fc](https://docs.nvidia.com/nppdefs.html#c.Npp64fc)*pSrc,[Npp64fc](https://docs.nvidia.com/nppdefs.html#c.Npp64fc)*pDst, size_t nLength,[Npp64f](https://docs.nvidia.com/nppdefs.html#c.Npp64f)nLevel,[Npp64fc](https://docs.nvidia.com/nppdefs.html#c.Npp64fc)nValue,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsThreshold_LTVal_64fc_Ctx)

-
64-bit floating point complex number signal NPP_CMP_LESS threshold with constant level.

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nLevel**– Constant threshold value (real part only and must be greater than 0) to be used to limit each signal sample**nValue**– Constant value to replace source value when threshold test is true.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsThreshold_LTVal_64fc_I_Ctx([Npp64fc](https://docs.nvidia.com/nppdefs.html#c.Npp64fc)*pSrcDst, size_t nLength,[Npp64f](https://docs.nvidia.com/nppdefs.html#c.Npp64f)nLevel,[Npp64fc](https://docs.nvidia.com/nppdefs.html#c.Npp64fc)nValue,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsThreshold_LTVal_64fc_I_Ctx)

-
64-bit in place floating point complex number signal NPP_CMP_LESS threshold with constant level.

- Parameters
-
**pSrcDst**–[In-Place Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1in_place_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nLevel**– Constant threshold value (real part only and must be greater than 0) to be used to limit each signal sample**nValue**– Constant value to replace source value when threshold test is true.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsThreshold_GTVal_16s_Ctx(const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrc,[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pDst, size_t nLength,[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)nLevel,[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)nValue,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsThreshold_GTVal_16s_Ctx)

-
16-bit signed short signal NPP_CMP_GREATER threshold with constant level.

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nLevel**– Constant threshold value to be used to limit each signal sample**nValue**– Constant value to replace source value when threshold test is true.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsThreshold_GTVal_16s_I_Ctx([Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrcDst, size_t nLength,[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)nLevel,[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)nValue,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsThreshold_GTVal_16s_I_Ctx)

-
16-bit in place signed short signal NPP_CMP_GREATER threshold with constant level.

- Parameters
-
**pSrcDst**–[In-Place Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1in_place_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nLevel**– Constant threshold value to be used to limit each signal sample**nValue**– Constant value to replace source value when threshold test is true.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsThreshold_GTVal_16sc_Ctx(const[Npp16sc](https://docs.nvidia.com/nppdefs.html#c.Npp16sc)*pSrc,[Npp16sc](https://docs.nvidia.com/nppdefs.html#c.Npp16sc)*pDst, size_t nLength,[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)nLevel,[Npp16sc](https://docs.nvidia.com/nppdefs.html#c.Npp16sc)nValue,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsThreshold_GTVal_16sc_Ctx)

-
16-bit signed short complex number signal NPP_CMP_GREATER threshold with constant level.

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nLevel**– Constant threshold value (real part only and must be greater than 0) to be used to limit each signal sample**nValue**– Constant value to replace source value when threshold test is true.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsThreshold_GTVal_16sc_I_Ctx([Npp16sc](https://docs.nvidia.com/nppdefs.html#c.Npp16sc)*pSrcDst, size_t nLength,[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)nLevel,[Npp16sc](https://docs.nvidia.com/nppdefs.html#c.Npp16sc)nValue,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsThreshold_GTVal_16sc_I_Ctx)

-
16-bit in place signed short complex number signal NPP_CMP_GREATER threshold with constant level.

- Parameters
-
**pSrcDst**–[In-Place Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1in_place_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nLevel**– Constant threshold value (real part only and must be greater than 0) to be used to limit each signal sample**nValue**– Constant value to replace source value when threshold test is true.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsThreshold_GTVal_32f_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pDst, size_t nLength,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)nLevel,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)nValue,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsThreshold_GTVal_32f_Ctx)

-
32-bit floating point signal NPP_CMP_GREATER threshold with constant level.

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nLevel**– Constant threshold value to be used to limit each signal sample**nValue**– Constant value to replace source value when threshold test is true.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsThreshold_GTVal_32f_I_Ctx([Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrcDst, size_t nLength,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)nLevel,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)nValue,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsThreshold_GTVal_32f_I_Ctx)

-
32-bit in place floating point signal NPP_CMP_GREATER threshold with constant level.

- Parameters
-
**pSrcDst**–[In-Place Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1in_place_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nLevel**– Constant threshold value to be used to limit each signal sample**nValue**– Constant value to replace source value when threshold test is true.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsThreshold_GTVal_32fc_Ctx(const[Npp32fc](https://docs.nvidia.com/nppdefs.html#c.Npp32fc)*pSrc,[Npp32fc](https://docs.nvidia.com/nppdefs.html#c.Npp32fc)*pDst, size_t nLength,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)nLevel,[Npp32fc](https://docs.nvidia.com/nppdefs.html#c.Npp32fc)nValue,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsThreshold_GTVal_32fc_Ctx)

-
32-bit floating point complex number signal NPP_CMP_GREATER threshold with constant level.

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nLevel**– Constant threshold value (real part only and must be greater than 0) to be used to limit each signal sample**nValue**– Constant value to replace source value when threshold test is true.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsThreshold_GTVal_32fc_I_Ctx([Npp32fc](https://docs.nvidia.com/nppdefs.html#c.Npp32fc)*pSrcDst, size_t nLength,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)nLevel,[Npp32fc](https://docs.nvidia.com/nppdefs.html#c.Npp32fc)nValue,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsThreshold_GTVal_32fc_I_Ctx)

-
32-bit in place floating point complex number signal NPP_CMP_GREATER threshold with constant level.

- Parameters
-
**pSrcDst**–[In-Place Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1in_place_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nLevel**– Constant threshold value (real part only and must be greater than 0) to be used to limit each signal sample**nValue**– Constant value to replace source value when threshold test is true.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsThreshold_GTVal_64f_Ctx(const[Npp64f](https://docs.nvidia.com/nppdefs.html#c.Npp64f)*pSrc,[Npp64f](https://docs.nvidia.com/nppdefs.html#c.Npp64f)*pDst, size_t nLength,[Npp64f](https://docs.nvidia.com/nppdefs.html#c.Npp64f)nLevel,[Npp64f](https://docs.nvidia.com/nppdefs.html#c.Npp64f)nValue,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsThreshold_GTVal_64f_Ctx)

-
64-bit floating point signal NPP_CMP_GREATER threshold with constant level.

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nLevel**– Constant threshold value to be used to limit each signal sample**nValue**– Constant value to replace source value when threshold test is true.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsThreshold_GTVal_64f_I_Ctx([Npp64f](https://docs.nvidia.com/nppdefs.html#c.Npp64f)*pSrcDst, size_t nLength,[Npp64f](https://docs.nvidia.com/nppdefs.html#c.Npp64f)nLevel,[Npp64f](https://docs.nvidia.com/nppdefs.html#c.Npp64f)nValue,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsThreshold_GTVal_64f_I_Ctx)

-
64-bit in place floating point signal NPP_CMP_GREATER threshold with constant level.

- Parameters
-
**pSrcDst**–[In-Place Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1in_place_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nLevel**– Constant threshold value to be used to limit each signal sample**nValue**– Constant value to replace source value when threshold test is true.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsThreshold_GTVal_64fc_Ctx(const[Npp64fc](https://docs.nvidia.com/nppdefs.html#c.Npp64fc)*pSrc,[Npp64fc](https://docs.nvidia.com/nppdefs.html#c.Npp64fc)*pDst, size_t nLength,[Npp64f](https://docs.nvidia.com/nppdefs.html#c.Npp64f)nLevel,[Npp64fc](https://docs.nvidia.com/nppdefs.html#c.Npp64fc)nValue,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsThreshold_GTVal_64fc_Ctx)

-
64-bit floating point complex number signal NPP_CMP_GREATER threshold with constant level.

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nLevel**– Constant threshold value (real part only and must be greater than 0) to be used to limit each signal sample**nValue**– Constant value to replace source value when threshold test is true.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsThreshold_GTVal_64fc_I_Ctx([Npp64fc](https://docs.nvidia.com/nppdefs.html#c.Npp64fc)*pSrcDst, size_t nLength,[Npp64f](https://docs.nvidia.com/nppdefs.html#c.Npp64f)nLevel,[Npp64fc](https://docs.nvidia.com/nppdefs.html#c.Npp64fc)nValue,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsThreshold_GTVal_64fc_I_Ctx)

-
64-bit in place floating point complex number signal NPP_CMP_GREATER threshold with constant level.

- Parameters
-
**pSrcDst**–[In-Place Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1in_place_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nLevel**– Constant threshold value (real part only and must be greater than 0) to be used to limit each signal sample**nValue**– Constant value to replace source value when threshold test is true.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).