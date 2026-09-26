source: https://docs.nvidia.com/cuda/npp/signal_arithmetic_and_logical_operations.html

# Signal Arithmetic And Logical Operations[](https://docs.nvidia.com#signal-arithmetic-and-logical-operations)

Functions that provide common arithmetic and logical operations.

## Signal Arithmetic Functions[](https://docs.nvidia.com#signal-arithmetic-functions)

### Arithmetic Operations[](https://docs.nvidia.com#group__signal__arithmetic_1signal_arithmetic)

The set of arithmetic operations for signal processing available in the library.

### Signal AddC[](https://docs.nvidia.com#signal-addc)

#### AddC[](https://docs.nvidia.com#group__signal__addc_1signal_addc)

Adds a constant value to each sample of a signal.

Functions

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsAddC_8u_ISfs_Ctx([Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)nValue,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrcDst, size_t nLength, int nScaleFactor,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsAddC_8u_ISfs_Ctx)

-
8-bit unsigned char in place signal add constant, scale, then clamp to saturated value

- Parameters
-
**pSrcDst**–[In-Place Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1in_place_signal_pointer).**nValue**– Constant value to be added to each vector element**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nScaleFactor**–[Integer Result Scaling](https://docs.nvidia.com/introduction.html#general_conventions_lb_1integer_result_scaling).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsAddC_8u_Sfs_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)nValue,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, size_t nLength, int nScaleFactor,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsAddC_8u_Sfs_Ctx)

-
8-bit unsigned charvector add constant, scale, then clamp to saturated value.

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nValue**– Constant value to be added to each vector element**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nScaleFactor**–[Integer Result Scaling](https://docs.nvidia.com/introduction.html#general_conventions_lb_1integer_result_scaling).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsAddC_16u_ISfs_Ctx([Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)nValue,[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrcDst, size_t nLength, int nScaleFactor,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsAddC_16u_ISfs_Ctx)

-
16-bit unsigned short in place signal add constant, scale, then clamp to saturated value.

- Parameters
-
**pSrcDst**–[In-Place Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1in_place_signal_pointer).**nValue**– Constant value to be added to each vector element**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nScaleFactor**–[Integer Result Scaling](https://docs.nvidia.com/introduction.html#general_conventions_lb_1integer_result_scaling).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsAddC_16u_Sfs_Ctx(const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrc,[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)nValue,[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pDst, size_t nLength, int nScaleFactor,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsAddC_16u_Sfs_Ctx)

-
16-bit unsigned short vector add constant, scale, then clamp to saturated value.

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nValue**– Constant value to be added to each vector element**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nScaleFactor**–[Integer Result Scaling](https://docs.nvidia.com/introduction.html#general_conventions_lb_1integer_result_scaling).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsAddC_16s_ISfs_Ctx([Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)nValue,[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrcDst, size_t nLength, int nScaleFactor,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsAddC_16s_ISfs_Ctx)

-
16-bit signed short in place signal add constant, scale, then clamp to saturated value.

- Parameters
-
**pSrcDst**–[In-Place Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1in_place_signal_pointer).**nValue**– Constant value to be added to each vector element**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nScaleFactor**–[Integer Result Scaling](https://docs.nvidia.com/introduction.html#general_conventions_lb_1integer_result_scaling).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsAddC_16s_Sfs_Ctx(const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrc,[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)nValue,[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pDst, size_t nLength, int nScaleFactor,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsAddC_16s_Sfs_Ctx)

-
16-bit signed short signal add constant, scale, then clamp to saturated value.

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nValue**– Constant value to be added to each vector element**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nScaleFactor**–[Integer Result Scaling](https://docs.nvidia.com/introduction.html#general_conventions_lb_1integer_result_scaling).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsAddC_16sc_ISfs_Ctx([Npp16sc](https://docs.nvidia.com/nppdefs.html#c.Npp16sc)nValue,[Npp16sc](https://docs.nvidia.com/nppdefs.html#c.Npp16sc)*pSrcDst, size_t nLength, int nScaleFactor,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsAddC_16sc_ISfs_Ctx)

-
16-bit integer complex number (16 bit real, 16 bit imaginary)signal add constant, scale, then clamp to saturated value.

- Parameters
-
**pSrcDst**–[In-Place Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1in_place_signal_pointer).**nValue**– Constant value to be added to each vector element**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nScaleFactor**–[Integer Result Scaling](https://docs.nvidia.com/introduction.html#general_conventions_lb_1integer_result_scaling).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsAddC_16sc_Sfs_Ctx(const[Npp16sc](https://docs.nvidia.com/nppdefs.html#c.Npp16sc)*pSrc,[Npp16sc](https://docs.nvidia.com/nppdefs.html#c.Npp16sc)nValue,[Npp16sc](https://docs.nvidia.com/nppdefs.html#c.Npp16sc)*pDst, size_t nLength, int nScaleFactor,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsAddC_16sc_Sfs_Ctx)

-
16-bit integer complex number (16 bit real, 16 bit imaginary) signal add constant, scale, then clamp to saturated value.

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nValue**– Constant value to be added to each vector element**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nScaleFactor**–[Integer Result Scaling](https://docs.nvidia.com/introduction.html#general_conventions_lb_1integer_result_scaling).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsAddC_32s_ISfs_Ctx([Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)nValue,[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pSrcDst, size_t nLength, int nScaleFactor,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsAddC_32s_ISfs_Ctx)

-
32-bit signed integer in place signal add constant and scale.

- Parameters
-
**pSrcDst**–[In-Place Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1in_place_signal_pointer).**nValue**– Constant value to be added to each vector element**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nScaleFactor**–[Integer Result Scaling](https://docs.nvidia.com/introduction.html#general_conventions_lb_1integer_result_scaling).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsAddC_32s_Sfs_Ctx(const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pSrc,[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)nValue,[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pDst, size_t nLength, int nScaleFactor,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsAddC_32s_Sfs_Ctx)

-
32-bit signed integersignal add constant and scale.

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nValue**– Constant value to be added to each vector element**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nScaleFactor**–[Integer Result Scaling](https://docs.nvidia.com/introduction.html#general_conventions_lb_1integer_result_scaling).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsAddC_32sc_ISfs_Ctx([Npp32sc](https://docs.nvidia.com/nppdefs.html#c.Npp32sc)nValue,[Npp32sc](https://docs.nvidia.com/nppdefs.html#c.Npp32sc)*pSrcDst, size_t nLength, int nScaleFactor,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsAddC_32sc_ISfs_Ctx)

-
32-bit integer complex number (32 bit real, 32 bit imaginary) in place signal add constant and scale.

- Parameters
-
**pSrcDst**–[In-Place Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1in_place_signal_pointer).**nValue**– Constant value to be added to each vector element**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nScaleFactor**–[Integer Result Scaling](https://docs.nvidia.com/introduction.html#general_conventions_lb_1integer_result_scaling).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsAddC_32sc_Sfs_Ctx(const[Npp32sc](https://docs.nvidia.com/nppdefs.html#c.Npp32sc)*pSrc,[Npp32sc](https://docs.nvidia.com/nppdefs.html#c.Npp32sc)nValue,[Npp32sc](https://docs.nvidia.com/nppdefs.html#c.Npp32sc)*pDst, size_t nLength, int nScaleFactor,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsAddC_32sc_Sfs_Ctx)

-
32-bit integer complex number (32 bit real, 32 bit imaginary) signal add constant and scale.

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nValue**– Constant value to be added to each vector element**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nScaleFactor**–[Integer Result Scaling](https://docs.nvidia.com/introduction.html#general_conventions_lb_1integer_result_scaling).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsAddC_32f_I_Ctx([Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)nValue,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrcDst, size_t nLength,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsAddC_32f_I_Ctx)

-
32-bit floating point in place signal add constant.

- Parameters
-
**pSrcDst**–[In-Place Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1in_place_signal_pointer).**nValue**– Constant value to be added to each vector element**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsAddC_32f_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)nValue,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pDst, size_t nLength,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsAddC_32f_Ctx)

-
32-bit floating point signal add constant.

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nValue**– Constant value to be added to each vector element**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsAddC_32fc_I_Ctx([Npp32fc](https://docs.nvidia.com/nppdefs.html#c.Npp32fc)nValue,[Npp32fc](https://docs.nvidia.com/nppdefs.html#c.Npp32fc)*pSrcDst, size_t nLength,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsAddC_32fc_I_Ctx)

-
32-bit floating point complex number (32 bit real, 32 bit imaginary) in place signal add constant.

- Parameters
-
**pSrcDst**–[In-Place Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1in_place_signal_pointer).**nValue**– Constant value to be added to each vector element**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsAddC_32fc_Ctx(const[Npp32fc](https://docs.nvidia.com/nppdefs.html#c.Npp32fc)*pSrc,[Npp32fc](https://docs.nvidia.com/nppdefs.html#c.Npp32fc)nValue,[Npp32fc](https://docs.nvidia.com/nppdefs.html#c.Npp32fc)*pDst, size_t nLength,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsAddC_32fc_Ctx)

-
32-bit floating point complex number (32 bit real, 32 bit imaginary) signal add constant.

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nValue**– Constant value to be added to each vector element.**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsAddC_64f_I_Ctx([Npp64f](https://docs.nvidia.com/nppdefs.html#c.Npp64f)nValue,[Npp64f](https://docs.nvidia.com/nppdefs.html#c.Npp64f)*pSrcDst, size_t nLength,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsAddC_64f_I_Ctx)

-
64-bit floating point, in place signal add constant.

- Parameters
-
**pSrcDst**–[In-Place Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1in_place_signal_pointer).**nValue**– Constant value to be added to each vector element**nLength**– Length of the vectors, number of items.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsAddC_64f_Ctx(const[Npp64f](https://docs.nvidia.com/nppdefs.html#c.Npp64f)*pSrc,[Npp64f](https://docs.nvidia.com/nppdefs.html#c.Npp64f)nValue,[Npp64f](https://docs.nvidia.com/nppdefs.html#c.Npp64f)*pDst, size_t nLength,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsAddC_64f_Ctx)

-
64-bit floating pointsignal add constant.

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nValue**– Constant value to be added to each vector element**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsAddC_64fc_I_Ctx([Npp64fc](https://docs.nvidia.com/nppdefs.html#c.Npp64fc)nValue,[Npp64fc](https://docs.nvidia.com/nppdefs.html#c.Npp64fc)*pSrcDst, size_t nLength,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsAddC_64fc_I_Ctx)

-
64-bit floating point complex number (64 bit real, 64 bit imaginary) in place signal add constant.

- Parameters
-
**pSrcDst**–[In-Place Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1in_place_signal_pointer).**nValue**– Constant value to be added to each vector element**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsAddC_64fc_Ctx(const[Npp64fc](https://docs.nvidia.com/nppdefs.html#c.Npp64fc)*pSrc,[Npp64fc](https://docs.nvidia.com/nppdefs.html#c.Npp64fc)nValue,[Npp64fc](https://docs.nvidia.com/nppdefs.html#c.Npp64fc)*pDst, size_t nLength,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsAddC_64fc_Ctx)

-
64-bit floating point complex number (64 bit real, 64 bit imaginary) signal add constant.

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nValue**– Constant value to be added to each vector element**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


### Signal AddProductC[](https://docs.nvidia.com#signal-addproductc)

#### AddProductC[](https://docs.nvidia.com#group__signal__addproductc_1signal_addproductc)

Adds product of a constant and each sample of a source signal to the each sample of destination signal.

Functions

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsAddProductC_32f_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)nValue,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pDst, size_t nLength,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsAddProductC_32f_Ctx)

-
32-bit floating point signal add product of signal times constant to destination signal.

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nValue**– Constant value to be multiplied by each vector element**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


### Signal MulC[](https://docs.nvidia.com#signal-mulc)

#### MulC[](https://docs.nvidia.com#group__signal__mulc_1signal_mulc)

Multiplies each sample of a signal by a constant value.

Functions

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsMulC_8u_ISfs_Ctx([Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)nValue,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrcDst, size_t nLength, int nScaleFactor,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsMulC_8u_ISfs_Ctx)

-
8-bit unsigned char in place signal times constant, scale, then clamp to saturated value

- Parameters
-
**pSrcDst**–[In-Place Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1in_place_signal_pointer).**nValue**– Constant value to be multiplied by each vector element**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nScaleFactor**–[Integer Result Scaling](https://docs.nvidia.com/introduction.html#general_conventions_lb_1integer_result_scaling).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsMulC_8u_Sfs_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)nValue,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, size_t nLength, int nScaleFactor,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsMulC_8u_Sfs_Ctx)

-
8-bit unsigned char signal times constant, scale, then clamp to saturated value.

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nValue**– Constant value to be multiplied by each vector element**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nScaleFactor**–[Integer Result Scaling](https://docs.nvidia.com/introduction.html#general_conventions_lb_1integer_result_scaling).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsMulC_16u_ISfs_Ctx([Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)nValue,[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrcDst, size_t nLength, int nScaleFactor,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsMulC_16u_ISfs_Ctx)

-
16-bit unsigned short in place signal times constant, scale, then clamp to saturated value.

- Parameters
-
**pSrcDst**–[In-Place Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1in_place_signal_pointer).**nValue**– Constant value to be multiplied by each vector element**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nScaleFactor**–[Integer Result Scaling](https://docs.nvidia.com/introduction.html#general_conventions_lb_1integer_result_scaling).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsMulC_16u_Sfs_Ctx(const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrc,[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)nValue,[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pDst, size_t nLength, int nScaleFactor,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsMulC_16u_Sfs_Ctx)

-
16-bit unsigned short signal times constant, scale, then clamp to saturated value.

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nValue**– Constant value to be multiplied by each vector element**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nScaleFactor**–[Integer Result Scaling](https://docs.nvidia.com/introduction.html#general_conventions_lb_1integer_result_scaling).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsMulC_16s_ISfs_Ctx([Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)nValue,[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrcDst, size_t nLength, int nScaleFactor,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsMulC_16s_ISfs_Ctx)

-
16-bit signed short in place signal times constant, scale, then clamp to saturated value.

- Parameters
-
**pSrcDst**–[In-Place Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1in_place_signal_pointer).**nValue**– Constant value to be multiplied by each vector element**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nScaleFactor**–[Integer Result Scaling](https://docs.nvidia.com/introduction.html#general_conventions_lb_1integer_result_scaling).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsMulC_16s_Sfs_Ctx(const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrc,[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)nValue,[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pDst, size_t nLength, int nScaleFactor,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsMulC_16s_Sfs_Ctx)

-
16-bit signed short signal times constant, scale, then clamp to saturated value.

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nValue**– Constant value to be multiplied by each vector element**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nScaleFactor**–[Integer Result Scaling](https://docs.nvidia.com/introduction.html#general_conventions_lb_1integer_result_scaling).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsMulC_16sc_ISfs_Ctx([Npp16sc](https://docs.nvidia.com/nppdefs.html#c.Npp16sc)nValue,[Npp16sc](https://docs.nvidia.com/nppdefs.html#c.Npp16sc)*pSrcDst, size_t nLength, int nScaleFactor,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsMulC_16sc_ISfs_Ctx)

-
16-bit integer complex number (16 bit real, 16 bit imaginary)signal times constant, scale, then clamp to saturated value.

- Parameters
-
**pSrcDst**–[In-Place Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1in_place_signal_pointer).**nValue**– Constant value to be multiplied by each vector element**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nScaleFactor**–[Integer Result Scaling](https://docs.nvidia.com/introduction.html#general_conventions_lb_1integer_result_scaling).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsMulC_16sc_Sfs_Ctx(const[Npp16sc](https://docs.nvidia.com/nppdefs.html#c.Npp16sc)*pSrc,[Npp16sc](https://docs.nvidia.com/nppdefs.html#c.Npp16sc)nValue,[Npp16sc](https://docs.nvidia.com/nppdefs.html#c.Npp16sc)*pDst, size_t nLength, int nScaleFactor,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsMulC_16sc_Sfs_Ctx)

-
16-bit integer complex number (16 bit real, 16 bit imaginary)signal times constant, scale, then clamp to saturated value.

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nValue**– Constant value to be multiplied by each vector element**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nScaleFactor**–[Integer Result Scaling](https://docs.nvidia.com/introduction.html#general_conventions_lb_1integer_result_scaling).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsMulC_32s_ISfs_Ctx([Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)nValue,[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pSrcDst, size_t nLength, int nScaleFactor,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsMulC_32s_ISfs_Ctx)

-
32-bit signed integer in place signal times constant and scale.

- Parameters
-
**pSrcDst**–[In-Place Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1in_place_signal_pointer).**nValue**– Constant value to be multiplied by each vector element**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nScaleFactor**–[Integer Result Scaling](https://docs.nvidia.com/introduction.html#general_conventions_lb_1integer_result_scaling).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsMulC_32s_Sfs_Ctx(const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pSrc,[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)nValue,[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pDst, size_t nLength, int nScaleFactor,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsMulC_32s_Sfs_Ctx)

-
32-bit signed integer signal times constant and scale.

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nValue**– Constant value to be multiplied by each vector element**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nScaleFactor**–[Integer Result Scaling](https://docs.nvidia.com/introduction.html#general_conventions_lb_1integer_result_scaling).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsMulC_32sc_ISfs_Ctx([Npp32sc](https://docs.nvidia.com/nppdefs.html#c.Npp32sc)nValue,[Npp32sc](https://docs.nvidia.com/nppdefs.html#c.Npp32sc)*pSrcDst, size_t nLength, int nScaleFactor,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsMulC_32sc_ISfs_Ctx)

-
32-bit integer complex number (32 bit real, 32 bit imaginary) in place signal times constant and scale.

- Parameters
-
**pSrcDst**–[In-Place Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1in_place_signal_pointer).**nValue**– Constant value to be multiplied by each vector element**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nScaleFactor**–[Integer Result Scaling](https://docs.nvidia.com/introduction.html#general_conventions_lb_1integer_result_scaling).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsMulC_32sc_Sfs_Ctx(const[Npp32sc](https://docs.nvidia.com/nppdefs.html#c.Npp32sc)*pSrc,[Npp32sc](https://docs.nvidia.com/nppdefs.html#c.Npp32sc)nValue,[Npp32sc](https://docs.nvidia.com/nppdefs.html#c.Npp32sc)*pDst, size_t nLength, int nScaleFactor,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsMulC_32sc_Sfs_Ctx)

-
32-bit integer complex number (32 bit real, 32 bit imaginary) signal times constant and scale.

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nValue**– Constant value to be multiplied by each vector element**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nScaleFactor**–[Integer Result Scaling](https://docs.nvidia.com/introduction.html#general_conventions_lb_1integer_result_scaling).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsMulC_32f_I_Ctx([Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)nValue,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrcDst, size_t nLength,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsMulC_32f_I_Ctx)

-
32-bit floating point in place signal times constant.

- Parameters
-
**pSrcDst**–[In-Place Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1in_place_signal_pointer).**nValue**– Constant value to be multiplied by each vector element**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsMulC_32f_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)nValue,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pDst, size_t nLength,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsMulC_32f_Ctx)

-
32-bit floating point signal times constant.

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nValue**– Constant value to be multiplied by each vector element**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsMulC_Low_32f16s_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)nValue,[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pDst, size_t nLength,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsMulC_Low_32f16s_Ctx)

-
32-bit floating point signal times constant with output converted to 16-bit signed integer.

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nValue**– Constant value to be multiplied by each vector element**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsMulC_32f16s_Sfs_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)nValue,[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pDst, size_t nLength, int nScaleFactor,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsMulC_32f16s_Sfs_Ctx)

-
32-bit floating point signal times constant with output converted to 16-bit signed integer with scaling and saturation of output result.

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nValue**– Constant value to be multiplied by each vector element**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nScaleFactor**–[Integer Result Scaling](https://docs.nvidia.com/introduction.html#general_conventions_lb_1integer_result_scaling).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsMulC_32fc_I_Ctx([Npp32fc](https://docs.nvidia.com/nppdefs.html#c.Npp32fc)nValue,[Npp32fc](https://docs.nvidia.com/nppdefs.html#c.Npp32fc)*pSrcDst, size_t nLength,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsMulC_32fc_I_Ctx)

-
32-bit floating point complex number (32 bit real, 32 bit imaginary) in place signal times constant.

- Parameters
-
**pSrcDst**–[In-Place Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1in_place_signal_pointer).**nValue**– Constant value to be multiplied by each vector element**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsMulC_32fc_Ctx(const[Npp32fc](https://docs.nvidia.com/nppdefs.html#c.Npp32fc)*pSrc,[Npp32fc](https://docs.nvidia.com/nppdefs.html#c.Npp32fc)nValue,[Npp32fc](https://docs.nvidia.com/nppdefs.html#c.Npp32fc)*pDst, size_t nLength,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsMulC_32fc_Ctx)

-
32-bit floating point complex number (32 bit real, 32 bit imaginary) signal times constant.

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nValue**– Constant value to be multiplied by each vector element**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsMulC_64f_I_Ctx([Npp64f](https://docs.nvidia.com/nppdefs.html#c.Npp64f)nValue,[Npp64f](https://docs.nvidia.com/nppdefs.html#c.Npp64f)*pSrcDst, size_t nLength,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsMulC_64f_I_Ctx)

-
64-bit floating point, in place signal times constant.

- Parameters
-
**pSrcDst**–[In-Place Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1in_place_signal_pointer).**nValue**– Constant value to be multiplied by each vector element**nLength**– Length of the vectors, number of items.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsMulC_64f_Ctx(const[Npp64f](https://docs.nvidia.com/nppdefs.html#c.Npp64f)*pSrc,[Npp64f](https://docs.nvidia.com/nppdefs.html#c.Npp64f)nValue,[Npp64f](https://docs.nvidia.com/nppdefs.html#c.Npp64f)*pDst, size_t nLength,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsMulC_64f_Ctx)

-
64-bit floating point signal times constant.

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nValue**– Constant value to be multiplied by each vector element**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsMulC_64f64s_ISfs_Ctx([Npp64f](https://docs.nvidia.com/nppdefs.html#c.Npp64f)nValue,[Npp64s](https://docs.nvidia.com/nppdefs.html#c.Npp64s)*pDst, size_t nLength, int nScaleFactor,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsMulC_64f64s_ISfs_Ctx)

-
64-bit floating point signal times constant with in place conversion to 64-bit signed integer and with scaling and saturation of output result.

- Parameters
-
**nValue**– Constant value to be multiplied by each vector element**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nScaleFactor**–[Integer Result Scaling](https://docs.nvidia.com/introduction.html#general_conventions_lb_1integer_result_scaling).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsMulC_64fc_I_Ctx([Npp64fc](https://docs.nvidia.com/nppdefs.html#c.Npp64fc)nValue,[Npp64fc](https://docs.nvidia.com/nppdefs.html#c.Npp64fc)*pSrcDst, size_t nLength,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsMulC_64fc_I_Ctx)

-
64-bit floating point complex number (64 bit real, 64 bit imaginary) in place signal times constant.

- Parameters
-
**pSrcDst**–[In-Place Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1in_place_signal_pointer).**nValue**– Constant value to be multiplied by each vector element**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsMulC_64fc_Ctx(const[Npp64fc](https://docs.nvidia.com/nppdefs.html#c.Npp64fc)*pSrc,[Npp64fc](https://docs.nvidia.com/nppdefs.html#c.Npp64fc)nValue,[Npp64fc](https://docs.nvidia.com/nppdefs.html#c.Npp64fc)*pDst, size_t nLength,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsMulC_64fc_Ctx)

-
64-bit floating point complex number (64 bit real, 64 bit imaginary) signal times constant.

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nValue**– Constant value to be multiplied by each vector element**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


### Signal SubC[](https://docs.nvidia.com#signal-subc)

#### SubC[](https://docs.nvidia.com#group__signal__subc_1signal_subc)

Subtracts a constant from each sample of a signal.

Functions

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsSubC_8u_ISfs_Ctx([Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)nValue,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrcDst, size_t nLength, int nScaleFactor,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsSubC_8u_ISfs_Ctx)

-
8-bit unsigned char in place signal subtract constant, scale, then clamp to saturated value

- Parameters
-
**pSrcDst**–[In-Place Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1in_place_signal_pointer).**nValue**– Constant value to be subtracted from each vector element**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nScaleFactor**–[Integer Result Scaling](https://docs.nvidia.com/introduction.html#general_conventions_lb_1integer_result_scaling).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsSubC_8u_Sfs_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)nValue,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, size_t nLength, int nScaleFactor,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsSubC_8u_Sfs_Ctx)

-
8-bit unsigned char signal subtract constant, scale, then clamp to saturated value.

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nValue**– Constant value to be subtracted from each vector element**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nScaleFactor**–[Integer Result Scaling](https://docs.nvidia.com/introduction.html#general_conventions_lb_1integer_result_scaling).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsSubC_16u_ISfs_Ctx([Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)nValue,[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrcDst, size_t nLength, int nScaleFactor,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsSubC_16u_ISfs_Ctx)

-
16-bit unsigned short in place signal subtract constant, scale, then clamp to saturated value.

- Parameters
-
**pSrcDst**–[In-Place Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1in_place_signal_pointer).**nValue**– Constant value to be subtracted from each vector element**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nScaleFactor**–[Integer Result Scaling](https://docs.nvidia.com/introduction.html#general_conventions_lb_1integer_result_scaling).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsSubC_16u_Sfs_Ctx(const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrc,[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)nValue,[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pDst, size_t nLength, int nScaleFactor,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsSubC_16u_Sfs_Ctx)

-
16-bit unsigned short signal subtract constant, scale, then clamp to saturated value.

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nValue**– Constant value to be subtracted from each vector element**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nScaleFactor**–[Integer Result Scaling](https://docs.nvidia.com/introduction.html#general_conventions_lb_1integer_result_scaling).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsSubC_16s_ISfs_Ctx([Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)nValue,[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrcDst, size_t nLength, int nScaleFactor,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsSubC_16s_ISfs_Ctx)

-
16-bit signed short in place signal subtract constant, scale, then clamp to saturated value.

- Parameters
-
**pSrcDst**–[In-Place Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1in_place_signal_pointer).**nValue**– Constant value to be subtracted from each vector element**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nScaleFactor**–[Integer Result Scaling](https://docs.nvidia.com/introduction.html#general_conventions_lb_1integer_result_scaling).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsSubC_16s_Sfs_Ctx(const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrc,[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)nValue,[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pDst, size_t nLength, int nScaleFactor,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsSubC_16s_Sfs_Ctx)

-
16-bit signed short signal subtract constant, scale, then clamp to saturated value.

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nValue**– Constant value to be subtracted from each vector element**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nScaleFactor**–[Integer Result Scaling](https://docs.nvidia.com/introduction.html#general_conventions_lb_1integer_result_scaling).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsSubC_16sc_ISfs_Ctx([Npp16sc](https://docs.nvidia.com/nppdefs.html#c.Npp16sc)nValue,[Npp16sc](https://docs.nvidia.com/nppdefs.html#c.Npp16sc)*pSrcDst, size_t nLength, int nScaleFactor,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsSubC_16sc_ISfs_Ctx)

-
16-bit integer complex number (16 bit real, 16 bit imaginary) signal subtract constant, scale, then clamp to saturated value.

- Parameters
-
**pSrcDst**–[In-Place Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1in_place_signal_pointer).**nValue**– Constant value to be subtracted from each vector element**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nScaleFactor**–[Integer Result Scaling](https://docs.nvidia.com/introduction.html#general_conventions_lb_1integer_result_scaling).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsSubC_16sc_Sfs_Ctx(const[Npp16sc](https://docs.nvidia.com/nppdefs.html#c.Npp16sc)*pSrc,[Npp16sc](https://docs.nvidia.com/nppdefs.html#c.Npp16sc)nValue,[Npp16sc](https://docs.nvidia.com/nppdefs.html#c.Npp16sc)*pDst, size_t nLength, int nScaleFactor,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsSubC_16sc_Sfs_Ctx)

-
16-bit integer complex number (16 bit real, 16 bit imaginary) signal subtract constant, scale, then clamp to saturated value.

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nValue**– Constant value to be subtracted from each vector element**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nScaleFactor**–[Integer Result Scaling](https://docs.nvidia.com/introduction.html#general_conventions_lb_1integer_result_scaling).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsSubC_32s_ISfs_Ctx([Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)nValue,[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pSrcDst, size_t nLength, int nScaleFactor,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsSubC_32s_ISfs_Ctx)

-
32-bit signed integer in place signal subtract constant and scale.

- Parameters
-
**pSrcDst**–[In-Place Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1in_place_signal_pointer).**nValue**– Constant value to be subtracted from each vector element**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nScaleFactor**–[Integer Result Scaling](https://docs.nvidia.com/introduction.html#general_conventions_lb_1integer_result_scaling).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsSubC_32s_Sfs_Ctx(const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pSrc,[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)nValue,[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pDst, size_t nLength, int nScaleFactor,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsSubC_32s_Sfs_Ctx)

-
32-bit signed integer signal subtract constant and scale.

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nValue**– Constant value to be subtracted from each vector element**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nScaleFactor**–[Integer Result Scaling](https://docs.nvidia.com/introduction.html#general_conventions_lb_1integer_result_scaling).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsSubC_32sc_ISfs_Ctx([Npp32sc](https://docs.nvidia.com/nppdefs.html#c.Npp32sc)nValue,[Npp32sc](https://docs.nvidia.com/nppdefs.html#c.Npp32sc)*pSrcDst, size_t nLength, int nScaleFactor,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsSubC_32sc_ISfs_Ctx)

-
32-bit integer complex number (32 bit real, 32 bit imaginary) in place signal subtract constant and scale.

- Parameters
-
**pSrcDst**–[In-Place Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1in_place_signal_pointer).**nValue**– Constant value to be subtracted from each vector element**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nScaleFactor**–[Integer Result Scaling](https://docs.nvidia.com/introduction.html#general_conventions_lb_1integer_result_scaling).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsSubC_32sc_Sfs_Ctx(const[Npp32sc](https://docs.nvidia.com/nppdefs.html#c.Npp32sc)*pSrc,[Npp32sc](https://docs.nvidia.com/nppdefs.html#c.Npp32sc)nValue,[Npp32sc](https://docs.nvidia.com/nppdefs.html#c.Npp32sc)*pDst, size_t nLength, int nScaleFactor,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsSubC_32sc_Sfs_Ctx)

-
32-bit integer complex number (32 bit real, 32 bit imaginary)signal subtract constant and scale.

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nValue**– Constant value to be subtracted from each vector element**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nScaleFactor**–[Integer Result Scaling](https://docs.nvidia.com/introduction.html#general_conventions_lb_1integer_result_scaling).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsSubC_32f_I_Ctx([Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)nValue,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrcDst, size_t nLength,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsSubC_32f_I_Ctx)

-
32-bit floating point in place signal subtract constant.

- Parameters
-
**pSrcDst**–[In-Place Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1in_place_signal_pointer).**nValue**– Constant value to be subtracted from each vector element**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsSubC_32f_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)nValue,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pDst, size_t nLength,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsSubC_32f_Ctx)

-
32-bit floating point signal subtract constant.

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nValue**– Constant value to be subtracted from each vector element**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsSubC_32fc_I_Ctx([Npp32fc](https://docs.nvidia.com/nppdefs.html#c.Npp32fc)nValue,[Npp32fc](https://docs.nvidia.com/nppdefs.html#c.Npp32fc)*pSrcDst, size_t nLength,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsSubC_32fc_I_Ctx)

-
32-bit floating point complex number (32 bit real, 32 bit imaginary) in place signal subtract constant.

- Parameters
-
**pSrcDst**–[In-Place Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1in_place_signal_pointer).**nValue**– Constant value to be subtracted from each vector element**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsSubC_32fc_Ctx(const[Npp32fc](https://docs.nvidia.com/nppdefs.html#c.Npp32fc)*pSrc,[Npp32fc](https://docs.nvidia.com/nppdefs.html#c.Npp32fc)nValue,[Npp32fc](https://docs.nvidia.com/nppdefs.html#c.Npp32fc)*pDst, size_t nLength,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsSubC_32fc_Ctx)

-
32-bit floating point complex number (32 bit real, 32 bit imaginary) signal subtract constant.

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nValue**– Constant value to be subtracted from each vector element**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsSubC_64f_I_Ctx([Npp64f](https://docs.nvidia.com/nppdefs.html#c.Npp64f)nValue,[Npp64f](https://docs.nvidia.com/nppdefs.html#c.Npp64f)*pSrcDst, size_t nLength,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsSubC_64f_I_Ctx)

-
64-bit floating point, in place signal subtract constant.

- Parameters
-
**pSrcDst**–[In-Place Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1in_place_signal_pointer).**nValue**– Constant value to be subtracted from each vector element**nLength**– Length of the vectors, number of items.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsSubC_64f_Ctx(const[Npp64f](https://docs.nvidia.com/nppdefs.html#c.Npp64f)*pSrc,[Npp64f](https://docs.nvidia.com/nppdefs.html#c.Npp64f)nValue,[Npp64f](https://docs.nvidia.com/nppdefs.html#c.Npp64f)*pDst, size_t nLength,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsSubC_64f_Ctx)

-
64-bit floating point signal subtract constant.

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nValue**– Constant value to be subtracted from each vector element**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsSubC_64fc_I_Ctx([Npp64fc](https://docs.nvidia.com/nppdefs.html#c.Npp64fc)nValue,[Npp64fc](https://docs.nvidia.com/nppdefs.html#c.Npp64fc)*pSrcDst, size_t nLength,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsSubC_64fc_I_Ctx)

-
64-bit floating point complex number (64 bit real, 64 bit imaginary) in place signal subtract constant.

- Parameters
-
**pSrcDst**–[In-Place Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1in_place_signal_pointer).**nValue**– Constant value to be subtracted from each vector element**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsSubC_64fc_Ctx(const[Npp64fc](https://docs.nvidia.com/nppdefs.html#c.Npp64fc)*pSrc,[Npp64fc](https://docs.nvidia.com/nppdefs.html#c.Npp64fc)nValue,[Npp64fc](https://docs.nvidia.com/nppdefs.html#c.Npp64fc)*pDst, size_t nLength,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsSubC_64fc_Ctx)

-
64-bit floating point complex number (64 bit real, 64 bit imaginary) signal subtract constant.

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nValue**– Constant value to be subtracted from each vector element**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


### Signal SubCRev[](https://docs.nvidia.com#signal-subcrev)

#### SubCRev[](https://docs.nvidia.com#group__signal__subcrev_1signal_subcrev)

Subtracts each sample of a signal from a constant.

Functions

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsSubCRev_8u_ISfs_Ctx([Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)nValue,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrcDst, size_t nLength, int nScaleFactor,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsSubCRev_8u_ISfs_Ctx)

-
8-bit unsigned char in place signal subtract from constant, scale, then clamp to saturated value

- Parameters
-
**pSrcDst**–[In-Place Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1in_place_signal_pointer).**nValue**– Constant value each vector element is to be subtracted from**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nScaleFactor**–[Integer Result Scaling](https://docs.nvidia.com/introduction.html#general_conventions_lb_1integer_result_scaling).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsSubCRev_8u_Sfs_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)nValue,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, size_t nLength, int nScaleFactor,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsSubCRev_8u_Sfs_Ctx)

-
8-bit unsigned char signal subtract from constant, scale, then clamp to saturated value.

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nValue**– Constant value each vector element is to be subtracted from**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nScaleFactor**–[Integer Result Scaling](https://docs.nvidia.com/introduction.html#general_conventions_lb_1integer_result_scaling).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsSubCRev_16u_ISfs_Ctx([Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)nValue,[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrcDst, size_t nLength, int nScaleFactor,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsSubCRev_16u_ISfs_Ctx)

-
16-bit unsigned short in place signal subtract from constant, scale, then clamp to saturated value.

- Parameters
-
**pSrcDst**–[In-Place Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1in_place_signal_pointer).**nValue**– Constant value each vector element is to be subtracted from**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nScaleFactor**–[Integer Result Scaling](https://docs.nvidia.com/introduction.html#general_conventions_lb_1integer_result_scaling).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsSubCRev_16u_Sfs_Ctx(const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrc,[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)nValue,[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pDst, size_t nLength, int nScaleFactor,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsSubCRev_16u_Sfs_Ctx)

-
16-bit unsigned short signal subtract from constant, scale, then clamp to saturated value.

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nValue**– Constant value each vector element is to be subtracted from**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nScaleFactor**–[Integer Result Scaling](https://docs.nvidia.com/introduction.html#general_conventions_lb_1integer_result_scaling).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsSubCRev_16s_ISfs_Ctx([Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)nValue,[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrcDst, size_t nLength, int nScaleFactor,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsSubCRev_16s_ISfs_Ctx)

-
16-bit signed short in place signal subtract from constant, scale, then clamp to saturated value.

- Parameters
-
**pSrcDst**–[In-Place Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1in_place_signal_pointer).**nValue**– Constant value each vector element is to be subtracted from**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nScaleFactor**–[Integer Result Scaling](https://docs.nvidia.com/introduction.html#general_conventions_lb_1integer_result_scaling).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsSubCRev_16s_Sfs_Ctx(const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrc,[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)nValue,[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pDst, size_t nLength, int nScaleFactor,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsSubCRev_16s_Sfs_Ctx)

-
16-bit signed short signal subtract from constant, scale, then clamp to saturated value.

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nValue**– Constant value each vector element is to be subtracted from**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nScaleFactor**–[Integer Result Scaling](https://docs.nvidia.com/introduction.html#general_conventions_lb_1integer_result_scaling).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsSubCRev_16sc_ISfs_Ctx([Npp16sc](https://docs.nvidia.com/nppdefs.html#c.Npp16sc)nValue,[Npp16sc](https://docs.nvidia.com/nppdefs.html#c.Npp16sc)*pSrcDst, size_t nLength, int nScaleFactor,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsSubCRev_16sc_ISfs_Ctx)

-
16-bit integer complex number (16 bit real, 16 bit imaginary) signal subtract from constant, scale, then clamp to saturated value.

- Parameters
-
**pSrcDst**–[In-Place Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1in_place_signal_pointer).**nValue**– Constant value each vector element is to be subtracted from**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nScaleFactor**–[Integer Result Scaling](https://docs.nvidia.com/introduction.html#general_conventions_lb_1integer_result_scaling).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsSubCRev_16sc_Sfs_Ctx(const[Npp16sc](https://docs.nvidia.com/nppdefs.html#c.Npp16sc)*pSrc,[Npp16sc](https://docs.nvidia.com/nppdefs.html#c.Npp16sc)nValue,[Npp16sc](https://docs.nvidia.com/nppdefs.html#c.Npp16sc)*pDst, size_t nLength, int nScaleFactor,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsSubCRev_16sc_Sfs_Ctx)

-
16-bit integer complex number (16 bit real, 16 bit imaginary) signal subtract from constant, scale, then clamp to saturated value.

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nValue**– Constant value each vector element is to be subtracted from**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nScaleFactor**–[Integer Result Scaling](https://docs.nvidia.com/introduction.html#general_conventions_lb_1integer_result_scaling).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsSubCRev_32s_ISfs_Ctx([Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)nValue,[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pSrcDst, size_t nLength, int nScaleFactor,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsSubCRev_32s_ISfs_Ctx)

-
32-bit signed integer in place signal subtract from constant and scale.

- Parameters
-
**pSrcDst**–[In-Place Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1in_place_signal_pointer).**nValue**– Constant value each vector element is to be subtracted from**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nScaleFactor**–[Integer Result Scaling](https://docs.nvidia.com/introduction.html#general_conventions_lb_1integer_result_scaling).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsSubCRev_32s_Sfs_Ctx(const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pSrc,[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)nValue,[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pDst, size_t nLength, int nScaleFactor,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsSubCRev_32s_Sfs_Ctx)

-
32-bit signed integersignal subtract from constant and scale.

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nValue**– Constant value each vector element is to be subtracted from**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nScaleFactor**–[Integer Result Scaling](https://docs.nvidia.com/introduction.html#general_conventions_lb_1integer_result_scaling).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsSubCRev_32sc_ISfs_Ctx([Npp32sc](https://docs.nvidia.com/nppdefs.html#c.Npp32sc)nValue,[Npp32sc](https://docs.nvidia.com/nppdefs.html#c.Npp32sc)*pSrcDst, size_t nLength, int nScaleFactor,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsSubCRev_32sc_ISfs_Ctx)

-
32-bit integer complex number (32 bit real, 32 bit imaginary) in place signal subtract from constant and scale.

- Parameters
-
**pSrcDst**–[In-Place Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1in_place_signal_pointer).**nValue**– Constant value each vector element is to be subtracted from**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nScaleFactor**–[Integer Result Scaling](https://docs.nvidia.com/introduction.html#general_conventions_lb_1integer_result_scaling).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsSubCRev_32sc_Sfs_Ctx(const[Npp32sc](https://docs.nvidia.com/nppdefs.html#c.Npp32sc)*pSrc,[Npp32sc](https://docs.nvidia.com/nppdefs.html#c.Npp32sc)nValue,[Npp32sc](https://docs.nvidia.com/nppdefs.html#c.Npp32sc)*pDst, size_t nLength, int nScaleFactor,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsSubCRev_32sc_Sfs_Ctx)

-
32-bit integer complex number (32 bit real, 32 bit imaginary) signal subtract from constant and scale.

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nValue**– Constant value each vector element is to be subtracted from**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nScaleFactor**–[Integer Result Scaling](https://docs.nvidia.com/introduction.html#general_conventions_lb_1integer_result_scaling).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsSubCRev_32f_I_Ctx([Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)nValue,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrcDst, size_t nLength,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsSubCRev_32f_I_Ctx)

-
32-bit floating point in place signal subtract from constant.

- Parameters
-
**pSrcDst**–[In-Place Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1in_place_signal_pointer).**nValue**– Constant value each vector element is to be subtracted from**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsSubCRev_32f_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)nValue,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pDst, size_t nLength,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsSubCRev_32f_Ctx)

-
32-bit floating point signal subtract from constant.

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nValue**– Constant value each vector element is to be subtracted from**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsSubCRev_32fc_I_Ctx([Npp32fc](https://docs.nvidia.com/nppdefs.html#c.Npp32fc)nValue,[Npp32fc](https://docs.nvidia.com/nppdefs.html#c.Npp32fc)*pSrcDst, size_t nLength,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsSubCRev_32fc_I_Ctx)

-
32-bit floating point complex number (32 bit real, 32 bit imaginary) in place signal subtract from constant.

- Parameters
-
**pSrcDst**–[In-Place Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1in_place_signal_pointer).**nValue**– Constant value each vector element is to be subtracted from**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsSubCRev_32fc_Ctx(const[Npp32fc](https://docs.nvidia.com/nppdefs.html#c.Npp32fc)*pSrc,[Npp32fc](https://docs.nvidia.com/nppdefs.html#c.Npp32fc)nValue,[Npp32fc](https://docs.nvidia.com/nppdefs.html#c.Npp32fc)*pDst, size_t nLength,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsSubCRev_32fc_Ctx)

-
32-bit floating point complex number (32 bit real, 32 bit imaginary) signal subtract from constant.

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nValue**– Constant value each vector element is to be subtracted from**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsSubCRev_64f_I_Ctx([Npp64f](https://docs.nvidia.com/nppdefs.html#c.Npp64f)nValue,[Npp64f](https://docs.nvidia.com/nppdefs.html#c.Npp64f)*pSrcDst, size_t nLength,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsSubCRev_64f_I_Ctx)

-
64-bit floating point, in place signal subtract from constant.

- Parameters
-
**pSrcDst**–[In-Place Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1in_place_signal_pointer).**nValue**– Constant value each vector element is to be subtracted from**nLength**– Length of the vectors, number of items.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsSubCRev_64f_Ctx(const[Npp64f](https://docs.nvidia.com/nppdefs.html#c.Npp64f)*pSrc,[Npp64f](https://docs.nvidia.com/nppdefs.html#c.Npp64f)nValue,[Npp64f](https://docs.nvidia.com/nppdefs.html#c.Npp64f)*pDst, size_t nLength,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsSubCRev_64f_Ctx)

-
64-bit floating point signal subtract from constant.

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nValue**– Constant value each vector element is to be subtracted from**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsSubCRev_64fc_I_Ctx([Npp64fc](https://docs.nvidia.com/nppdefs.html#c.Npp64fc)nValue,[Npp64fc](https://docs.nvidia.com/nppdefs.html#c.Npp64fc)*pSrcDst, size_t nLength,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsSubCRev_64fc_I_Ctx)

-
64-bit floating point complex number (64 bit real, 64 bit imaginary) in place signal subtract from constant.

- Parameters
-
**pSrcDst**–[In-Place Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1in_place_signal_pointer).**nValue**– Constant value each vector element is to be subtracted from**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsSubCRev_64fc_Ctx(const[Npp64fc](https://docs.nvidia.com/nppdefs.html#c.Npp64fc)*pSrc,[Npp64fc](https://docs.nvidia.com/nppdefs.html#c.Npp64fc)nValue,[Npp64fc](https://docs.nvidia.com/nppdefs.html#c.Npp64fc)*pDst, size_t nLength,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsSubCRev_64fc_Ctx)

-
64-bit floating point complex number (64 bit real, 64 bit imaginary) signal subtract from constant.

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nValue**– Constant value each vector element is to be subtracted from**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


### Signal DivC[](https://docs.nvidia.com#signal-divc)

#### DivC[](https://docs.nvidia.com#group__signal__divc_1signal_divc)

Divides each sample of a signal by a constant.

Functions

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsDivC_8u_ISfs_Ctx([Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)nValue,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrcDst, size_t nLength, int nScaleFactor,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsDivC_8u_ISfs_Ctx)

-
8-bit unsigned char in place signal divided by constant, scale, then clamp to saturated value

- Parameters
-
**pSrcDst**–[In-Place Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1in_place_signal_pointer).**nValue**– Constant value to be divided into each vector element**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nScaleFactor**–[Integer Result Scaling](https://docs.nvidia.com/introduction.html#general_conventions_lb_1integer_result_scaling).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsDivC_8u_Sfs_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)nValue,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, size_t nLength, int nScaleFactor,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsDivC_8u_Sfs_Ctx)

-
8-bit unsigned char signal divided by constant, scale, then clamp to saturated value.

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nValue**– Constant value to be divided into each vector element**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nScaleFactor**–[Integer Result Scaling](https://docs.nvidia.com/introduction.html#general_conventions_lb_1integer_result_scaling).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsDivC_16u_ISfs_Ctx([Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)nValue,[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrcDst, size_t nLength, int nScaleFactor,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsDivC_16u_ISfs_Ctx)

-
16-bit unsigned short in place signal divided by constant, scale, then clamp to saturated value.

- Parameters
-
**pSrcDst**–[In-Place Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1in_place_signal_pointer).**nValue**– Constant value to be divided into each vector element**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nScaleFactor**–[Integer Result Scaling](https://docs.nvidia.com/introduction.html#general_conventions_lb_1integer_result_scaling).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsDivC_16u_Sfs_Ctx(const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrc,[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)nValue,[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pDst, size_t nLength, int nScaleFactor,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsDivC_16u_Sfs_Ctx)

-
16-bit unsigned short signal divided by constant, scale, then clamp to saturated value.

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nValue**– Constant value to be divided into each vector element**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nScaleFactor**–[Integer Result Scaling](https://docs.nvidia.com/introduction.html#general_conventions_lb_1integer_result_scaling).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsDivC_16s_ISfs_Ctx([Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)nValue,[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrcDst, size_t nLength, int nScaleFactor,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsDivC_16s_ISfs_Ctx)

-
16-bit signed short in place signal divided by constant, scale, then clamp to saturated value.

- Parameters
-
**pSrcDst**–[In-Place Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1in_place_signal_pointer).**nValue**– Constant value to be divided into each vector element**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nScaleFactor**–[Integer Result Scaling](https://docs.nvidia.com/introduction.html#general_conventions_lb_1integer_result_scaling).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsDivC_16s_Sfs_Ctx(const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrc,[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)nValue,[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pDst, size_t nLength, int nScaleFactor,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsDivC_16s_Sfs_Ctx)

-
16-bit signed short signal divided by constant, scale, then clamp to saturated value.

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nValue**– Constant value to be divided into each vector element**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nScaleFactor**–[Integer Result Scaling](https://docs.nvidia.com/introduction.html#general_conventions_lb_1integer_result_scaling).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsDivC_16sc_ISfs_Ctx([Npp16sc](https://docs.nvidia.com/nppdefs.html#c.Npp16sc)nValue,[Npp16sc](https://docs.nvidia.com/nppdefs.html#c.Npp16sc)*pSrcDst, size_t nLength, int nScaleFactor,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsDivC_16sc_ISfs_Ctx)

-
16-bit integer complex number (16 bit real, 16 bit imaginary)signal divided by constant, scale, then clamp to saturated value.

- Parameters
-
**pSrcDst**–[In-Place Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1in_place_signal_pointer).**nValue**– Constant value to be divided into each vector element**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nScaleFactor**–[Integer Result Scaling](https://docs.nvidia.com/introduction.html#general_conventions_lb_1integer_result_scaling).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsDivC_16sc_Sfs_Ctx(const[Npp16sc](https://docs.nvidia.com/nppdefs.html#c.Npp16sc)*pSrc,[Npp16sc](https://docs.nvidia.com/nppdefs.html#c.Npp16sc)nValue,[Npp16sc](https://docs.nvidia.com/nppdefs.html#c.Npp16sc)*pDst, size_t nLength, int nScaleFactor,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsDivC_16sc_Sfs_Ctx)

-
16-bit integer complex number (16 bit real, 16 bit imaginary) signal divided by constant, scale, then clamp to saturated value.

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nValue**– Constant value to be divided into each vector element**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nScaleFactor**–[Integer Result Scaling](https://docs.nvidia.com/introduction.html#general_conventions_lb_1integer_result_scaling).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsDivC_32f_I_Ctx([Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)nValue,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrcDst, size_t nLength,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsDivC_32f_I_Ctx)

-
32-bit floating point in place signal divided by constant.

- Parameters
-
**pSrcDst**–[In-Place Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1in_place_signal_pointer).**nValue**– Constant value to be divided into each vector element**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsDivC_32f_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)nValue,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pDst, size_t nLength,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsDivC_32f_Ctx)

-
32-bit floating point signal divided by constant.

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nValue**– Constant value to be divided into each vector element**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsDivC_32fc_I_Ctx([Npp32fc](https://docs.nvidia.com/nppdefs.html#c.Npp32fc)nValue,[Npp32fc](https://docs.nvidia.com/nppdefs.html#c.Npp32fc)*pSrcDst, size_t nLength,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsDivC_32fc_I_Ctx)

-
32-bit floating point complex number (32 bit real, 32 bit imaginary) in place signal divided by constant.

- Parameters
-
**pSrcDst**–[In-Place Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1in_place_signal_pointer).**nValue**– Constant value to be divided into each vector element**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsDivC_32fc_Ctx(const[Npp32fc](https://docs.nvidia.com/nppdefs.html#c.Npp32fc)*pSrc,[Npp32fc](https://docs.nvidia.com/nppdefs.html#c.Npp32fc)nValue,[Npp32fc](https://docs.nvidia.com/nppdefs.html#c.Npp32fc)*pDst, size_t nLength,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsDivC_32fc_Ctx)

-
32-bit floating point complex number (32 bit real, 32 bit imaginary) signal divided by constant.

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nValue**– Constant value to be divided into each vector element**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsDivC_64f_I_Ctx([Npp64f](https://docs.nvidia.com/nppdefs.html#c.Npp64f)nValue,[Npp64f](https://docs.nvidia.com/nppdefs.html#c.Npp64f)*pSrcDst, size_t nLength,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsDivC_64f_I_Ctx)

-
64-bit floating point in place signal divided by constant.

- Parameters
-
**pSrcDst**–[In-Place Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1in_place_signal_pointer).**nValue**– Constant value to be divided into each vector element**nLength**– Length of the vectors, number of items.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsDivC_64f_Ctx(const[Npp64f](https://docs.nvidia.com/nppdefs.html#c.Npp64f)*pSrc,[Npp64f](https://docs.nvidia.com/nppdefs.html#c.Npp64f)nValue,[Npp64f](https://docs.nvidia.com/nppdefs.html#c.Npp64f)*pDst, size_t nLength,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsDivC_64f_Ctx)

-
64-bit floating point signal divided by constant.

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nValue**– Constant value to be divided into each vector element**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsDivC_64fc_I_Ctx([Npp64fc](https://docs.nvidia.com/nppdefs.html#c.Npp64fc)nValue,[Npp64fc](https://docs.nvidia.com/nppdefs.html#c.Npp64fc)*pSrcDst, size_t nLength,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsDivC_64fc_I_Ctx)

-
64-bit floating point complex number (64 bit real, 64 bit imaginary) in place signal divided by constant.

- Parameters
-
**pSrcDst**–[In-Place Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1in_place_signal_pointer).**nValue**– Constant value to be divided into each vector element**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsDivC_64fc_Ctx(const[Npp64fc](https://docs.nvidia.com/nppdefs.html#c.Npp64fc)*pSrc,[Npp64fc](https://docs.nvidia.com/nppdefs.html#c.Npp64fc)nValue,[Npp64fc](https://docs.nvidia.com/nppdefs.html#c.Npp64fc)*pDst, size_t nLength,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsDivC_64fc_Ctx)

-
64-bit floating point complex number (64 bit real, 64 bit imaginary) signal divided by constant.

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nValue**– Constant value to be divided into each vector element**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


### Signal DivCRev[](https://docs.nvidia.com#signal-divcrev)

#### DivCRev[](https://docs.nvidia.com#group__signal__divcrev_1signal_divcrev)

Divides a constant by each sample of a signal.

Functions

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsDivCRev_16u_I_Ctx([Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)nValue,[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrcDst, size_t nLength,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsDivCRev_16u_I_Ctx)

-
16-bit unsigned short in place constant divided by signal, then clamp to saturated value.

- Parameters
-
**pSrcDst**–[In-Place Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1in_place_signal_pointer).**nValue**– Constant value to be divided by each vector element**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsDivCRev_16u_Ctx(const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrc,[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)nValue,[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pDst, size_t nLength,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsDivCRev_16u_Ctx)

-
16-bit unsigned short signal divided by constant, then clamp to saturated value.

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nValue**– Constant value to be divided by each vector element**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsDivCRev_32f_I_Ctx([Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)nValue,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrcDst, size_t nLength,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsDivCRev_32f_I_Ctx)

-
32-bit floating point in place constant divided by signal.

- Parameters
-
**pSrcDst**–[In-Place Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1in_place_signal_pointer).**nValue**– Constant value to be divided by each vector element**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsDivCRev_32f_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)nValue,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pDst, size_t nLength,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsDivCRev_32f_Ctx)

-
32-bit floating point constant divided by signal.

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nValue**– Constant value to be divided by each vector element**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


### Signal Add[](https://docs.nvidia.com#signal-add)

#### Add[](https://docs.nvidia.com#group__signal__add_1signal_add)

Sample by sample addition of two signals.

Functions

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsAdd_16s_Ctx(const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrc1, const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrc2,[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pDst, size_t nLength,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsAdd_16s_Ctx)

-
16-bit signed short signal add signal, then clamp to saturated value.

- Parameters
-
**pSrc1**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pSrc2**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer). signal2 elements to be added to signal1 elements**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsAdd_16u_Ctx(const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrc1, const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrc2,[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pDst, size_t nLength,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsAdd_16u_Ctx)

-
16-bit unsigned short signal add signal, then clamp to saturated value.

- Parameters
-
**pSrc1**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pSrc2**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer). signal2 elements to be added to signal1 elements**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsAdd_32u_Ctx(const[Npp32u](https://docs.nvidia.com/nppdefs.html#c.Npp32u)*pSrc1, const[Npp32u](https://docs.nvidia.com/nppdefs.html#c.Npp32u)*pSrc2,[Npp32u](https://docs.nvidia.com/nppdefs.html#c.Npp32u)*pDst, size_t nLength,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsAdd_32u_Ctx)

-
32-bit unsigned int signal add signal, then clamp to saturated value.

- Parameters
-
**pSrc1**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pSrc2**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer). signal2 elements to be added to signal1 elements**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsAdd_32f_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc1, const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc2,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pDst, size_t nLength,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsAdd_32f_Ctx)

-
32-bit floating point signal add signal, then clamp to saturated value.

- Parameters
-
**pSrc1**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pSrc2**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer). signal2 elements to be added to signal1 elements**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsAdd_64f_Ctx(const[Npp64f](https://docs.nvidia.com/nppdefs.html#c.Npp64f)*pSrc1, const[Npp64f](https://docs.nvidia.com/nppdefs.html#c.Npp64f)*pSrc2,[Npp64f](https://docs.nvidia.com/nppdefs.html#c.Npp64f)*pDst, size_t nLength,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsAdd_64f_Ctx)

-
64-bit floating point signal add signal, then clamp to saturated value.

- Parameters
-
**pSrc1**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pSrc2**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer). signal2 elements to be added to signal1 elements**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsAdd_32fc_Ctx(const[Npp32fc](https://docs.nvidia.com/nppdefs.html#c.Npp32fc)*pSrc1, const[Npp32fc](https://docs.nvidia.com/nppdefs.html#c.Npp32fc)*pSrc2,[Npp32fc](https://docs.nvidia.com/nppdefs.html#c.Npp32fc)*pDst, size_t nLength,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsAdd_32fc_Ctx)

-
32-bit complex floating point signal add signal, then clamp to saturated value.

- Parameters
-
**pSrc1**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pSrc2**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer). signal2 elements to be added to signal1 elements**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsAdd_64fc_Ctx(const[Npp64fc](https://docs.nvidia.com/nppdefs.html#c.Npp64fc)*pSrc1, const[Npp64fc](https://docs.nvidia.com/nppdefs.html#c.Npp64fc)*pSrc2,[Npp64fc](https://docs.nvidia.com/nppdefs.html#c.Npp64fc)*pDst, size_t nLength,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsAdd_64fc_Ctx)

-
64-bit complex floating point signal add signal, then clamp to saturated value.

- Parameters
-
**pSrc1**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pSrc2**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer). signal2 elements to be added to signal1 elements**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsAdd_8u16u_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc1, const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc2,[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pDst, size_t nLength,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsAdd_8u16u_Ctx)

-
8-bit unsigned char signal add signal with 16-bit unsigned result, then clamp to saturated value.

- Parameters
-
**pSrc1**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pSrc2**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer). signal2 elements to be added to signal1 elements**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsAdd_16s32f_Ctx(const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrc1, const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrc2,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pDst, size_t nLength,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsAdd_16s32f_Ctx)

-
16-bit signed short signal add signal with 32-bit floating point result, then clamp to saturated value.

- Parameters
-
**pSrc1**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pSrc2**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer). signal2 elements to be added to signal1 elements**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsAdd_8u_Sfs_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc1, const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc2,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, size_t nLength, int nScaleFactor,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsAdd_8u_Sfs_Ctx)

-
8-bit unsigned char add signal, scale, then clamp to saturated value.

- Parameters
-
**pSrc1**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pSrc2**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer), signal2 elements to be added to signal1 elements.**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nScaleFactor**–[Integer Result Scaling](https://docs.nvidia.com/introduction.html#general_conventions_lb_1integer_result_scaling).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsAdd_16u_Sfs_Ctx(const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrc1, const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrc2,[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pDst, size_t nLength, int nScaleFactor,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsAdd_16u_Sfs_Ctx)

-
16-bit unsigned short add signal, scale, then clamp to saturated value.

- Parameters
-
**pSrc1**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pSrc2**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer), signal2 elements to be added to signal1 elements.**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nScaleFactor**–[Integer Result Scaling](https://docs.nvidia.com/introduction.html#general_conventions_lb_1integer_result_scaling).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsAdd_16s_Sfs_Ctx(const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrc1, const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrc2,[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pDst, size_t nLength, int nScaleFactor,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsAdd_16s_Sfs_Ctx)

-
16-bit signed short add signal, scale, then clamp to saturated value.

- Parameters
-
**pSrc1**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pSrc2**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer), signal2 elements to be added to signal1 elements.**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nScaleFactor**–[Integer Result Scaling](https://docs.nvidia.com/introduction.html#general_conventions_lb_1integer_result_scaling).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsAdd_32s_Sfs_Ctx(const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pSrc1, const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pSrc2,[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pDst, size_t nLength, int nScaleFactor,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsAdd_32s_Sfs_Ctx)

-
32-bit signed integer add signal, scale, then clamp to saturated value.

- Parameters
-
**pSrc1**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pSrc2**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer), signal2 elements to be added to signal1 elements.**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nScaleFactor**–[Integer Result Scaling](https://docs.nvidia.com/introduction.html#general_conventions_lb_1integer_result_scaling).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsAdd_64s_Sfs_Ctx(const[Npp64s](https://docs.nvidia.com/nppdefs.html#c.Npp64s)*pSrc1, const[Npp64s](https://docs.nvidia.com/nppdefs.html#c.Npp64s)*pSrc2,[Npp64s](https://docs.nvidia.com/nppdefs.html#c.Npp64s)*pDst, size_t nLength, int nScaleFactor,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsAdd_64s_Sfs_Ctx)

-
64-bit signed integer add signal, scale, then clamp to saturated value.

- Parameters
-
**pSrc1**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pSrc2**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer), signal2 elements to be added to signal1 elements.**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nScaleFactor**–[Integer Result Scaling](https://docs.nvidia.com/introduction.html#general_conventions_lb_1integer_result_scaling).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsAdd_16sc_Sfs_Ctx(const[Npp16sc](https://docs.nvidia.com/nppdefs.html#c.Npp16sc)*pSrc1, const[Npp16sc](https://docs.nvidia.com/nppdefs.html#c.Npp16sc)*pSrc2,[Npp16sc](https://docs.nvidia.com/nppdefs.html#c.Npp16sc)*pDst, size_t nLength, int nScaleFactor,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsAdd_16sc_Sfs_Ctx)

-
16-bit signed complex short add signal, scale, then clamp to saturated value.

- Parameters
-
**pSrc1**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pSrc2**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer), signal2 elements to be added to signal1 elements.**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nScaleFactor**–[Integer Result Scaling](https://docs.nvidia.com/introduction.html#general_conventions_lb_1integer_result_scaling).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsAdd_32sc_Sfs_Ctx(const[Npp32sc](https://docs.nvidia.com/nppdefs.html#c.Npp32sc)*pSrc1, const[Npp32sc](https://docs.nvidia.com/nppdefs.html#c.Npp32sc)*pSrc2,[Npp32sc](https://docs.nvidia.com/nppdefs.html#c.Npp32sc)*pDst, size_t nLength, int nScaleFactor,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsAdd_32sc_Sfs_Ctx)

-
32-bit signed complex integer add signal, scale, then clamp to saturated value.

- Parameters
-
**pSrc1**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pSrc2**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer), signal2 elements to be added to signal1 elements.**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nScaleFactor**–[Integer Result Scaling](https://docs.nvidia.com/introduction.html#general_conventions_lb_1integer_result_scaling).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsAdd_16s_I_Ctx(const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrc,[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrcDst, size_t nLength,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsAdd_16s_I_Ctx)

-
16-bit signed short in place signal add signal, then clamp to saturated value.

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pSrcDst**–[In-Place Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1in_place_signal_pointer). signal2 elements to be added to signal1 elements**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsAdd_32f_I_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrcDst, size_t nLength,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsAdd_32f_I_Ctx)

-
32-bit floating point in place signal add signal, then clamp to saturated value.

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pSrcDst**–[In-Place Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1in_place_signal_pointer). signal2 elements to be added to signal1 elements**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsAdd_64f_I_Ctx(const[Npp64f](https://docs.nvidia.com/nppdefs.html#c.Npp64f)*pSrc,[Npp64f](https://docs.nvidia.com/nppdefs.html#c.Npp64f)*pSrcDst, size_t nLength,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsAdd_64f_I_Ctx)

-
64-bit floating point in place signal add signal, then clamp to saturated value.

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pSrcDst**–[In-Place Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1in_place_signal_pointer). signal2 elements to be added to signal1 elements**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsAdd_32fc_I_Ctx(const[Npp32fc](https://docs.nvidia.com/nppdefs.html#c.Npp32fc)*pSrc,[Npp32fc](https://docs.nvidia.com/nppdefs.html#c.Npp32fc)*pSrcDst, size_t nLength,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsAdd_32fc_I_Ctx)

-
32-bit complex floating point in place signal add signal, then clamp to saturated value.

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pSrcDst**–[In-Place Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1in_place_signal_pointer). signal2 elements to be added to signal1 elements**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsAdd_64fc_I_Ctx(const[Npp64fc](https://docs.nvidia.com/nppdefs.html#c.Npp64fc)*pSrc,[Npp64fc](https://docs.nvidia.com/nppdefs.html#c.Npp64fc)*pSrcDst, size_t nLength,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsAdd_64fc_I_Ctx)

-
64-bit complex floating point in place signal add signal, then clamp to saturated value.

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pSrcDst**–[In-Place Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1in_place_signal_pointer). signal2 elements to be added to signal1 elements**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsAdd_16s32s_I_Ctx(const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrc,[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pSrcDst, size_t nLength,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsAdd_16s32s_I_Ctx)

-
16/32-bit signed short in place signal add signal with 32-bit signed integer results, then clamp to saturated value.

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pSrcDst**–[In-Place Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1in_place_signal_pointer). signal2 elements to be added to signal1 elements**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsAdd_8u_ISfs_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrcDst, size_t nLength, int nScaleFactor,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsAdd_8u_ISfs_Ctx)

-
8-bit unsigned char in place signal add signal, with scaling, then clamp to saturated value.

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pSrcDst**–[In-Place Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1in_place_signal_pointer). signal2 elements to be added to signal1 elements**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nScaleFactor**–[Integer Result Scaling](https://docs.nvidia.com/introduction.html#general_conventions_lb_1integer_result_scaling).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsAdd_16u_ISfs_Ctx(const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrc,[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrcDst, size_t nLength, int nScaleFactor,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsAdd_16u_ISfs_Ctx)

-
16-bit unsigned short in place signal add signal, with scaling, then clamp to saturated value.

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pSrcDst**–[In-Place Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1in_place_signal_pointer). signal2 elements to be added to signal1 elements**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nScaleFactor**–[Integer Result Scaling](https://docs.nvidia.com/introduction.html#general_conventions_lb_1integer_result_scaling).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsAdd_16s_ISfs_Ctx(const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrc,[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrcDst, size_t nLength, int nScaleFactor,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsAdd_16s_ISfs_Ctx)

-
16-bit signed short in place signal add signal, with scaling, then clamp to saturated value.

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pSrcDst**–[In-Place Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1in_place_signal_pointer). signal2 elements to be added to signal1 elements**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nScaleFactor**–[Integer Result Scaling](https://docs.nvidia.com/introduction.html#general_conventions_lb_1integer_result_scaling).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsAdd_32s_ISfs_Ctx(const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pSrc,[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pSrcDst, size_t nLength, int nScaleFactor,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsAdd_32s_ISfs_Ctx)

-
32-bit signed integer in place signal add signal, with scaling, then clamp to saturated value.

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pSrcDst**–[In-Place Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1in_place_signal_pointer). signal2 elements to be added to signal1 elements**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nScaleFactor**–[Integer Result Scaling](https://docs.nvidia.com/introduction.html#general_conventions_lb_1integer_result_scaling).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsAdd_16sc_ISfs_Ctx(const[Npp16sc](https://docs.nvidia.com/nppdefs.html#c.Npp16sc)*pSrc,[Npp16sc](https://docs.nvidia.com/nppdefs.html#c.Npp16sc)*pSrcDst, size_t nLength, int nScaleFactor,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsAdd_16sc_ISfs_Ctx)

-
16-bit complex signed short in place signal add signal, with scaling, then clamp to saturated value.

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pSrcDst**–[In-Place Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1in_place_signal_pointer). signal2 elements to be added to signal1 elements**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nScaleFactor**–[Integer Result Scaling](https://docs.nvidia.com/introduction.html#general_conventions_lb_1integer_result_scaling).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsAdd_32sc_ISfs_Ctx(const[Npp32sc](https://docs.nvidia.com/nppdefs.html#c.Npp32sc)*pSrc,[Npp32sc](https://docs.nvidia.com/nppdefs.html#c.Npp32sc)*pSrcDst, size_t nLength, int nScaleFactor,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsAdd_32sc_ISfs_Ctx)

-
32-bit complex signed integer in place signal add signal, with scaling, then clamp to saturated value.

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pSrcDst**–[In-Place Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1in_place_signal_pointer). signal2 elements to be added to signal1 elements**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nScaleFactor**–[Integer Result Scaling](https://docs.nvidia.com/introduction.html#general_conventions_lb_1integer_result_scaling).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


### Signal AddProduct[](https://docs.nvidia.com#signal-addproduct)

#### AddProduct[](https://docs.nvidia.com#group__signal__addproduct_1signal_addproduct)

Adds sample by sample product of two signals to the destination signal.

Functions

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsAddProduct_32f_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc1, const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc2,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pDst, size_t nLength,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsAddProduct_32f_Ctx)

-
32-bit floating point signal add product of source signal times destination signal to destination signal, then clamp to saturated value.

- Parameters
-
**pSrc1**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pSrc2**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer). product of source1 and source2 signal elements to be added to destination elements**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsAddProduct_64f_Ctx(const[Npp64f](https://docs.nvidia.com/nppdefs.html#c.Npp64f)*pSrc1, const[Npp64f](https://docs.nvidia.com/nppdefs.html#c.Npp64f)*pSrc2,[Npp64f](https://docs.nvidia.com/nppdefs.html#c.Npp64f)*pDst, size_t nLength,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsAddProduct_64f_Ctx)

-
64-bit floating point signal add product of source signal times destination signal to destination signal, then clamp to saturated value.

- Parameters
-
**pSrc1**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pSrc2**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer). product of source1 and source2 signal elements to be added to destination elements**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsAddProduct_32fc_Ctx(const[Npp32fc](https://docs.nvidia.com/nppdefs.html#c.Npp32fc)*pSrc1, const[Npp32fc](https://docs.nvidia.com/nppdefs.html#c.Npp32fc)*pSrc2,[Npp32fc](https://docs.nvidia.com/nppdefs.html#c.Npp32fc)*pDst, size_t nLength,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsAddProduct_32fc_Ctx)

-
32-bit complex floating point signal add product of source signal times destination signal to destination signal, then clamp to saturated value.

- Parameters
-
**pSrc1**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pSrc2**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer). product of source1 and source2 signal elements to be added to destination elements**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsAddProduct_64fc_Ctx(const[Npp64fc](https://docs.nvidia.com/nppdefs.html#c.Npp64fc)*pSrc1, const[Npp64fc](https://docs.nvidia.com/nppdefs.html#c.Npp64fc)*pSrc2,[Npp64fc](https://docs.nvidia.com/nppdefs.html#c.Npp64fc)*pDst, size_t nLength,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsAddProduct_64fc_Ctx)

-
64-bit complex floating point signal add product of source signal times destination signal to destination signal, then clamp to saturated value.

- Parameters
-
**pSrc1**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pSrc2**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer). product of source1 and source2 signal elements to be added to destination elements**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsAddProduct_16s_Sfs_Ctx(const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrc1, const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrc2,[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pDst, size_t nLength, int nScaleFactor,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsAddProduct_16s_Sfs_Ctx)

-
16-bit signed short signal add product of source signal1 times source signal2 to destination signal, with scaling, then clamp to saturated value.

- Parameters
-
**pSrc1**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pSrc2**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer). product of source1 and source2 signal elements to be added to destination elements**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nScaleFactor**–[Integer Result Scaling](https://docs.nvidia.com/introduction.html#general_conventions_lb_1integer_result_scaling).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsAddProduct_32s_Sfs_Ctx(const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pSrc1, const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pSrc2,[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pDst, size_t nLength, int nScaleFactor,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsAddProduct_32s_Sfs_Ctx)

-
32-bit signed short signal add product of source signal1 times source signal2 to destination signal, with scaling, then clamp to saturated value.

- Parameters
-
**pSrc1**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pSrc2**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer). product of source1 and source2 signal elements to be added to destination elements**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nScaleFactor**–[Integer Result Scaling](https://docs.nvidia.com/introduction.html#general_conventions_lb_1integer_result_scaling).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsAddProduct_16s32s_Sfs_Ctx(const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrc1, const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrc2,[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pDst, size_t nLength, int nScaleFactor,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsAddProduct_16s32s_Sfs_Ctx)

-
16-bit signed short signal add product of source signal1 times source signal2 to 32-bit signed integer destination signal, with scaling, then clamp to saturated value.

- Parameters
-
**pSrc1**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pSrc2**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer). product of source1 and source2 signal elements to be added to destination elements**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nScaleFactor**–[Integer Result Scaling](https://docs.nvidia.com/introduction.html#general_conventions_lb_1integer_result_scaling).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


### Signal Mul[](https://docs.nvidia.com#signal-mul)

#### Mul[](https://docs.nvidia.com#group__signal__mul_1signal_mul)

Sample by sample multiplication the samples of two signals.

Functions

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsMul_16s_Ctx(const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrc1, const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrc2,[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pDst, size_t nLength,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsMul_16s_Ctx)

-
16-bit signed short signal times signal, then clamp to saturated value.

- Parameters
-
**pSrc1**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pSrc2**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer). signal2 elements to be multiplied by signal1 elements**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsMul_32f_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc1, const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc2,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pDst, size_t nLength,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsMul_32f_Ctx)

-
32-bit floating point signal times signal, then clamp to saturated value.

- Parameters
-
**pSrc1**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pSrc2**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer). signal2 elements to be multiplied by signal1 elements**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsMul_64f_Ctx(const[Npp64f](https://docs.nvidia.com/nppdefs.html#c.Npp64f)*pSrc1, const[Npp64f](https://docs.nvidia.com/nppdefs.html#c.Npp64f)*pSrc2,[Npp64f](https://docs.nvidia.com/nppdefs.html#c.Npp64f)*pDst, size_t nLength,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsMul_64f_Ctx)

-
64-bit floating point signal times signal, then clamp to saturated value.

- Parameters
-
**pSrc1**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pSrc2**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer). signal2 elements to be multiplied by signal1 elements**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsMul_32fc_Ctx(const[Npp32fc](https://docs.nvidia.com/nppdefs.html#c.Npp32fc)*pSrc1, const[Npp32fc](https://docs.nvidia.com/nppdefs.html#c.Npp32fc)*pSrc2,[Npp32fc](https://docs.nvidia.com/nppdefs.html#c.Npp32fc)*pDst, size_t nLength,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsMul_32fc_Ctx)

-
32-bit complex floating point signal times signal, then clamp to saturated value.

- Parameters
-
**pSrc1**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pSrc2**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer). signal2 elements to be multiplied by signal1 elements**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsMul_64fc_Ctx(const[Npp64fc](https://docs.nvidia.com/nppdefs.html#c.Npp64fc)*pSrc1, const[Npp64fc](https://docs.nvidia.com/nppdefs.html#c.Npp64fc)*pSrc2,[Npp64fc](https://docs.nvidia.com/nppdefs.html#c.Npp64fc)*pDst, size_t nLength,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsMul_64fc_Ctx)

-
64-bit complex floating point signal times signal, then clamp to saturated value.

- Parameters
-
**pSrc1**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pSrc2**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer). signal2 elements to be multiplied by signal1 elements**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsMul_8u16u_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc1, const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc2,[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pDst, size_t nLength,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsMul_8u16u_Ctx)

-
8-bit unsigned char signal times signal with 16-bit unsigned result, then clamp to saturated value.

- Parameters
-
**pSrc1**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pSrc2**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer). signal2 elements to be multiplied by signal1 elements**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsMul_16s32f_Ctx(const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrc1, const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrc2,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pDst, size_t nLength,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsMul_16s32f_Ctx)

-
16-bit signed short signal times signal with 32-bit floating point result, then clamp to saturated value.

- Parameters
-
**pSrc1**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pSrc2**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer). signal2 elements to be multiplied by signal1 elements**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsMul_32f32fc_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc1, const[Npp32fc](https://docs.nvidia.com/nppdefs.html#c.Npp32fc)*pSrc2,[Npp32fc](https://docs.nvidia.com/nppdefs.html#c.Npp32fc)*pDst, size_t nLength,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsMul_32f32fc_Ctx)

-
32-bit floating point signal times 32-bit complex floating point signal with complex 32-bit floating point result, then clamp to saturated value.

- Parameters
-
**pSrc1**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pSrc2**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer). signal2 elements to be multiplied by signal1 elements**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsMul_8u_Sfs_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc1, const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc2,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, size_t nLength, int nScaleFactor,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsMul_8u_Sfs_Ctx)

-
8-bit unsigned char signal times signal, scale, then clamp to saturated value.

- Parameters
-
**pSrc1**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pSrc2**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer), signal2 elements to be multiplied by signal1 elements.**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nScaleFactor**–[Integer Result Scaling](https://docs.nvidia.com/introduction.html#general_conventions_lb_1integer_result_scaling).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsMul_16u_Sfs_Ctx(const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrc1, const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrc2,[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pDst, size_t nLength, int nScaleFactor,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsMul_16u_Sfs_Ctx)

-
16-bit unsigned short signal time signal, scale, then clamp to saturated value.

- Parameters
-
**pSrc1**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pSrc2**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer), signal2 elements to be multiplied by signal1 elements.**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nScaleFactor**–[Integer Result Scaling](https://docs.nvidia.com/introduction.html#general_conventions_lb_1integer_result_scaling).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsMul_16s_Sfs_Ctx(const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrc1, const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrc2,[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pDst, size_t nLength, int nScaleFactor,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsMul_16s_Sfs_Ctx)

-
16-bit signed short signal times signal, scale, then clamp to saturated value.

- Parameters
-
**pSrc1**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pSrc2**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer), signal2 elements to be multiplied by signal1 elements.**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nScaleFactor**–[Integer Result Scaling](https://docs.nvidia.com/introduction.html#general_conventions_lb_1integer_result_scaling).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsMul_32s_Sfs_Ctx(const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pSrc1, const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pSrc2,[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pDst, size_t nLength, int nScaleFactor,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsMul_32s_Sfs_Ctx)

-
32-bit signed integer signal times signal, scale, then clamp to saturated value.

- Parameters
-
**pSrc1**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pSrc2**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer), signal2 elements to be multiplied by signal1 elements.**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nScaleFactor**–[Integer Result Scaling](https://docs.nvidia.com/introduction.html#general_conventions_lb_1integer_result_scaling).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsMul_16sc_Sfs_Ctx(const[Npp16sc](https://docs.nvidia.com/nppdefs.html#c.Npp16sc)*pSrc1, const[Npp16sc](https://docs.nvidia.com/nppdefs.html#c.Npp16sc)*pSrc2,[Npp16sc](https://docs.nvidia.com/nppdefs.html#c.Npp16sc)*pDst, size_t nLength, int nScaleFactor,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsMul_16sc_Sfs_Ctx)

-
16-bit signed complex short signal times signal, scale, then clamp to saturated value.

- Parameters
-
**pSrc1**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pSrc2**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer), signal2 elements to be multiplied by signal1 elements.**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nScaleFactor**–[Integer Result Scaling](https://docs.nvidia.com/introduction.html#general_conventions_lb_1integer_result_scaling).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsMul_32sc_Sfs_Ctx(const[Npp32sc](https://docs.nvidia.com/nppdefs.html#c.Npp32sc)*pSrc1, const[Npp32sc](https://docs.nvidia.com/nppdefs.html#c.Npp32sc)*pSrc2,[Npp32sc](https://docs.nvidia.com/nppdefs.html#c.Npp32sc)*pDst, size_t nLength, int nScaleFactor,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsMul_32sc_Sfs_Ctx)

-
32-bit signed complex integer signal times signal, scale, then clamp to saturated value.

- Parameters
-
**pSrc1**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pSrc2**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer), signal2 elements to be multiplied by signal1 elements.**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nScaleFactor**–[Integer Result Scaling](https://docs.nvidia.com/introduction.html#general_conventions_lb_1integer_result_scaling).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsMul_16u16s_Sfs_Ctx(const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrc1, const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrc2,[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pDst, size_t nLength, int nScaleFactor,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsMul_16u16s_Sfs_Ctx)

-
16-bit unsigned short signal times 16-bit signed short signal, scale, then clamp to 16-bit signed saturated value.

- Parameters
-
**pSrc1**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pSrc2**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer), signal2 elements to be multiplied by signal1 elements.**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nScaleFactor**–[Integer Result Scaling](https://docs.nvidia.com/introduction.html#general_conventions_lb_1integer_result_scaling).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsMul_16s32s_Sfs_Ctx(const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrc1, const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrc2,[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pDst, size_t nLength, int nScaleFactor,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsMul_16s32s_Sfs_Ctx)

-
16-bit signed short signal times signal, scale, then clamp to 32-bit signed saturated value.

- Parameters
-
**pSrc1**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pSrc2**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer), signal2 elements to be multiplied by signal1 elements.**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nScaleFactor**–[Integer Result Scaling](https://docs.nvidia.com/introduction.html#general_conventions_lb_1integer_result_scaling).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsMul_32s32sc_Sfs_Ctx(const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pSrc1, const[Npp32sc](https://docs.nvidia.com/nppdefs.html#c.Npp32sc)*pSrc2,[Npp32sc](https://docs.nvidia.com/nppdefs.html#c.Npp32sc)*pDst, size_t nLength, int nScaleFactor,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsMul_32s32sc_Sfs_Ctx)

-
32-bit signed integer signal times 32-bit complex signed integer signal, scale, then clamp to 32-bit complex integer saturated value.

- Parameters
-
**pSrc1**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pSrc2**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer), signal2 elements to be multiplied by signal1 elements.**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nScaleFactor**–[Integer Result Scaling](https://docs.nvidia.com/introduction.html#general_conventions_lb_1integer_result_scaling).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsMul_Low_32s_Sfs_Ctx(const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pSrc1, const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pSrc2,[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pDst, size_t nLength, int nScaleFactor,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsMul_Low_32s_Sfs_Ctx)

-
32-bit signed integer signal times signal, scale, then clamp to saturated value.

- Parameters
-
**pSrc1**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pSrc2**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer), signal2 elements to be multiplied by signal1 elements.**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nScaleFactor**–[Integer Result Scaling](https://docs.nvidia.com/introduction.html#general_conventions_lb_1integer_result_scaling).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsMul_16s_I_Ctx(const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrc,[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrcDst, size_t nLength,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsMul_16s_I_Ctx)

-
16-bit signed short in place signal times signal, then clamp to saturated value.

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pSrcDst**–[In-Place Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1in_place_signal_pointer). signal2 elements to be multiplied by signal1 elements**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsMul_32f_I_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrcDst, size_t nLength,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsMul_32f_I_Ctx)

-
32-bit floating point in place signal times signal, then clamp to saturated value.

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pSrcDst**–[In-Place Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1in_place_signal_pointer). signal2 elements to be multiplied by signal1 elements**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsMul_64f_I_Ctx(const[Npp64f](https://docs.nvidia.com/nppdefs.html#c.Npp64f)*pSrc,[Npp64f](https://docs.nvidia.com/nppdefs.html#c.Npp64f)*pSrcDst, size_t nLength,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsMul_64f_I_Ctx)

-
64-bit floating point in place signal times signal, then clamp to saturated value.

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pSrcDst**–[In-Place Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1in_place_signal_pointer). signal2 elements to be multiplied by signal1 elements**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsMul_32fc_I_Ctx(const[Npp32fc](https://docs.nvidia.com/nppdefs.html#c.Npp32fc)*pSrc,[Npp32fc](https://docs.nvidia.com/nppdefs.html#c.Npp32fc)*pSrcDst, size_t nLength,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsMul_32fc_I_Ctx)

-
32-bit complex floating point in place signal times signal, then clamp to saturated value.

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pSrcDst**–[In-Place Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1in_place_signal_pointer). signal2 elements to be multiplied by signal1 elements**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsMul_64fc_I_Ctx(const[Npp64fc](https://docs.nvidia.com/nppdefs.html#c.Npp64fc)*pSrc,[Npp64fc](https://docs.nvidia.com/nppdefs.html#c.Npp64fc)*pSrcDst, size_t nLength,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsMul_64fc_I_Ctx)

-
64-bit complex floating point in place signal times signal, then clamp to saturated value.

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pSrcDst**–[In-Place Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1in_place_signal_pointer). signal2 elements to be multiplied by signal1 elements**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsMul_32f32fc_I_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc,[Npp32fc](https://docs.nvidia.com/nppdefs.html#c.Npp32fc)*pSrcDst, size_t nLength,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsMul_32f32fc_I_Ctx)

-
32-bit complex floating point in place signal times 32-bit floating point signal, then clamp to 32-bit complex floating point saturated value.

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pSrcDst**–[In-Place Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1in_place_signal_pointer). signal2 elements to be multiplied by signal1 elements**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsMul_8u_ISfs_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrcDst, size_t nLength, int nScaleFactor,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsMul_8u_ISfs_Ctx)

-
8-bit unsigned char in place signal times signal, with scaling, then clamp to saturated value.

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pSrcDst**–[In-Place Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1in_place_signal_pointer). signal2 elements to be multiplied by signal1 elements**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nScaleFactor**–[Integer Result Scaling](https://docs.nvidia.com/introduction.html#general_conventions_lb_1integer_result_scaling).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsMul_16u_ISfs_Ctx(const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrc,[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrcDst, size_t nLength, int nScaleFactor,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsMul_16u_ISfs_Ctx)

-
16-bit unsigned short in place signal times signal, with scaling, then clamp to saturated value.

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pSrcDst**–[In-Place Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1in_place_signal_pointer). signal2 elements to be multiplied by signal1 elements**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nScaleFactor**–[Integer Result Scaling](https://docs.nvidia.com/introduction.html#general_conventions_lb_1integer_result_scaling).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsMul_16s_ISfs_Ctx(const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrc,[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrcDst, size_t nLength, int nScaleFactor,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsMul_16s_ISfs_Ctx)

-
16-bit signed short in place signal times signal, with scaling, then clamp to saturated value.

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pSrcDst**–[In-Place Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1in_place_signal_pointer). signal2 elements to be multiplied by signal1 elements**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nScaleFactor**–[Integer Result Scaling](https://docs.nvidia.com/introduction.html#general_conventions_lb_1integer_result_scaling).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsMul_32s_ISfs_Ctx(const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pSrc,[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pSrcDst, size_t nLength, int nScaleFactor,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsMul_32s_ISfs_Ctx)

-
32-bit signed integer in place signal times signal, with scaling, then clamp to saturated value.

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pSrcDst**–[In-Place Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1in_place_signal_pointer). signal2 elements to be multiplied by signal1 elements**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nScaleFactor**–[Integer Result Scaling](https://docs.nvidia.com/introduction.html#general_conventions_lb_1integer_result_scaling).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsMul_16sc_ISfs_Ctx(const[Npp16sc](https://docs.nvidia.com/nppdefs.html#c.Npp16sc)*pSrc,[Npp16sc](https://docs.nvidia.com/nppdefs.html#c.Npp16sc)*pSrcDst, size_t nLength, int nScaleFactor,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsMul_16sc_ISfs_Ctx)

-
16-bit complex signed short in place signal times signal, with scaling, then clamp to saturated value.

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pSrcDst**–[In-Place Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1in_place_signal_pointer). signal2 elements to be multiplied by signal1 elements**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nScaleFactor**–[Integer Result Scaling](https://docs.nvidia.com/introduction.html#general_conventions_lb_1integer_result_scaling).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsMul_32sc_ISfs_Ctx(const[Npp32sc](https://docs.nvidia.com/nppdefs.html#c.Npp32sc)*pSrc,[Npp32sc](https://docs.nvidia.com/nppdefs.html#c.Npp32sc)*pSrcDst, size_t nLength, int nScaleFactor,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsMul_32sc_ISfs_Ctx)

-
32-bit complex signed integer in place signal times signal, with scaling, then clamp to saturated value.

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pSrcDst**–[In-Place Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1in_place_signal_pointer). signal2 elements to be multiplied by signal1 elements**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nScaleFactor**–[Integer Result Scaling](https://docs.nvidia.com/introduction.html#general_conventions_lb_1integer_result_scaling).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsMul_32s32sc_ISfs_Ctx(const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pSrc,[Npp32sc](https://docs.nvidia.com/nppdefs.html#c.Npp32sc)*pSrcDst, size_t nLength, int nScaleFactor,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsMul_32s32sc_ISfs_Ctx)

-
32-bit complex signed integer in place signal times 32-bit signed integer signal, with scaling, then clamp to saturated value.

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pSrcDst**–[In-Place Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1in_place_signal_pointer). signal2 elements to be multiplied by signal1 elements**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nScaleFactor**–[Integer Result Scaling](https://docs.nvidia.com/introduction.html#general_conventions_lb_1integer_result_scaling).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


### Signal Sub[](https://docs.nvidia.com#signal-sub)

#### Sub[](https://docs.nvidia.com#group__signal__sub_1signal_sub)

Sample by sample subtraction of the samples of two signals.

Functions

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsSub_16s_Ctx(const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrc1, const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrc2,[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pDst, size_t nLength,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsSub_16s_Ctx)

-
16-bit signed short signal subtract signal, then clamp to saturated value.

- Parameters
-
**pSrc1**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pSrc2**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer). signal1 elements to be subtracted from signal2 elements**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsSub_32f_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc1, const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc2,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pDst, size_t nLength,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsSub_32f_Ctx)

-
32-bit floating point signal subtract signal, then clamp to saturated value.

- Parameters
-
**pSrc1**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pSrc2**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer). signal1 elements to be subtracted from signal2 elements**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsSub_64f_Ctx(const[Npp64f](https://docs.nvidia.com/nppdefs.html#c.Npp64f)*pSrc1, const[Npp64f](https://docs.nvidia.com/nppdefs.html#c.Npp64f)*pSrc2,[Npp64f](https://docs.nvidia.com/nppdefs.html#c.Npp64f)*pDst, size_t nLength,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsSub_64f_Ctx)

-
64-bit floating point signal subtract signal, then clamp to saturated value.

- Parameters
-
**pSrc1**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pSrc2**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer). signal1 elements to be subtracted from signal2 elements**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsSub_32fc_Ctx(const[Npp32fc](https://docs.nvidia.com/nppdefs.html#c.Npp32fc)*pSrc1, const[Npp32fc](https://docs.nvidia.com/nppdefs.html#c.Npp32fc)*pSrc2,[Npp32fc](https://docs.nvidia.com/nppdefs.html#c.Npp32fc)*pDst, size_t nLength,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsSub_32fc_Ctx)

-
32-bit complex floating point signal subtract signal, then clamp to saturated value.

- Parameters
-
**pSrc1**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pSrc2**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer). signal1 elements to be subtracted from signal2 elements**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsSub_64fc_Ctx(const[Npp64fc](https://docs.nvidia.com/nppdefs.html#c.Npp64fc)*pSrc1, const[Npp64fc](https://docs.nvidia.com/nppdefs.html#c.Npp64fc)*pSrc2,[Npp64fc](https://docs.nvidia.com/nppdefs.html#c.Npp64fc)*pDst, size_t nLength,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsSub_64fc_Ctx)

-
64-bit complex floating point signal subtract signal, then clamp to saturated value.

- Parameters
-
**pSrc1**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pSrc2**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer). signal1 elements to be subtracted from signal2 elements**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsSub_16s32f_Ctx(const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrc1, const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrc2,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pDst, size_t nLength,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsSub_16s32f_Ctx)

-
16-bit signed short signal subtract 16-bit signed short signal, then clamp and convert to 32-bit floating point saturated value.

- Parameters
-
**pSrc1**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pSrc2**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer). signal1 elements to be subtracted from signal2 elements**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsSub_8u_Sfs_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc1, const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc2,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, size_t nLength, int nScaleFactor,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsSub_8u_Sfs_Ctx)

-
8-bit unsigned char signal subtract signal, scale, then clamp to saturated value.

- Parameters
-
**pSrc1**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pSrc2**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer), signal1 elements to be subtracted from signal2 elements.**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nScaleFactor**–[Integer Result Scaling](https://docs.nvidia.com/introduction.html#general_conventions_lb_1integer_result_scaling).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsSub_16u_Sfs_Ctx(const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrc1, const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrc2,[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pDst, size_t nLength, int nScaleFactor,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsSub_16u_Sfs_Ctx)

-
16-bit unsigned short signal subtract signal, scale, then clamp to saturated value.

- Parameters
-
**pSrc1**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pSrc2**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer), signal1 elements to be subtracted from signal2 elements.**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nScaleFactor**–[Integer Result Scaling](https://docs.nvidia.com/introduction.html#general_conventions_lb_1integer_result_scaling).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsSub_16s_Sfs_Ctx(const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrc1, const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrc2,[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pDst, size_t nLength, int nScaleFactor,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsSub_16s_Sfs_Ctx)

-
16-bit signed short signal subtract signal, scale, then clamp to saturated value.

- Parameters
-
**pSrc1**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pSrc2**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer), signal1 elements to be subtracted from signal2 elements.**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nScaleFactor**–[Integer Result Scaling](https://docs.nvidia.com/introduction.html#general_conventions_lb_1integer_result_scaling).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsSub_32s_Sfs_Ctx(const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pSrc1, const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pSrc2,[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pDst, size_t nLength, int nScaleFactor,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsSub_32s_Sfs_Ctx)

-
32-bit signed integer signal subtract signal, scale, then clamp to saturated value.

- Parameters
-
**pSrc1**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pSrc2**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer), signal1 elements to be subtracted from signal2 elements.**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nScaleFactor**–[Integer Result Scaling](https://docs.nvidia.com/introduction.html#general_conventions_lb_1integer_result_scaling).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsSub_16sc_Sfs_Ctx(const[Npp16sc](https://docs.nvidia.com/nppdefs.html#c.Npp16sc)*pSrc1, const[Npp16sc](https://docs.nvidia.com/nppdefs.html#c.Npp16sc)*pSrc2,[Npp16sc](https://docs.nvidia.com/nppdefs.html#c.Npp16sc)*pDst, size_t nLength, int nScaleFactor,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsSub_16sc_Sfs_Ctx)

-
16-bit signed complex short signal subtract signal, scale, then clamp to saturated value.

- Parameters
-
**pSrc1**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pSrc2**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer), signal1 elements to be subtracted from signal2 elements.**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nScaleFactor**–[Integer Result Scaling](https://docs.nvidia.com/introduction.html#general_conventions_lb_1integer_result_scaling).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsSub_32sc_Sfs_Ctx(const[Npp32sc](https://docs.nvidia.com/nppdefs.html#c.Npp32sc)*pSrc1, const[Npp32sc](https://docs.nvidia.com/nppdefs.html#c.Npp32sc)*pSrc2,[Npp32sc](https://docs.nvidia.com/nppdefs.html#c.Npp32sc)*pDst, size_t nLength, int nScaleFactor,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsSub_32sc_Sfs_Ctx)

-
32-bit signed complex integer signal subtract signal, scale, then clamp to saturated value.

- Parameters
-
**pSrc1**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pSrc2**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer), signal1 elements to be subtracted from signal2 elements.**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nScaleFactor**–[Integer Result Scaling](https://docs.nvidia.com/introduction.html#general_conventions_lb_1integer_result_scaling).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsSub_16s_I_Ctx(const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrc,[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrcDst, size_t nLength,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsSub_16s_I_Ctx)

-
16-bit signed short in place signal subtract signal, then clamp to saturated value.

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pSrcDst**–[In-Place Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1in_place_signal_pointer). signal1 elements to be subtracted from signal2 elements**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsSub_32f_I_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrcDst, size_t nLength,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsSub_32f_I_Ctx)

-
32-bit floating point in place signal subtract signal, then clamp to saturated value.

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pSrcDst**–[In-Place Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1in_place_signal_pointer). signal1 elements to be subtracted from signal2 elements**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsSub_64f_I_Ctx(const[Npp64f](https://docs.nvidia.com/nppdefs.html#c.Npp64f)*pSrc,[Npp64f](https://docs.nvidia.com/nppdefs.html#c.Npp64f)*pSrcDst, size_t nLength,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsSub_64f_I_Ctx)

-
64-bit floating point in place signal subtract signal, then clamp to saturated value.

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pSrcDst**–[In-Place Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1in_place_signal_pointer). signal1 elements to be subtracted from signal2 elements**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsSub_32fc_I_Ctx(const[Npp32fc](https://docs.nvidia.com/nppdefs.html#c.Npp32fc)*pSrc,[Npp32fc](https://docs.nvidia.com/nppdefs.html#c.Npp32fc)*pSrcDst, size_t nLength,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsSub_32fc_I_Ctx)

-
32-bit complex floating point in place signal subtract signal, then clamp to saturated value.

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pSrcDst**–[In-Place Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1in_place_signal_pointer). signal1 elements to be subtracted from signal2 elements**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsSub_64fc_I_Ctx(const[Npp64fc](https://docs.nvidia.com/nppdefs.html#c.Npp64fc)*pSrc,[Npp64fc](https://docs.nvidia.com/nppdefs.html#c.Npp64fc)*pSrcDst, size_t nLength,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsSub_64fc_I_Ctx)

-
64-bit complex floating point in place signal subtract signal, then clamp to saturated value.

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pSrcDst**–[In-Place Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1in_place_signal_pointer). signal1 elements to be subtracted from signal2 elements**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsSub_8u_ISfs_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrcDst, size_t nLength, int nScaleFactor,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsSub_8u_ISfs_Ctx)

-
8-bit unsigned char in place signal subtract signal, with scaling, then clamp to saturated value.

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pSrcDst**–[In-Place Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1in_place_signal_pointer). signal1 elements to be subtracted from signal2 elements**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nScaleFactor**–[Integer Result Scaling](https://docs.nvidia.com/introduction.html#general_conventions_lb_1integer_result_scaling).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsSub_16u_ISfs_Ctx(const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrc,[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrcDst, size_t nLength, int nScaleFactor,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsSub_16u_ISfs_Ctx)

-
16-bit unsigned short in place signal subtract signal, with scaling, then clamp to saturated value.

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pSrcDst**–[In-Place Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1in_place_signal_pointer). signal1 elements to be subtracted from signal2 elements**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nScaleFactor**–[Integer Result Scaling](https://docs.nvidia.com/introduction.html#general_conventions_lb_1integer_result_scaling).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsSub_16s_ISfs_Ctx(const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrc,[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrcDst, size_t nLength, int nScaleFactor,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsSub_16s_ISfs_Ctx)

-
16-bit signed short in place signal subtract signal, with scaling, then clamp to saturated value.

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pSrcDst**–[In-Place Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1in_place_signal_pointer). signal1 elements to be subtracted from signal2 elements**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nScaleFactor**–[Integer Result Scaling](https://docs.nvidia.com/introduction.html#general_conventions_lb_1integer_result_scaling).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsSub_32s_ISfs_Ctx(const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pSrc,[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pSrcDst, size_t nLength, int nScaleFactor,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsSub_32s_ISfs_Ctx)

-
32-bit signed integer in place signal subtract signal, with scaling, then clamp to saturated value.

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pSrcDst**–[In-Place Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1in_place_signal_pointer). signal1 elements to be subtracted from signal2 elements**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nScaleFactor**–[Integer Result Scaling](https://docs.nvidia.com/introduction.html#general_conventions_lb_1integer_result_scaling).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsSub_16sc_ISfs_Ctx(const[Npp16sc](https://docs.nvidia.com/nppdefs.html#c.Npp16sc)*pSrc,[Npp16sc](https://docs.nvidia.com/nppdefs.html#c.Npp16sc)*pSrcDst, size_t nLength, int nScaleFactor,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsSub_16sc_ISfs_Ctx)

-
16-bit complex signed short in place signal subtract signal, with scaling, then clamp to saturated value.

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pSrcDst**–[In-Place Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1in_place_signal_pointer). signal1 elements to be subtracted from signal2 elements**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nScaleFactor**–[Integer Result Scaling](https://docs.nvidia.com/introduction.html#general_conventions_lb_1integer_result_scaling).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsSub_32sc_ISfs_Ctx(const[Npp32sc](https://docs.nvidia.com/nppdefs.html#c.Npp32sc)*pSrc,[Npp32sc](https://docs.nvidia.com/nppdefs.html#c.Npp32sc)*pSrcDst, size_t nLength, int nScaleFactor,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsSub_32sc_ISfs_Ctx)

-
32-bit complex signed integer in place signal subtract signal, with scaling, then clamp to saturated value.

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pSrcDst**–[In-Place Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1in_place_signal_pointer). signal1 elements to be subtracted from signal2 elements**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nScaleFactor**–[Integer Result Scaling](https://docs.nvidia.com/introduction.html#general_conventions_lb_1integer_result_scaling).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


### Signal Div[](https://docs.nvidia.com#signal-div)

#### Div[](https://docs.nvidia.com#group__signal__div_1signal_div)

Sample by sample division of the samples of two signals.

Functions

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsDiv_8u_Sfs_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc1, const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc2,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, size_t nLength, int nScaleFactor,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsDiv_8u_Sfs_Ctx)

-
8-bit unsigned char signal divide signal, scale, then clamp to saturated value.

- Parameters
-
**pSrc1**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pSrc2**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer), signal1 divisor elements to be divided into signal2 dividend elements.**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nScaleFactor**–[Integer Result Scaling](https://docs.nvidia.com/introduction.html#general_conventions_lb_1integer_result_scaling).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsDiv_16u_Sfs_Ctx(const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrc1, const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrc2,[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pDst, size_t nLength, int nScaleFactor,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsDiv_16u_Sfs_Ctx)

-
16-bit unsigned short signal divide signal, scale, then clamp to saturated value.

- Parameters
-
**pSrc1**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pSrc2**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer), signal1 divisor elements to be divided into signal2 dividend elements.**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nScaleFactor**–[Integer Result Scaling](https://docs.nvidia.com/introduction.html#general_conventions_lb_1integer_result_scaling).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsDiv_16s_Sfs_Ctx(const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrc1, const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrc2,[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pDst, size_t nLength, int nScaleFactor,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsDiv_16s_Sfs_Ctx)

-
16-bit signed short signal divide signal, scale, then clamp to saturated value.

- Parameters
-
**pSrc1**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pSrc2**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer), signal1 divisor elements to be divided into signal2 dividend elements.**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nScaleFactor**–[Integer Result Scaling](https://docs.nvidia.com/introduction.html#general_conventions_lb_1integer_result_scaling).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsDiv_32s_Sfs_Ctx(const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pSrc1, const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pSrc2,[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pDst, size_t nLength, int nScaleFactor,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsDiv_32s_Sfs_Ctx)

-
32-bit signed integer signal divide signal, scale, then clamp to saturated value.

- Parameters
-
**pSrc1**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pSrc2**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer), signal1 divisor elements to be divided into signal2 dividend elements.**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nScaleFactor**–[Integer Result Scaling](https://docs.nvidia.com/introduction.html#general_conventions_lb_1integer_result_scaling).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsDiv_16sc_Sfs_Ctx(const[Npp16sc](https://docs.nvidia.com/nppdefs.html#c.Npp16sc)*pSrc1, const[Npp16sc](https://docs.nvidia.com/nppdefs.html#c.Npp16sc)*pSrc2,[Npp16sc](https://docs.nvidia.com/nppdefs.html#c.Npp16sc)*pDst, size_t nLength, int nScaleFactor,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsDiv_16sc_Sfs_Ctx)

-
16-bit signed complex short signal divide signal, scale, then clamp to saturated value.

- Parameters
-
**pSrc1**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pSrc2**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer), signal1 divisor elements to be divided into signal2 dividend elements.**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nScaleFactor**–[Integer Result Scaling](https://docs.nvidia.com/introduction.html#general_conventions_lb_1integer_result_scaling).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsDiv_32s16s_Sfs_Ctx(const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrc1, const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pSrc2,[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pDst, size_t nLength, int nScaleFactor,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsDiv_32s16s_Sfs_Ctx)

-
32-bit signed integer signal divided by 16-bit signed short signal, scale, then clamp to 16-bit signed short saturated value.

- Parameters
-
**pSrc1**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pSrc2**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer), signal1 divisor elements to be divided into signal2 dividend elements.**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nScaleFactor**–[Integer Result Scaling](https://docs.nvidia.com/introduction.html#general_conventions_lb_1integer_result_scaling).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsDiv_32f_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc1, const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc2,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pDst, size_t nLength,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsDiv_32f_Ctx)

-
32-bit floating point signal divide signal, then clamp to saturated value.

- Parameters
-
**pSrc1**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pSrc2**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer), signal1 divisor elements to be divided into signal2 dividend elements.**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsDiv_64f_Ctx(const[Npp64f](https://docs.nvidia.com/nppdefs.html#c.Npp64f)*pSrc1, const[Npp64f](https://docs.nvidia.com/nppdefs.html#c.Npp64f)*pSrc2,[Npp64f](https://docs.nvidia.com/nppdefs.html#c.Npp64f)*pDst, size_t nLength,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsDiv_64f_Ctx)

-
64-bit floating point signal divide signal, then clamp to saturated value.

- Parameters
-
**pSrc1**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pSrc2**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer), signal1 divisor elements to be divided into signal2 dividend elements.**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsDiv_32fc_Ctx(const[Npp32fc](https://docs.nvidia.com/nppdefs.html#c.Npp32fc)*pSrc1, const[Npp32fc](https://docs.nvidia.com/nppdefs.html#c.Npp32fc)*pSrc2,[Npp32fc](https://docs.nvidia.com/nppdefs.html#c.Npp32fc)*pDst, size_t nLength,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsDiv_32fc_Ctx)

-
32-bit complex floating point signal divide signal, then clamp to saturated value.

- Parameters
-
**pSrc1**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pSrc2**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer), signal1 divisor elements to be divided into signal2 dividend elements.**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsDiv_64fc_Ctx(const[Npp64fc](https://docs.nvidia.com/nppdefs.html#c.Npp64fc)*pSrc1, const[Npp64fc](https://docs.nvidia.com/nppdefs.html#c.Npp64fc)*pSrc2,[Npp64fc](https://docs.nvidia.com/nppdefs.html#c.Npp64fc)*pDst, size_t nLength,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsDiv_64fc_Ctx)

-
64-bit complex floating point signal divide signal, then clamp to saturated value.

- Parameters
-
**pSrc1**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pSrc2**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer), signal1 divisor elements to be divided into signal2 dividend elements.**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsDiv_8u_ISfs_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrcDst, size_t nLength, int nScaleFactor,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsDiv_8u_ISfs_Ctx)

-
8-bit unsigned char in place signal divide signal, with scaling, then clamp to saturated value.

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pSrcDst**–[In-Place Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1in_place_signal_pointer). signal1 divisor elements to be divided into signal2 dividend elements**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nScaleFactor**–[Integer Result Scaling](https://docs.nvidia.com/introduction.html#general_conventions_lb_1integer_result_scaling).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsDiv_16u_ISfs_Ctx(const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrc,[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrcDst, size_t nLength, int nScaleFactor,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsDiv_16u_ISfs_Ctx)

-
16-bit unsigned short in place signal divide signal, with scaling, then clamp to saturated value.

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pSrcDst**–[In-Place Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1in_place_signal_pointer). signal1 divisor elements to be divided into signal2 dividend elements**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nScaleFactor**–[Integer Result Scaling](https://docs.nvidia.com/introduction.html#general_conventions_lb_1integer_result_scaling).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsDiv_16s_ISfs_Ctx(const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrc,[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrcDst, size_t nLength, int nScaleFactor,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsDiv_16s_ISfs_Ctx)

-
16-bit signed short in place signal divide signal, with scaling, then clamp to saturated value.

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pSrcDst**–[In-Place Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1in_place_signal_pointer). signal1 divisor elements to be divided into signal2 dividend elements**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nScaleFactor**–[Integer Result Scaling](https://docs.nvidia.com/introduction.html#general_conventions_lb_1integer_result_scaling).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsDiv_16sc_ISfs_Ctx(const[Npp16sc](https://docs.nvidia.com/nppdefs.html#c.Npp16sc)*pSrc,[Npp16sc](https://docs.nvidia.com/nppdefs.html#c.Npp16sc)*pSrcDst, size_t nLength, int nScaleFactor,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsDiv_16sc_ISfs_Ctx)

-
16-bit complex signed short in place signal divide signal, with scaling, then clamp to saturated value.

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pSrcDst**–[In-Place Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1in_place_signal_pointer). signal1 divisor elements to be divided into signal2 dividend elements**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nScaleFactor**–[Integer Result Scaling](https://docs.nvidia.com/introduction.html#general_conventions_lb_1integer_result_scaling).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsDiv_32s_ISfs_Ctx(const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pSrc,[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pSrcDst, size_t nLength, int nScaleFactor,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsDiv_32s_ISfs_Ctx)

-
32-bit signed integer in place signal divide signal, with scaling, then clamp to saturated value.

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pSrcDst**–[In-Place Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1in_place_signal_pointer). signal1 divisor elements to be divided into signal2 dividend elements**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nScaleFactor**–[Integer Result Scaling](https://docs.nvidia.com/introduction.html#general_conventions_lb_1integer_result_scaling).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsDiv_32f_I_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrcDst, size_t nLength,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsDiv_32f_I_Ctx)

-
32-bit floating point in place signal divide signal, then clamp to saturated value.

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pSrcDst**–[In-Place Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1in_place_signal_pointer). signal1 divisor elements to be divided into signal2 dividend elements**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsDiv_64f_I_Ctx(const[Npp64f](https://docs.nvidia.com/nppdefs.html#c.Npp64f)*pSrc,[Npp64f](https://docs.nvidia.com/nppdefs.html#c.Npp64f)*pSrcDst, size_t nLength,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsDiv_64f_I_Ctx)

-
64-bit floating point in place signal divide signal, then clamp to saturated value.

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pSrcDst**–[In-Place Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1in_place_signal_pointer). signal1 divisor elements to be divided into signal2 dividend elements**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsDiv_32fc_I_Ctx(const[Npp32fc](https://docs.nvidia.com/nppdefs.html#c.Npp32fc)*pSrc,[Npp32fc](https://docs.nvidia.com/nppdefs.html#c.Npp32fc)*pSrcDst, size_t nLength,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsDiv_32fc_I_Ctx)

-
32-bit complex floating point in place signal divide signal, then clamp to saturated value.

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pSrcDst**–[In-Place Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1in_place_signal_pointer). signal1 divisor elements to be divided into signal2 dividend elements**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsDiv_64fc_I_Ctx(const[Npp64fc](https://docs.nvidia.com/nppdefs.html#c.Npp64fc)*pSrc,[Npp64fc](https://docs.nvidia.com/nppdefs.html#c.Npp64fc)*pSrcDst, size_t nLength,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsDiv_64fc_I_Ctx)

-
64-bit complex floating point in place signal divide signal, then clamp to saturated value.

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pSrcDst**–[In-Place Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1in_place_signal_pointer). signal1 divisor elements to be divided into signal2 dividend elements**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


### Signal Div Round[](https://docs.nvidia.com#signal-div-round)

#### Div_Round[](https://docs.nvidia.com#group__signal__divround_1signal_divround)

Sample by sample division of the samples of two signals with rounding.

Functions

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsDiv_Round_8u_Sfs_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc1, const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc2,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, size_t nLength,[NppRoundMode](https://docs.nvidia.com/nppdefs.html#c.NppRoundMode)nRndMode, int nScaleFactor,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsDiv_Round_8u_Sfs_Ctx)

-
8-bit unsigned char signal divide signal, scale, then clamp to saturated value.

- Parameters
-
**pSrc1**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pSrc2**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer), signal1 divisor elements to be divided into signal2 dividend elements.**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nRndMode**– various rounding modes.**nScaleFactor**–[Integer Result Scaling](https://docs.nvidia.com/introduction.html#general_conventions_lb_1integer_result_scaling).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsDiv_Round_16u_Sfs_Ctx(const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrc1, const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrc2,[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pDst, size_t nLength,[NppRoundMode](https://docs.nvidia.com/nppdefs.html#c.NppRoundMode)nRndMode, int nScaleFactor,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsDiv_Round_16u_Sfs_Ctx)

-
16-bit unsigned short signal divide signal, scale, round, then clamp to saturated value.

- Parameters
-
**pSrc1**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pSrc2**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer), signal1 divisor elements to be divided into signal2 dividend elements.**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nRndMode**– various rounding modes.**nScaleFactor**–[Integer Result Scaling](https://docs.nvidia.com/introduction.html#general_conventions_lb_1integer_result_scaling).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsDiv_Round_16s_Sfs_Ctx(const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrc1, const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrc2,[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pDst, size_t nLength,[NppRoundMode](https://docs.nvidia.com/nppdefs.html#c.NppRoundMode)nRndMode, int nScaleFactor,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsDiv_Round_16s_Sfs_Ctx)

-
16-bit signed short signal divide signal, scale, round, then clamp to saturated value.

- Parameters
-
**pSrc1**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pSrc2**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer), signal1 divisor elements to be divided into signal2 dividend elements.**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nRndMode**– various rounding modes.**nScaleFactor**–[Integer Result Scaling](https://docs.nvidia.com/introduction.html#general_conventions_lb_1integer_result_scaling).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsDiv_Round_8u_ISfs_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrcDst, size_t nLength,[NppRoundMode](https://docs.nvidia.com/nppdefs.html#c.NppRoundMode)nRndMode, int nScaleFactor,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsDiv_Round_8u_ISfs_Ctx)

-
8-bit unsigned char in place signal divide signal, with scaling, rounding then clamp to saturated value.

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pSrcDst**–[In-Place Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1in_place_signal_pointer). signal1 divisor elements to be divided into signal2 dividend elements**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nRndMode**– various rounding modes.**nScaleFactor**–[Integer Result Scaling](https://docs.nvidia.com/introduction.html#general_conventions_lb_1integer_result_scaling).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsDiv_Round_16u_ISfs_Ctx(const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrc,[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrcDst, size_t nLength,[NppRoundMode](https://docs.nvidia.com/nppdefs.html#c.NppRoundMode)nRndMode, int nScaleFactor,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsDiv_Round_16u_ISfs_Ctx)

-
16-bit unsigned short in place signal divide signal, with scaling, rounding then clamp to saturated value.

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pSrcDst**–[In-Place Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1in_place_signal_pointer). signal1 divisor elements to be divided into signal2 dividend elements**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nRndMode**– various rounding modes.**nScaleFactor**–[Integer Result Scaling](https://docs.nvidia.com/introduction.html#general_conventions_lb_1integer_result_scaling).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsDiv_Round_16s_ISfs_Ctx(const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrc,[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrcDst, size_t nLength,[NppRoundMode](https://docs.nvidia.com/nppdefs.html#c.NppRoundMode)nRndMode, int nScaleFactor,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsDiv_Round_16s_ISfs_Ctx)

-
16-bit signed short in place signal divide signal, with scaling, rounding then clamp to saturated value.

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pSrcDst**–[In-Place Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1in_place_signal_pointer). signal1 divisor elements to be divided into signal2 dividend elements**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nRndMode**– various rounding modes.**nScaleFactor**–[Integer Result Scaling](https://docs.nvidia.com/introduction.html#general_conventions_lb_1integer_result_scaling).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


### Signal Abs[](https://docs.nvidia.com#signal-abs)

#### Abs[](https://docs.nvidia.com#group__signal__abs_1signal_abs)

Absolute value of each sample of a signal.

Functions

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsAbs_16s_Ctx(const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrc,[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pDst, size_t nLength,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsAbs_16s_Ctx)

-
16-bit signed short signal absolute value.

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsAbs_32s_Ctx(const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pSrc,[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pDst, size_t nLength,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsAbs_32s_Ctx)

-
32-bit signed integer signal absolute value.

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsAbs_32f_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pDst, size_t nLength,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsAbs_32f_Ctx)

-
32-bit floating point signal absolute value.

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsAbs_64f_Ctx(const[Npp64f](https://docs.nvidia.com/nppdefs.html#c.Npp64f)*pSrc,[Npp64f](https://docs.nvidia.com/nppdefs.html#c.Npp64f)*pDst, size_t nLength,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsAbs_64f_Ctx)

-
64-bit floating point signal absolute value.

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsAbs_16s_I_Ctx([Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrcDst, size_t nLength,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsAbs_16s_I_Ctx)

-
16-bit signed short signal absolute value.

- Parameters
-
**pSrcDst**–[In-Place Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1in_place_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsAbs_32s_I_Ctx([Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pSrcDst, size_t nLength,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsAbs_32s_I_Ctx)

-
32-bit signed integer signal absolute value.

- Parameters
-
**pSrcDst**–[In-Place Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1in_place_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsAbs_32f_I_Ctx([Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrcDst, size_t nLength,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsAbs_32f_I_Ctx)

-
32-bit floating point signal absolute value.

- Parameters
-
**pSrcDst**–[In-Place Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1in_place_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsAbs_64f_I_Ctx([Npp64f](https://docs.nvidia.com/nppdefs.html#c.Npp64f)*pSrcDst, size_t nLength,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsAbs_64f_I_Ctx)

-
64-bit floating point signal absolute value.

- Parameters
-
**pSrcDst**–[In-Place Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1in_place_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


### Signal Square[](https://docs.nvidia.com#signal-square)

#### Sqr[](https://docs.nvidia.com#group__signal__square_1signal_square)

Squares each sample of a signal.

Functions

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsSqr_32f_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pDst, size_t nLength,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsSqr_32f_Ctx)

-
32-bit floating point signal squared.

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsSqr_64f_Ctx(const[Npp64f](https://docs.nvidia.com/nppdefs.html#c.Npp64f)*pSrc,[Npp64f](https://docs.nvidia.com/nppdefs.html#c.Npp64f)*pDst, size_t nLength,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsSqr_64f_Ctx)

-
64-bit floating point signal squared.

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsSqr_32fc_Ctx(const[Npp32fc](https://docs.nvidia.com/nppdefs.html#c.Npp32fc)*pSrc,[Npp32fc](https://docs.nvidia.com/nppdefs.html#c.Npp32fc)*pDst, size_t nLength,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsSqr_32fc_Ctx)

-
32-bit complex floating point signal squared.

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsSqr_64fc_Ctx(const[Npp64fc](https://docs.nvidia.com/nppdefs.html#c.Npp64fc)*pSrc,[Npp64fc](https://docs.nvidia.com/nppdefs.html#c.Npp64fc)*pDst, size_t nLength,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsSqr_64fc_Ctx)

-
64-bit complex floating point signal squared.

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsSqr_32f_I_Ctx([Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrcDst, size_t nLength,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsSqr_32f_I_Ctx)

-
32-bit floating point signal squared.

- Parameters
-
**pSrcDst**–[In-Place Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1in_place_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsSqr_64f_I_Ctx([Npp64f](https://docs.nvidia.com/nppdefs.html#c.Npp64f)*pSrcDst, size_t nLength,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsSqr_64f_I_Ctx)

-
64-bit floating point signal squared.

- Parameters
-
**pSrcDst**–[In-Place Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1in_place_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsSqr_32fc_I_Ctx([Npp32fc](https://docs.nvidia.com/nppdefs.html#c.Npp32fc)*pSrcDst, size_t nLength,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsSqr_32fc_I_Ctx)

-
32-bit complex floating point signal squared.

- Parameters
-
**pSrcDst**–[In-Place Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1in_place_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsSqr_64fc_I_Ctx([Npp64fc](https://docs.nvidia.com/nppdefs.html#c.Npp64fc)*pSrcDst, size_t nLength,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsSqr_64fc_I_Ctx)

-
64-bit complex floating point signal squared.

- Parameters
-
**pSrcDst**–[In-Place Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1in_place_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsSqr_8u_Sfs_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, size_t nLength, int nScaleFactor,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsSqr_8u_Sfs_Ctx)

-
8-bit unsigned char signal squared, scale, then clamp to saturated value.

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nScaleFactor**–[Integer Result Scaling](https://docs.nvidia.com/introduction.html#general_conventions_lb_1integer_result_scaling).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsSqr_16u_Sfs_Ctx(const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrc,[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pDst, size_t nLength, int nScaleFactor,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsSqr_16u_Sfs_Ctx)

-
16-bit unsigned short signal squared, scale, then clamp to saturated value.

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nScaleFactor**–[Integer Result Scaling](https://docs.nvidia.com/introduction.html#general_conventions_lb_1integer_result_scaling).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsSqr_16s_Sfs_Ctx(const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrc,[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pDst, size_t nLength, int nScaleFactor,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsSqr_16s_Sfs_Ctx)

-
16-bit signed short signal squared, scale, then clamp to saturated value.

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nScaleFactor**–[Integer Result Scaling](https://docs.nvidia.com/introduction.html#general_conventions_lb_1integer_result_scaling).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsSqr_16sc_Sfs_Ctx(const[Npp16sc](https://docs.nvidia.com/nppdefs.html#c.Npp16sc)*pSrc,[Npp16sc](https://docs.nvidia.com/nppdefs.html#c.Npp16sc)*pDst, size_t nLength, int nScaleFactor,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsSqr_16sc_Sfs_Ctx)

-
16-bit complex signed short signal squared, scale, then clamp to saturated value.

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nScaleFactor**–[Integer Result Scaling](https://docs.nvidia.com/introduction.html#general_conventions_lb_1integer_result_scaling).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsSqr_8u_ISfs_Ctx([Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrcDst, size_t nLength, int nScaleFactor,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsSqr_8u_ISfs_Ctx)

-
8-bit unsigned char signal squared, scale, then clamp to saturated value.

- Parameters
-
**pSrcDst**–[In-Place Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1in_place_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nScaleFactor**–[Integer Result Scaling](https://docs.nvidia.com/introduction.html#general_conventions_lb_1integer_result_scaling).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsSqr_16u_ISfs_Ctx([Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrcDst, size_t nLength, int nScaleFactor,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsSqr_16u_ISfs_Ctx)

-
16-bit unsigned short signal squared, scale, then clamp to saturated value.

- Parameters
-
**pSrcDst**–[In-Place Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1in_place_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nScaleFactor**–[Integer Result Scaling](https://docs.nvidia.com/introduction.html#general_conventions_lb_1integer_result_scaling).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsSqr_16s_ISfs_Ctx([Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrcDst, size_t nLength, int nScaleFactor,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsSqr_16s_ISfs_Ctx)

-
16-bit signed short signal squared, scale, then clamp to saturated value.

- Parameters
-
**pSrcDst**–[In-Place Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1in_place_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nScaleFactor**–[Integer Result Scaling](https://docs.nvidia.com/introduction.html#general_conventions_lb_1integer_result_scaling).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsSqr_16sc_ISfs_Ctx([Npp16sc](https://docs.nvidia.com/nppdefs.html#c.Npp16sc)*pSrcDst, size_t nLength, int nScaleFactor,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsSqr_16sc_ISfs_Ctx)

-
16-bit complex signed short signal squared, scale, then clamp to saturated value.

- Parameters
-
**pSrcDst**–[In-Place Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1in_place_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nScaleFactor**–[Integer Result Scaling](https://docs.nvidia.com/introduction.html#general_conventions_lb_1integer_result_scaling).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


### Signal Square Root[](https://docs.nvidia.com#signal-square-root)

#### Sqrt[](https://docs.nvidia.com#group__signal__sqrt_1signal_sqrt)

Square root of each sample of a signal.

Functions

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsSqrt_32f_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pDst, size_t nLength,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsSqrt_32f_Ctx)

-
32-bit floating point signal square root.

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsSqrt_64f_Ctx(const[Npp64f](https://docs.nvidia.com/nppdefs.html#c.Npp64f)*pSrc,[Npp64f](https://docs.nvidia.com/nppdefs.html#c.Npp64f)*pDst, size_t nLength,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsSqrt_64f_Ctx)

-
64-bit floating point signal square root.

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsSqrt_32fc_Ctx(const[Npp32fc](https://docs.nvidia.com/nppdefs.html#c.Npp32fc)*pSrc,[Npp32fc](https://docs.nvidia.com/nppdefs.html#c.Npp32fc)*pDst, size_t nLength,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsSqrt_32fc_Ctx)

-
32-bit complex floating point signal square root.

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsSqrt_64fc_Ctx(const[Npp64fc](https://docs.nvidia.com/nppdefs.html#c.Npp64fc)*pSrc,[Npp64fc](https://docs.nvidia.com/nppdefs.html#c.Npp64fc)*pDst, size_t nLength,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsSqrt_64fc_Ctx)

-
64-bit complex floating point signal square root.

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsSqrt_32f_I_Ctx([Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrcDst, size_t nLength,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsSqrt_32f_I_Ctx)

-
32-bit floating point signal square root.

- Parameters
-
**pSrcDst**–[In-Place Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1in_place_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsSqrt_64f_I_Ctx([Npp64f](https://docs.nvidia.com/nppdefs.html#c.Npp64f)*pSrcDst, size_t nLength,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsSqrt_64f_I_Ctx)

-
64-bit floating point signal square root.

- Parameters
-
**pSrcDst**–[In-Place Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1in_place_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsSqrt_32fc_I_Ctx([Npp32fc](https://docs.nvidia.com/nppdefs.html#c.Npp32fc)*pSrcDst, size_t nLength,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsSqrt_32fc_I_Ctx)

-
32-bit complex floating point signal square root.

- Parameters
-
**pSrcDst**–[In-Place Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1in_place_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsSqrt_64fc_I_Ctx([Npp64fc](https://docs.nvidia.com/nppdefs.html#c.Npp64fc)*pSrcDst, size_t nLength,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsSqrt_64fc_I_Ctx)

-
64-bit complex floating point signal square root.

- Parameters
-
**pSrcDst**–[In-Place Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1in_place_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsSqrt_8u_Sfs_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, size_t nLength, int nScaleFactor,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsSqrt_8u_Sfs_Ctx)

-
8-bit unsigned char signal square root, scale, then clamp to saturated value.

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nScaleFactor**–[Integer Result Scaling](https://docs.nvidia.com/introduction.html#general_conventions_lb_1integer_result_scaling).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsSqrt_16u_Sfs_Ctx(const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrc,[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pDst, size_t nLength, int nScaleFactor,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsSqrt_16u_Sfs_Ctx)

-
16-bit unsigned short signal square root, scale, then clamp to saturated value.

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nScaleFactor**–[Integer Result Scaling](https://docs.nvidia.com/introduction.html#general_conventions_lb_1integer_result_scaling).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsSqrt_16s_Sfs_Ctx(const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrc,[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pDst, size_t nLength, int nScaleFactor,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsSqrt_16s_Sfs_Ctx)

-
16-bit signed short signal square root, scale, then clamp to saturated value.

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nScaleFactor**–[Integer Result Scaling](https://docs.nvidia.com/introduction.html#general_conventions_lb_1integer_result_scaling).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsSqrt_16sc_Sfs_Ctx(const[Npp16sc](https://docs.nvidia.com/nppdefs.html#c.Npp16sc)*pSrc,[Npp16sc](https://docs.nvidia.com/nppdefs.html#c.Npp16sc)*pDst, size_t nLength, int nScaleFactor,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsSqrt_16sc_Sfs_Ctx)

-
16-bit complex signed short signal square root, scale, then clamp to saturated value.

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nScaleFactor**–[Integer Result Scaling](https://docs.nvidia.com/introduction.html#general_conventions_lb_1integer_result_scaling).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsSqrt_64s_Sfs_Ctx(const[Npp64s](https://docs.nvidia.com/nppdefs.html#c.Npp64s)*pSrc,[Npp64s](https://docs.nvidia.com/nppdefs.html#c.Npp64s)*pDst, size_t nLength, int nScaleFactor,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsSqrt_64s_Sfs_Ctx)

-
64-bit signed integer signal square root, scale, then clamp to saturated value.

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nScaleFactor**–[Integer Result Scaling](https://docs.nvidia.com/introduction.html#general_conventions_lb_1integer_result_scaling).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsSqrt_32s16s_Sfs_Ctx(const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pSrc,[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pDst, size_t nLength, int nScaleFactor,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsSqrt_32s16s_Sfs_Ctx)

-
32-bit signed integer signal square root, scale, then clamp to 16-bit signed integer saturated value.

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nScaleFactor**–[Integer Result Scaling](https://docs.nvidia.com/introduction.html#general_conventions_lb_1integer_result_scaling).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsSqrt_64s16s_Sfs_Ctx(const[Npp64s](https://docs.nvidia.com/nppdefs.html#c.Npp64s)*pSrc,[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pDst, size_t nLength, int nScaleFactor,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsSqrt_64s16s_Sfs_Ctx)

-
64-bit signed integer signal square root, scale, then clamp to 16-bit signed integer saturated value.

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nScaleFactor**–[Integer Result Scaling](https://docs.nvidia.com/introduction.html#general_conventions_lb_1integer_result_scaling).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsSqrt_8u_ISfs_Ctx([Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrcDst, size_t nLength, int nScaleFactor,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsSqrt_8u_ISfs_Ctx)

-
8-bit unsigned char signal square root, scale, then clamp to saturated value.

- Parameters
-
**pSrcDst**–[In-Place Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1in_place_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nScaleFactor**–[Integer Result Scaling](https://docs.nvidia.com/introduction.html#general_conventions_lb_1integer_result_scaling).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsSqrt_16u_ISfs_Ctx([Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrcDst, size_t nLength, int nScaleFactor,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsSqrt_16u_ISfs_Ctx)

-
16-bit unsigned short signal square root, scale, then clamp to saturated value.

- Parameters
-
**pSrcDst**–[In-Place Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1in_place_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nScaleFactor**–[Integer Result Scaling](https://docs.nvidia.com/introduction.html#general_conventions_lb_1integer_result_scaling).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsSqrt_16s_ISfs_Ctx([Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrcDst, size_t nLength, int nScaleFactor,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsSqrt_16s_ISfs_Ctx)

-
16-bit signed short signal square root, scale, then clamp to saturated value.

- Parameters
-
**pSrcDst**–[In-Place Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1in_place_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nScaleFactor**–[Integer Result Scaling](https://docs.nvidia.com/introduction.html#general_conventions_lb_1integer_result_scaling).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsSqrt_16sc_ISfs_Ctx([Npp16sc](https://docs.nvidia.com/nppdefs.html#c.Npp16sc)*pSrcDst, size_t nLength, int nScaleFactor,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsSqrt_16sc_ISfs_Ctx)

-
16-bit complex signed short signal square root, scale, then clamp to saturated value.

- Parameters
-
**pSrcDst**–[In-Place Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1in_place_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nScaleFactor**–[Integer Result Scaling](https://docs.nvidia.com/introduction.html#general_conventions_lb_1integer_result_scaling).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsSqrt_64s_ISfs_Ctx([Npp64s](https://docs.nvidia.com/nppdefs.html#c.Npp64s)*pSrcDst, size_t nLength, int nScaleFactor,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsSqrt_64s_ISfs_Ctx)

-
64-bit signed integer signal square root, scale, then clamp to saturated value.

- Parameters
-
**pSrcDst**–[In-Place Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1in_place_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nScaleFactor**–[Integer Result Scaling](https://docs.nvidia.com/introduction.html#general_conventions_lb_1integer_result_scaling).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


### Signal Cube Root[](https://docs.nvidia.com#signal-cube-root)

#### Cubrt[](https://docs.nvidia.com#group__signal__cuberoot_1signal_cuberoot)

Cube root of each sample of a signal.

Functions

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsCubrt_32f_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pDst, size_t nLength,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsCubrt_32f_Ctx)

-
32-bit floating point signal cube root.

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsCubrt_32s16s_Sfs_Ctx(const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pSrc,[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pDst, size_t nLength, int nScaleFactor,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsCubrt_32s16s_Sfs_Ctx)

-
32-bit signed integer signal cube root, scale, then clamp to 16-bit signed integer saturated value.

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nScaleFactor**–[Integer Result Scaling](https://docs.nvidia.com/introduction.html#general_conventions_lb_1integer_result_scaling).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


### Signal Exp[](https://docs.nvidia.com#signal-exp)

#### Exp[](https://docs.nvidia.com#group__signal__exp_1signal_exp)

E raised to the power of each sample of a signal.

Functions

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsExp_32f_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pDst, size_t nLength,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsExp_32f_Ctx)

-
32-bit floating point signal exponent.

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsExp_64f_Ctx(const[Npp64f](https://docs.nvidia.com/nppdefs.html#c.Npp64f)*pSrc,[Npp64f](https://docs.nvidia.com/nppdefs.html#c.Npp64f)*pDst, size_t nLength,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsExp_64f_Ctx)

-
64-bit floating point signal exponent.

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsExp_32f64f_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc,[Npp64f](https://docs.nvidia.com/nppdefs.html#c.Npp64f)*pDst, size_t nLength,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsExp_32f64f_Ctx)

-
32-bit floating point signal exponent with 64-bit floating point result.

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsExp_32f_I_Ctx([Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrcDst, size_t nLength,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsExp_32f_I_Ctx)

-
32-bit floating point signal exponent.

- Parameters
-
**pSrcDst**–[In-Place Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1in_place_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsExp_64f_I_Ctx([Npp64f](https://docs.nvidia.com/nppdefs.html#c.Npp64f)*pSrcDst, size_t nLength,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsExp_64f_I_Ctx)

-
64-bit floating point signal exponent.

- Parameters
-
**pSrcDst**–[In-Place Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1in_place_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsExp_16s_Sfs_Ctx(const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrc,[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pDst, size_t nLength, int nScaleFactor,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsExp_16s_Sfs_Ctx)

-
16-bit signed short signal exponent, scale, then clamp to saturated value.

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nScaleFactor**–[Integer Result Scaling](https://docs.nvidia.com/introduction.html#general_conventions_lb_1integer_result_scaling).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsExp_32s_Sfs_Ctx(const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pSrc,[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pDst, size_t nLength, int nScaleFactor,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsExp_32s_Sfs_Ctx)

-
32-bit signed integer signal exponent, scale, then clamp to saturated value.

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nScaleFactor**–[Integer Result Scaling](https://docs.nvidia.com/introduction.html#general_conventions_lb_1integer_result_scaling).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsExp_64s_Sfs_Ctx(const[Npp64s](https://docs.nvidia.com/nppdefs.html#c.Npp64s)*pSrc,[Npp64s](https://docs.nvidia.com/nppdefs.html#c.Npp64s)*pDst, size_t nLength, int nScaleFactor,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsExp_64s_Sfs_Ctx)

-
64-bit signed integer signal exponent, scale, then clamp to saturated value.

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nScaleFactor**–[Integer Result Scaling](https://docs.nvidia.com/introduction.html#general_conventions_lb_1integer_result_scaling).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsExp_16s_ISfs_Ctx([Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrcDst, size_t nLength, int nScaleFactor,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsExp_16s_ISfs_Ctx)

-
16-bit signed short signal exponent, scale, then clamp to saturated value.

- Parameters
-
**pSrcDst**–[In-Place Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1in_place_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nScaleFactor**–[Integer Result Scaling](https://docs.nvidia.com/introduction.html#general_conventions_lb_1integer_result_scaling).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsExp_32s_ISfs_Ctx([Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pSrcDst, size_t nLength, int nScaleFactor,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsExp_32s_ISfs_Ctx)

-
32-bit signed integer signal exponent, scale, then clamp to saturated value.

- Parameters
-
**pSrcDst**–[In-Place Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1in_place_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nScaleFactor**–[Integer Result Scaling](https://docs.nvidia.com/introduction.html#general_conventions_lb_1integer_result_scaling).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsExp_64s_ISfs_Ctx([Npp64s](https://docs.nvidia.com/nppdefs.html#c.Npp64s)*pSrcDst, size_t nLength, int nScaleFactor,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsExp_64s_ISfs_Ctx)

-
64-bit signed integer signal exponent, scale, then clamp to saturated value.

- Parameters
-
**pSrcDst**–[In-Place Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1in_place_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nScaleFactor**–[Integer Result Scaling](https://docs.nvidia.com/introduction.html#general_conventions_lb_1integer_result_scaling).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


### Signal Ln[](https://docs.nvidia.com#signal-ln)

#### Ln[](https://docs.nvidia.com#group__signal__ln_1signal_ln)

Natural logarithm of each sample of a signal.

Functions

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsLn_32f_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pDst, size_t nLength,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsLn_32f_Ctx)

-
32-bit floating point signal natural logarithm.

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsLn_64f_Ctx(const[Npp64f](https://docs.nvidia.com/nppdefs.html#c.Npp64f)*pSrc,[Npp64f](https://docs.nvidia.com/nppdefs.html#c.Npp64f)*pDst, size_t nLength,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsLn_64f_Ctx)

-
64-bit floating point signal natural logarithm.

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsLn_64f32f_Ctx(const[Npp64f](https://docs.nvidia.com/nppdefs.html#c.Npp64f)*pSrc,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pDst, size_t nLength,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsLn_64f32f_Ctx)

-
64-bit floating point signal natural logarithm with 32-bit floating point result.

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsLn_32f_I_Ctx([Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrcDst, size_t nLength,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsLn_32f_I_Ctx)

-
32-bit floating point signal natural logarithm.

- Parameters
-
**pSrcDst**–[In-Place Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1in_place_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsLn_64f_I_Ctx([Npp64f](https://docs.nvidia.com/nppdefs.html#c.Npp64f)*pSrcDst, size_t nLength,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsLn_64f_I_Ctx)

-
64-bit floating point signal natural logarithm.

- Parameters
-
**pSrcDst**–[In-Place Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1in_place_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsLn_16s_Sfs_Ctx(const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrc,[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pDst, size_t nLength, int nScaleFactor,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsLn_16s_Sfs_Ctx)

-
16-bit signed short signal natural logarithm, scale, then clamp to saturated value.

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nScaleFactor**–[Integer Result Scaling](https://docs.nvidia.com/introduction.html#general_conventions_lb_1integer_result_scaling).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsLn_32s_Sfs_Ctx(const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pSrc,[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pDst, size_t nLength, int nScaleFactor,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsLn_32s_Sfs_Ctx)

-
32-bit signed integer signal natural logarithm, scale, then clamp to saturated value.

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nScaleFactor**–[Integer Result Scaling](https://docs.nvidia.com/introduction.html#general_conventions_lb_1integer_result_scaling).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsLn_32s16s_Sfs_Ctx(const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pSrc,[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pDst, size_t nLength, int nScaleFactor,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsLn_32s16s_Sfs_Ctx)

-
32-bit signed integer signal natural logarithm, scale, then clamp to 16-bit signed short saturated value.

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nScaleFactor**–[Integer Result Scaling](https://docs.nvidia.com/introduction.html#general_conventions_lb_1integer_result_scaling).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsLn_16s_ISfs_Ctx([Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrcDst, size_t nLength, int nScaleFactor,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsLn_16s_ISfs_Ctx)

-
16-bit signed short signal natural logarithm, scale, then clamp to saturated value.

- Parameters
-
**pSrcDst**–[In-Place Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1in_place_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nScaleFactor**–[Integer Result Scaling](https://docs.nvidia.com/introduction.html#general_conventions_lb_1integer_result_scaling).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsLn_32s_ISfs_Ctx([Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pSrcDst, size_t nLength, int nScaleFactor,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsLn_32s_ISfs_Ctx)

-
32-bit signed integer signal natural logarithm, scale, then clamp to saturated value.

- Parameters
-
**pSrcDst**–[In-Place Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1in_place_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nScaleFactor**–[Integer Result Scaling](https://docs.nvidia.com/introduction.html#general_conventions_lb_1integer_result_scaling).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


### Signal 10Log10[](https://docs.nvidia.com#signal-10log10)

#### 10Log10[](https://docs.nvidia.com#group__signal__10log10_1signal_10log10)

Ten times the decimal logarithm of each sample of a signal.

Functions

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)npps10Log10_32s_Sfs_Ctx(const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pSrc,[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pDst, size_t nLength, int nScaleFactor,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.npps10Log10_32s_Sfs_Ctx)

-
32-bit signed integer signal 10 times base 10 logarithm, scale, then clamp to saturated value.

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nScaleFactor**–[Integer Result Scaling](https://docs.nvidia.com/introduction.html#general_conventions_lb_1integer_result_scaling).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)npps10Log10_32s_ISfs_Ctx([Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pSrcDst, size_t nLength, int nScaleFactor,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.npps10Log10_32s_ISfs_Ctx)

-
32-bit signed integer signal 10 times base 10 logarithm, scale, then clamp to saturated value.

- Parameters
-
**pSrcDst**–[In-Place Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1in_place_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nScaleFactor**–[Integer Result Scaling](https://docs.nvidia.com/introduction.html#general_conventions_lb_1integer_result_scaling).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


### Signal SumLn[](https://docs.nvidia.com#signal-sumln)

#### SumLn[](https://docs.nvidia.com#group__signal__sumln_1signal_sumln)

Sums up the natural logarithm of each sample of a signal.

Functions

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsSumLnGetBufferSize_32f_Ctx(size_t nLength, size_t *hpBufferSize,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsSumLnGetBufferSize_32f_Ctx)

-
Device scratch buffer size (in bytes) for 32f SumLn.

This primitive provides the correct buffer size for nppsSumLn_32f.

- Parameters
-
**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**hpBufferSize**– Required buffer size. Important: hpBufferSize is a*host pointer.*[Scratch Buffer and Host Pointer](https://docs.nvidia.com/introduction.html#general_conventions_lb_1general_scratch_buffer).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
NPP_SUCCESS



-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsSumLn_32f_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc, size_t nLength,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pDst,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDeviceBuffer,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsSumLn_32f_Ctx)

-
32-bit floating point signal sum natural logarithm.

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**pDst**– Pointer to the output result.**pDeviceBuffer**– Pointer to the required device memory allocation.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsSumLnGetBufferSize_64f_Ctx(size_t nLength, size_t *hpBufferSize,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsSumLnGetBufferSize_64f_Ctx)

-
Device scratch buffer size (in bytes) for 64f SumLn.

This primitive provides the correct buffer size for nppsSumLn_64f.

- Parameters
-
**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**hpBufferSize**– Required buffer size. Important: hpBufferSize is a*host pointer.*[Scratch Buffer and Host Pointer](https://docs.nvidia.com/introduction.html#general_conventions_lb_1general_scratch_buffer).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
NPP_SUCCESS



-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsSumLn_64f_Ctx(const[Npp64f](https://docs.nvidia.com/nppdefs.html#c.Npp64f)*pSrc, size_t nLength,[Npp64f](https://docs.nvidia.com/nppdefs.html#c.Npp64f)*pDst,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDeviceBuffer,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsSumLn_64f_Ctx)

-
64-bit floating point signal sum natural logarithm.

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**pDst**– Pointer to the output result.**pDeviceBuffer**– Pointer to the required device memory allocation.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsSumLnGetBufferSize_32f64f_Ctx(size_t nLength, size_t *hpBufferSize,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsSumLnGetBufferSize_32f64f_Ctx)

-
Device scratch buffer size (in bytes) for 32f64f SumLn.

This primitive provides the correct buffer size for nppsSumLn_32f64f.

- Parameters
-
**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**hpBufferSize**– Required buffer size. Important: hpBufferSize is a*host pointer.*[Scratch Buffer and Host Pointer](https://docs.nvidia.com/introduction.html#general_conventions_lb_1general_scratch_buffer).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
NPP_SUCCESS



-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsSumLn_32f64f_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc, size_t nLength,[Npp64f](https://docs.nvidia.com/nppdefs.html#c.Npp64f)*pDst,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDeviceBuffer,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsSumLn_32f64f_Ctx)

-
32-bit flaoting point input, 64-bit floating point output signal sum natural logarithm.

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**pDst**– Pointer to the output result.**pDeviceBuffer**– Pointer to the required device memory allocation.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsSumLnGetBufferSize_16s32f_Ctx(size_t nLength, size_t *hpBufferSize,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsSumLnGetBufferSize_16s32f_Ctx)

-
Device scratch buffer size (in bytes) for 16s32f SumLn.

This primitive provides the correct buffer size for nppsSumLn_16s32f.

- Parameters
-
**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**hpBufferSize**– Required buffer size. Important: hpBufferSize is a*host pointer.*[Scratch Buffer and Host Pointer](https://docs.nvidia.com/introduction.html#general_conventions_lb_1general_scratch_buffer).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
NPP_SUCCESS



-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsSumLn_16s32f_Ctx(const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrc, size_t nLength,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pDst,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDeviceBuffer,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsSumLn_16s32f_Ctx)

-
16-bit signed short integer input, 32-bit floating point output signal sum natural logarithm.

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**pDst**– Pointer to the output result.**pDeviceBuffer**– Pointer to the required device memory allocation.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


### Signal ArcTan[](https://docs.nvidia.com#signal-arctan)

#### Arctan[](https://docs.nvidia.com#group__signal__inversetan_1signal_inversetan)

Inverse tangent of each sample of a signal.

Functions

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsArctan_32f_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pDst, size_t nLength,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsArctan_32f_Ctx)

-
32-bit floating point signal inverse tangent.

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsArctan_64f_Ctx(const[Npp64f](https://docs.nvidia.com/nppdefs.html#c.Npp64f)*pSrc,[Npp64f](https://docs.nvidia.com/nppdefs.html#c.Npp64f)*pDst, size_t nLength,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsArctan_64f_Ctx)

-
64-bit floating point signal inverse tangent.

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsArctan_32f_I_Ctx([Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrcDst, size_t nLength,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsArctan_32f_I_Ctx)

-
32-bit floating point signal inverse tangent.

- Parameters
-
**pSrcDst**–[In-Place Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1in_place_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsArctan_64f_I_Ctx([Npp64f](https://docs.nvidia.com/nppdefs.html#c.Npp64f)*pSrcDst, size_t nLength,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsArctan_64f_I_Ctx)

-
64-bit floating point signal inverse tangent.

- Parameters
-
**pSrcDst**–[In-Place Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1in_place_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


### Signal Normalize[](https://docs.nvidia.com#signal-normalize)

#### Normalize[](https://docs.nvidia.com#group__signal__normalize_1signal_normalize)

Normalize each sample of a real or complex signal using offset and division operations.

Functions

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsNormalize_32f_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pDst, size_t nLength,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)vSub,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)vDiv,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsNormalize_32f_Ctx)

-
32-bit floating point signal normalize.

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**vSub**– value subtracted from each signal element before division**vDiv**– divisor of post-subtracted signal element dividend**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsNormalize_32fc_Ctx(const[Npp32fc](https://docs.nvidia.com/nppdefs.html#c.Npp32fc)*pSrc,[Npp32fc](https://docs.nvidia.com/nppdefs.html#c.Npp32fc)*pDst, size_t nLength,[Npp32fc](https://docs.nvidia.com/nppdefs.html#c.Npp32fc)vSub,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)vDiv,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsNormalize_32fc_Ctx)

-
32-bit complex floating point signal normalize.

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**vSub**– value subtracted from each signal element before division**vDiv**– divisor of post-subtracted signal element dividend**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsNormalize_64f_Ctx(const[Npp64f](https://docs.nvidia.com/nppdefs.html#c.Npp64f)*pSrc,[Npp64f](https://docs.nvidia.com/nppdefs.html#c.Npp64f)*pDst, size_t nLength,[Npp64f](https://docs.nvidia.com/nppdefs.html#c.Npp64f)vSub,[Npp64f](https://docs.nvidia.com/nppdefs.html#c.Npp64f)vDiv,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsNormalize_64f_Ctx)

-
64-bit floating point signal normalize.

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**vSub**– value subtracted from each signal element before division**vDiv**– divisor of post-subtracted signal element dividend**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsNormalize_64fc_Ctx(const[Npp64fc](https://docs.nvidia.com/nppdefs.html#c.Npp64fc)*pSrc,[Npp64fc](https://docs.nvidia.com/nppdefs.html#c.Npp64fc)*pDst, size_t nLength,[Npp64fc](https://docs.nvidia.com/nppdefs.html#c.Npp64fc)vSub,[Npp64f](https://docs.nvidia.com/nppdefs.html#c.Npp64f)vDiv,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsNormalize_64fc_Ctx)

-
64-bit complex floating point signal normalize.

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**vSub**– value subtracted from each signal element before division**vDiv**– divisor of post-subtracted signal element dividend**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsNormalize_16s_Sfs_Ctx(const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrc,[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pDst, size_t nLength,[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)vSub, int vDiv, int nScaleFactor,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsNormalize_16s_Sfs_Ctx)

-
16-bit signed short signal normalize, scale, then clamp to saturated value.

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**vSub**– value subtracted from each signal element before division**vDiv**– divisor of post-subtracted signal element dividend**nScaleFactor**–[Integer Result Scaling](https://docs.nvidia.com/introduction.html#general_conventions_lb_1integer_result_scaling).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsNormalize_16sc_Sfs_Ctx(const[Npp16sc](https://docs.nvidia.com/nppdefs.html#c.Npp16sc)*pSrc,[Npp16sc](https://docs.nvidia.com/nppdefs.html#c.Npp16sc)*pDst, size_t nLength,[Npp16sc](https://docs.nvidia.com/nppdefs.html#c.Npp16sc)vSub, int vDiv, int nScaleFactor,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsNormalize_16sc_Sfs_Ctx)

-
16-bit complex signed short signal normalize, scale, then clamp to saturated value.

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**vSub**– value subtracted from each signal element before division**vDiv**– divisor of post-subtracted signal element dividend**nScaleFactor**–[Integer Result Scaling](https://docs.nvidia.com/introduction.html#general_conventions_lb_1integer_result_scaling).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


### Signal Cauchy, CouchyD, And CouchyDD2[](https://docs.nvidia.com#signal-cauchy-couchyd-and-couchydd2)

#### Cauchy, CauchyD, and CauchyDD2[](https://docs.nvidia.com#group__signal__cauchy_1signal_cauchy)

Determine Cauchy robust error function and its first and second derivatives for each sample of a signal.

Functions

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsCauchy_32f_I_Ctx([Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrcDst, size_t nLength,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)nParam,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsCauchy_32f_I_Ctx)

-
32-bit floating point signal Cauchy error calculation.

- Parameters
-
**pSrcDst**–[In-Place Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1in_place_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nParam**– constant used in Cauchy formula**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsCauchyD_32f_I_Ctx([Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrcDst, size_t nLength,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)nParam,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsCauchyD_32f_I_Ctx)

-
32-bit floating point signal Cauchy first derivative.

- Parameters
-
**pSrcDst**–[In-Place Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1in_place_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nParam**– constant used in Cauchy formula**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsCauchyDD2_32f_I_Ctx([Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrcDst,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pD2FVal, size_t nLength,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)nParam,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsCauchyDD2_32f_I_Ctx)

-
32-bit floating point signal Cauchy first and second derivatives.

- Parameters
-
**pSrcDst**–[In-Place Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1in_place_signal_pointer).**pD2FVal**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer). This signal contains the second derivative of the source signal.**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nParam**– constant used in Cauchy formula**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


## Logical And Shift Operations[](https://docs.nvidia.com#logical-and-shift-operations)

### Logical And Shift Operations[](https://docs.nvidia.com#group__signal__logical__and__shift__operations_1signal_logical_and_shift_operations)

The set of logical and shift operations for signal processing available in the library.

### Signal AndC[](https://docs.nvidia.com#signal-andc)

#### AndC[](https://docs.nvidia.com#group__signal__andc_1signal_andc)

Bitwise AND of a constant and each sample of a signal.

Functions

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsAndC_8u_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)nValue,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, size_t nLength,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsAndC_8u_Ctx)

-
8-bit unsigned char signal and with constant.

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nValue**– Constant value to be anded with each vector element**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsAndC_16u_Ctx(const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrc,[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)nValue,[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pDst, size_t nLength,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsAndC_16u_Ctx)

-
16-bit unsigned short signal and with constant.

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nValue**– Constant value to be anded with each vector element**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsAndC_32u_Ctx(const[Npp32u](https://docs.nvidia.com/nppdefs.html#c.Npp32u)*pSrc,[Npp32u](https://docs.nvidia.com/nppdefs.html#c.Npp32u)nValue,[Npp32u](https://docs.nvidia.com/nppdefs.html#c.Npp32u)*pDst, size_t nLength,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsAndC_32u_Ctx)

-
32-bit unsigned integer signal and with constant.

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nValue**– Constant value to be anded with each vector element**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsAndC_8u_I_Ctx([Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)nValue,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrcDst, size_t nLength,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsAndC_8u_I_Ctx)

-
8-bit unsigned char in place signal and with constant.

- Parameters
-
**pSrcDst**–[In-Place Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1in_place_signal_pointer).**nValue**– Constant value to be anded with each vector element**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsAndC_16u_I_Ctx([Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)nValue,[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrcDst, size_t nLength,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsAndC_16u_I_Ctx)

-
16-bit unsigned short in place signal and with constant.

- Parameters
-
**pSrcDst**–[In-Place Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1in_place_signal_pointer).**nValue**– Constant value to be anded with each vector element**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsAndC_32u_I_Ctx([Npp32u](https://docs.nvidia.com/nppdefs.html#c.Npp32u)nValue,[Npp32u](https://docs.nvidia.com/nppdefs.html#c.Npp32u)*pSrcDst, size_t nLength,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsAndC_32u_I_Ctx)

-
32-bit unsigned signed integer in place signal and with constant.

- Parameters
-
**pSrcDst**–[In-Place Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1in_place_signal_pointer).**nValue**– Constant value to be anded with each vector element**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


### Signal And[](https://docs.nvidia.com#signal-and)

#### And[](https://docs.nvidia.com#group__signal__and_1signal_and)

Sample by sample bitwise AND of samples from two signals.

Functions

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsAnd_8u_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc1, const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc2,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, size_t nLength,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsAnd_8u_Ctx)

-
8-bit unsigned char signal and with signal.

- Parameters
-
**pSrc1**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pSrc2**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer). signal2 elements to be anded with signal1 elements**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsAnd_16u_Ctx(const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrc1, const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrc2,[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pDst, size_t nLength,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsAnd_16u_Ctx)

-
16-bit unsigned short signal and with signal.

- Parameters
-
**pSrc1**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pSrc2**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer). signal2 elements to be anded with signal1 elements**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsAnd_32u_Ctx(const[Npp32u](https://docs.nvidia.com/nppdefs.html#c.Npp32u)*pSrc1, const[Npp32u](https://docs.nvidia.com/nppdefs.html#c.Npp32u)*pSrc2,[Npp32u](https://docs.nvidia.com/nppdefs.html#c.Npp32u)*pDst, size_t nLength,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsAnd_32u_Ctx)

-
32-bit unsigned integer signal and with signal.

- Parameters
-
**pSrc1**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pSrc2**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer). signal2 elements to be anded with signal1 elements**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsAnd_8u_I_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrcDst, size_t nLength,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsAnd_8u_I_Ctx)

-
8-bit unsigned char in place signal and with signal.

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pSrcDst**–[In-Place Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1in_place_signal_pointer). signal2 elements to be anded with signal1 elements**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsAnd_16u_I_Ctx(const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrc,[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrcDst, size_t nLength,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsAnd_16u_I_Ctx)

-
16-bit unsigned short in place signal and with signal.

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pSrcDst**–[In-Place Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1in_place_signal_pointer). signal2 elements to be anded with signal1 elements**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsAnd_32u_I_Ctx(const[Npp32u](https://docs.nvidia.com/nppdefs.html#c.Npp32u)*pSrc,[Npp32u](https://docs.nvidia.com/nppdefs.html#c.Npp32u)*pSrcDst, size_t nLength,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsAnd_32u_I_Ctx)

-
32-bit unsigned integer in place signal and with signal.

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pSrcDst**–[In-Place Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1in_place_signal_pointer). signal2 elements to be anded with signal1 elements**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


### Signal OrC[](https://docs.nvidia.com#signal-orc)

#### OrC[](https://docs.nvidia.com#group__signal__orc_1signal_orc)

Bitwise OR of a constant and each sample of a signal.

Functions

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsOrC_8u_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)nValue,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, size_t nLength,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsOrC_8u_Ctx)

-
8-bit unsigned char signal or with constant.

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nValue**– Constant value to be ored with each vector element**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsOrC_16u_Ctx(const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrc,[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)nValue,[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pDst, size_t nLength,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsOrC_16u_Ctx)

-
16-bit unsigned short signal or with constant.

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nValue**– Constant value to be ored with each vector element**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsOrC_32u_Ctx(const[Npp32u](https://docs.nvidia.com/nppdefs.html#c.Npp32u)*pSrc,[Npp32u](https://docs.nvidia.com/nppdefs.html#c.Npp32u)nValue,[Npp32u](https://docs.nvidia.com/nppdefs.html#c.Npp32u)*pDst, size_t nLength,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsOrC_32u_Ctx)

-
32-bit unsigned integer signal or with constant.

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nValue**– Constant value to be ored with each vector element**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsOrC_8u_I_Ctx([Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)nValue,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrcDst, size_t nLength,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsOrC_8u_I_Ctx)

-
8-bit unsigned char in place signal or with constant.

- Parameters
-
**pSrcDst**–[In-Place Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1in_place_signal_pointer).**nValue**– Constant value to be ored with each vector element**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsOrC_16u_I_Ctx([Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)nValue,[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrcDst, size_t nLength,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsOrC_16u_I_Ctx)

-
16-bit unsigned short in place signal or with constant.

- Parameters
-
**pSrcDst**–[In-Place Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1in_place_signal_pointer).**nValue**– Constant value to be ored with each vector element**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsOrC_32u_I_Ctx([Npp32u](https://docs.nvidia.com/nppdefs.html#c.Npp32u)nValue,[Npp32u](https://docs.nvidia.com/nppdefs.html#c.Npp32u)*pSrcDst, size_t nLength,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsOrC_32u_I_Ctx)

-
32-bit unsigned signed integer in place signal or with constant.

- Parameters
-
**pSrcDst**–[In-Place Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1in_place_signal_pointer).**nValue**– Constant value to be ored with each vector element**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


### Signal Or[](https://docs.nvidia.com#signal-or)

#### Or[](https://docs.nvidia.com#group__signal__or_1signal_or)

Sample by sample bitwise OR of the samples from two signals.

Functions

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsOr_8u_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc1, const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc2,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, size_t nLength,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsOr_8u_Ctx)

-
8-bit unsigned char signal or with signal.

- Parameters
-
**pSrc1**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pSrc2**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer). signal2 elements to be ored with signal1 elements**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsOr_16u_Ctx(const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrc1, const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrc2,[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pDst, size_t nLength,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsOr_16u_Ctx)

-
16-bit unsigned short signal or with signal.

- Parameters
-
**pSrc1**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pSrc2**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer). signal2 elements to be ored with signal1 elements**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsOr_32u_Ctx(const[Npp32u](https://docs.nvidia.com/nppdefs.html#c.Npp32u)*pSrc1, const[Npp32u](https://docs.nvidia.com/nppdefs.html#c.Npp32u)*pSrc2,[Npp32u](https://docs.nvidia.com/nppdefs.html#c.Npp32u)*pDst, size_t nLength,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsOr_32u_Ctx)

-
32-bit unsigned integer signal or with signal.

- Parameters
-
**pSrc1**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pSrc2**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer). signal2 elements to be ored with signal1 elements**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsOr_8u_I_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrcDst, size_t nLength,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsOr_8u_I_Ctx)

-
8-bit unsigned char in place signal or with signal.

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pSrcDst**–[In-Place Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1in_place_signal_pointer). signal2 elements to be ored with signal1 elements**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsOr_16u_I_Ctx(const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrc,[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrcDst, size_t nLength,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsOr_16u_I_Ctx)

-
16-bit unsigned short in place signal or with signal.

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pSrcDst**–[In-Place Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1in_place_signal_pointer). signal2 elements to be ored with signal1 elements**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsOr_32u_I_Ctx(const[Npp32u](https://docs.nvidia.com/nppdefs.html#c.Npp32u)*pSrc,[Npp32u](https://docs.nvidia.com/nppdefs.html#c.Npp32u)*pSrcDst, size_t nLength,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsOr_32u_I_Ctx)

-
32-bit unsigned integer in place signal or with signal.

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pSrcDst**–[In-Place Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1in_place_signal_pointer). signal2 elements to be ored with signal1 elements**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


### Signal XorC[](https://docs.nvidia.com#signal-xorc)

#### XorC[](https://docs.nvidia.com#group__signal__xorc_1signal_xorc)

Bitwise XOR of a constant and each sample of a signal.

Functions

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsXorC_8u_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)nValue,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, size_t nLength,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsXorC_8u_Ctx)

-
8-bit unsigned char signal exclusive or with constant.

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nValue**– Constant value to be exclusive ored with each vector element**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsXorC_16u_Ctx(const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrc,[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)nValue,[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pDst, size_t nLength,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsXorC_16u_Ctx)

-
16-bit unsigned short signal exclusive or with constant.

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nValue**– Constant value to be exclusive ored with each vector element**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsXorC_32u_Ctx(const[Npp32u](https://docs.nvidia.com/nppdefs.html#c.Npp32u)*pSrc,[Npp32u](https://docs.nvidia.com/nppdefs.html#c.Npp32u)nValue,[Npp32u](https://docs.nvidia.com/nppdefs.html#c.Npp32u)*pDst, size_t nLength,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsXorC_32u_Ctx)

-
32-bit unsigned integer signal exclusive or with constant.

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nValue**– Constant value to be exclusive ored with each vector element**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsXorC_8u_I_Ctx([Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)nValue,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrcDst, size_t nLength,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsXorC_8u_I_Ctx)

-
8-bit unsigned char in place signal exclusive or with constant.

- Parameters
-
**pSrcDst**–[In-Place Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1in_place_signal_pointer).**nValue**– Constant value to be exclusive ored with each vector element**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsXorC_16u_I_Ctx([Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)nValue,[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrcDst, size_t nLength,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsXorC_16u_I_Ctx)

-
16-bit unsigned short in place signal exclusive or with constant.

- Parameters
-
**pSrcDst**–[In-Place Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1in_place_signal_pointer).**nValue**– Constant value to be exclusive ored with each vector element**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsXorC_32u_I_Ctx([Npp32u](https://docs.nvidia.com/nppdefs.html#c.Npp32u)nValue,[Npp32u](https://docs.nvidia.com/nppdefs.html#c.Npp32u)*pSrcDst, size_t nLength,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsXorC_32u_I_Ctx)

-
32-bit unsigned signed integer in place signal exclusive or with constant.

- Parameters
-
**pSrcDst**–[In-Place Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1in_place_signal_pointer).**nValue**– Constant value to be exclusive ored with each vector element**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


### Signal Xor[](https://docs.nvidia.com#signal-xor)

#### Xor[](https://docs.nvidia.com#group__signal__xor_1signal_xor)

Sample by sample bitwise XOR of the samples from two signals.

Functions

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsXor_8u_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc1, const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc2,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, size_t nLength,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsXor_8u_Ctx)

-
8-bit unsigned char signal exclusive or with signal.

- Parameters
-
**pSrc1**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pSrc2**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer). signal2 elements to be exclusive ored with signal1 elements**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsXor_16u_Ctx(const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrc1, const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrc2,[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pDst, size_t nLength,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsXor_16u_Ctx)

-
16-bit unsigned short signal exclusive or with signal.

- Parameters
-
**pSrc1**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pSrc2**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer). signal2 elements to be exclusive ored with signal1 elements**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsXor_32u_Ctx(const[Npp32u](https://docs.nvidia.com/nppdefs.html#c.Npp32u)*pSrc1, const[Npp32u](https://docs.nvidia.com/nppdefs.html#c.Npp32u)*pSrc2,[Npp32u](https://docs.nvidia.com/nppdefs.html#c.Npp32u)*pDst, size_t nLength,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsXor_32u_Ctx)

-
32-bit unsigned integer signal exclusive or with signal.

- Parameters
-
**pSrc1**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pSrc2**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer). signal2 elements to be exclusive ored with signal1 elements**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsXor_8u_I_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrcDst, size_t nLength,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsXor_8u_I_Ctx)

-
8-bit unsigned char in place signal exclusive or with signal.

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pSrcDst**–[In-Place Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1in_place_signal_pointer). signal2 elements to be exclusive ored with signal1 elements**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsXor_16u_I_Ctx(const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrc,[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrcDst, size_t nLength,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsXor_16u_I_Ctx)

-
16-bit unsigned short in place signal exclusive or with signal.

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pSrcDst**–[In-Place Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1in_place_signal_pointer). signal2 elements to be exclusive ored with signal1 elements**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsXor_32u_I_Ctx(const[Npp32u](https://docs.nvidia.com/nppdefs.html#c.Npp32u)*pSrc,[Npp32u](https://docs.nvidia.com/nppdefs.html#c.Npp32u)*pSrcDst, size_t nLength,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsXor_32u_I_Ctx)

-
32-bit unsigned integer in place signal exclusive or with signal.

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pSrcDst**–[In-Place Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1in_place_signal_pointer). signal2 elements to be exclusive ored with signal1 elements**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


### Signal Not[](https://docs.nvidia.com#signal-not)

#### Not[](https://docs.nvidia.com#group__signal__not_1signal_not)

Bitwise NOT of each sample of a signal.

Functions

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsNot_8u_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, size_t nLength,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsNot_8u_Ctx)

-
8-bit unsigned char not signal.

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsNot_16u_Ctx(const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrc,[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pDst, size_t nLength,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsNot_16u_Ctx)

-
16-bit unsigned short not signal.

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsNot_32u_Ctx(const[Npp32u](https://docs.nvidia.com/nppdefs.html#c.Npp32u)*pSrc,[Npp32u](https://docs.nvidia.com/nppdefs.html#c.Npp32u)*pDst, size_t nLength,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsNot_32u_Ctx)

-
32-bit unsigned integer not signal.

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsNot_8u_I_Ctx([Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrcDst, size_t nLength,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsNot_8u_I_Ctx)

-
8-bit unsigned char in place not signal.

- Parameters
-
**pSrcDst**–[In-Place Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1in_place_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsNot_16u_I_Ctx([Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrcDst, size_t nLength,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsNot_16u_I_Ctx)

-
16-bit unsigned short in place not signal.

- Parameters
-
**pSrcDst**–[In-Place Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1in_place_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsNot_32u_I_Ctx([Npp32u](https://docs.nvidia.com/nppdefs.html#c.Npp32u)*pSrcDst, size_t nLength,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsNot_32u_I_Ctx)

-
32-bit unsigned signed integer in place not signal.

- Parameters
-
**pSrcDst**–[In-Place Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1in_place_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


### Signal LShiftC[](https://docs.nvidia.com#signal-lshiftc)

#### LShiftC[](https://docs.nvidia.com#group__signal__lshiftc_1signal_lshiftc)

Left shifts the bits of each sample of a signal by a constant amount.

Functions

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsLShiftC_8u_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nValue,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, size_t nLength,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsLShiftC_8u_Ctx)

-
8-bit unsigned char signal left shift with constant.

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nValue**– Constant value to be used to left shift each vector element**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsLShiftC_16u_Ctx(const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrc, int nValue,[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pDst, size_t nLength,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsLShiftC_16u_Ctx)

-
16-bit unsigned short signal left shift with constant.

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nValue**– Constant value to be used to left shift each vector element**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsLShiftC_16s_Ctx(const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrc, int nValue,[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pDst, size_t nLength,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsLShiftC_16s_Ctx)

-
16-bit signed short signal left shift with constant.

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nValue**– Constant value to be used to left shift each vector element**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsLShiftC_32u_Ctx(const[Npp32u](https://docs.nvidia.com/nppdefs.html#c.Npp32u)*pSrc, int nValue,[Npp32u](https://docs.nvidia.com/nppdefs.html#c.Npp32u)*pDst, size_t nLength,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsLShiftC_32u_Ctx)

-
32-bit unsigned integer signal left shift with constant.

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nValue**– Constant value to be used to left shift each vector element**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsLShiftC_32s_Ctx(const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pSrc, int nValue,[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pDst, size_t nLength,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsLShiftC_32s_Ctx)

-
32-bit signed integer signal left shift with constant.

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nValue**– Constant value to be used to left shift each vector element**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsLShiftC_8u_I_Ctx(int nValue,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrcDst, size_t nLength,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsLShiftC_8u_I_Ctx)

-
8-bit unsigned char in place signal left shift with constant.

- Parameters
-
**pSrcDst**–[In-Place Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1in_place_signal_pointer).**nValue**– Constant value to be used to left shift each vector element**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsLShiftC_16u_I_Ctx(int nValue,[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrcDst, size_t nLength,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsLShiftC_16u_I_Ctx)

-
16-bit unsigned short in place signal left shift with constant.

- Parameters
-
**pSrcDst**–[In-Place Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1in_place_signal_pointer).**nValue**– Constant value to be used to left shift each vector element**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsLShiftC_16s_I_Ctx(int nValue,[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrcDst, size_t nLength,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsLShiftC_16s_I_Ctx)

-
16-bit signed short in place signal left shift with constant.

- Parameters
-
**pSrcDst**–[In-Place Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1in_place_signal_pointer).**nValue**– Constant value to be used to left shift each vector element**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsLShiftC_32u_I_Ctx(int nValue,[Npp32u](https://docs.nvidia.com/nppdefs.html#c.Npp32u)*pSrcDst, size_t nLength,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsLShiftC_32u_I_Ctx)

-
32-bit unsigned signed integer in place signal left shift with constant.

- Parameters
-
**pSrcDst**–[In-Place Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1in_place_signal_pointer).**nValue**– Constant value to be used to left shift each vector element**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsLShiftC_32s_I_Ctx(int nValue,[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pSrcDst, size_t nLength,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsLShiftC_32s_I_Ctx)

-
32-bit signed signed integer in place signal left shift with constant.

- Parameters
-
**pSrcDst**–[In-Place Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1in_place_signal_pointer).**nValue**– Constant value to be used to left shift each vector element**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


### Signal RShiftC[](https://docs.nvidia.com#signal-rshiftc)

#### RShiftC[](https://docs.nvidia.com#group__signal__rshiftc_1signal_rshiftc)

Right shifts the bits of each sample of a signal by a constant amount.

Functions

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsRShiftC_8u_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nValue,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, size_t nLength,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsRShiftC_8u_Ctx)

-
8-bit unsigned char signal right shift with constant.

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nValue**– Constant value to be used to right shift each vector element**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsRShiftC_16u_Ctx(const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrc, int nValue,[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pDst, size_t nLength,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsRShiftC_16u_Ctx)

-
16-bit unsigned short signal right shift with constant.

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nValue**– Constant value to be used to right shift each vector element**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsRShiftC_16s_Ctx(const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrc, int nValue,[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pDst, size_t nLength,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsRShiftC_16s_Ctx)

-
16-bit signed short signal right shift with constant.

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nValue**– Constant value to be used to right shift each vector element**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsRShiftC_32u_Ctx(const[Npp32u](https://docs.nvidia.com/nppdefs.html#c.Npp32u)*pSrc, int nValue,[Npp32u](https://docs.nvidia.com/nppdefs.html#c.Npp32u)*pDst, size_t nLength,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsRShiftC_32u_Ctx)

-
32-bit unsigned integer signal right shift with constant.

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nValue**– Constant value to be used to right shift each vector element**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsRShiftC_32s_Ctx(const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pSrc, int nValue,[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pDst, size_t nLength,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsRShiftC_32s_Ctx)

-
32-bit signed integer signal right shift with constant.

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**nValue**– Constant value to be used to right shift each vector element**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsRShiftC_8u_I_Ctx(int nValue,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrcDst, size_t nLength,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsRShiftC_8u_I_Ctx)

-
8-bit unsigned char in place signal right shift with constant.

- Parameters
-
**pSrcDst**–[In-Place Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1in_place_signal_pointer).**nValue**– Constant value to be used to right shift each vector element**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsRShiftC_16u_I_Ctx(int nValue,[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrcDst, size_t nLength,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsRShiftC_16u_I_Ctx)

-
16-bit unsigned short in place signal right shift with constant.

- Parameters
-
**pSrcDst**–[In-Place Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1in_place_signal_pointer).**nValue**– Constant value to be used to right shift each vector element**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsRShiftC_16s_I_Ctx(int nValue,[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrcDst, size_t nLength,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsRShiftC_16s_I_Ctx)

-
16-bit signed short in place signal right shift with constant.

- Parameters
-
**pSrcDst**–[In-Place Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1in_place_signal_pointer).**nValue**– Constant value to be used to right shift each vector element**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsRShiftC_32u_I_Ctx(int nValue,[Npp32u](https://docs.nvidia.com/nppdefs.html#c.Npp32u)*pSrcDst, size_t nLength,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsRShiftC_32u_I_Ctx)

-
32-bit unsigned signed integer in place signal right shift with constant.

- Parameters
-
**pSrcDst**–[In-Place Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1in_place_signal_pointer).**nValue**– Constant value to be used to right shift each vector element**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsRShiftC_32s_I_Ctx(int nValue,[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pSrcDst, size_t nLength,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsRShiftC_32s_I_Ctx)

-
32-bit signed signed integer in place signal right shift with constant.

- Parameters
-
**pSrcDst**–[In-Place Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1in_place_signal_pointer).**nValue**– Constant value to be used to right shift each vector element**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).