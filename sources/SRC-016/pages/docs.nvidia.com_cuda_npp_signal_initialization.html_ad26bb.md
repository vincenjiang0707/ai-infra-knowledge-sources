source: https://docs.nvidia.com/cuda/npp/signal_initialization.html

# Signal Initialization Functions[](https://docs.nvidia.com#signal-initialization-functions)

Functions that provide functionality of initialization signal like: set, zero or copy other signal.

## Signal Set[](https://docs.nvidia.com#signal-set)

### Set[](https://docs.nvidia.com#group__signal__set_1signal_set)

The set of set initialization operations available in the library.

Set

Set methods for 1D vectors of various types.

The copy methods operate on vector data given as a pointer to the underlying data-type (e.g. 8-bit vectors would be passed as pointers to Npp8u type) and length of the vectors, i.e. the number of items.

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsSet_8u_Ctx([Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)nValue,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, size_t nLength,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsSet_8u_Ctx)

-
8-bit unsigned char, vector set method.

- Parameters
-
**nValue**– Value used to initialize the vector pDst.**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsSet_8s_Ctx([Npp8s](https://docs.nvidia.com/nppdefs.html#c.Npp8s)nValue,[Npp8s](https://docs.nvidia.com/nppdefs.html#c.Npp8s)*pDst, size_t nLength,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsSet_8s_Ctx)

-
8-bit signed char, vector set method.

- Parameters
-
**nValue**– Value used to initialize the vector pDst.**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsSet_16u_Ctx([Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)nValue,[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pDst, size_t nLength,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsSet_16u_Ctx)

-
16-bit unsigned integer, vector set method.

- Parameters
-
**nValue**– Value used to initialize the vector pDst.**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsSet_16s_Ctx([Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)nValue,[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pDst, size_t nLength,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsSet_16s_Ctx)

-
16-bit signed integer, vector set method.

- Parameters
-
**nValue**– Value used to initialize the vector pDst.**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsSet_16sc_Ctx([Npp16sc](https://docs.nvidia.com/nppdefs.html#c.Npp16sc)nValue,[Npp16sc](https://docs.nvidia.com/nppdefs.html#c.Npp16sc)*pDst, size_t nLength,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsSet_16sc_Ctx)

-
16-bit integer complex, vector set method.

- Parameters
-
**nValue**– Value used to initialize the vector pDst.**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsSet_32u_Ctx([Npp32u](https://docs.nvidia.com/nppdefs.html#c.Npp32u)nValue,[Npp32u](https://docs.nvidia.com/nppdefs.html#c.Npp32u)*pDst, size_t nLength,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsSet_32u_Ctx)

-
32-bit unsigned integer, vector set method.

- Parameters
-
**nValue**– Value used to initialize the vector pDst.**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsSet_32s_Ctx([Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)nValue,[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pDst, size_t nLength,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsSet_32s_Ctx)

-
32-bit signed integer, vector set method.

- Parameters
-
**nValue**– Value used to initialize the vector pDst.**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsSet_32sc_Ctx([Npp32sc](https://docs.nvidia.com/nppdefs.html#c.Npp32sc)nValue,[Npp32sc](https://docs.nvidia.com/nppdefs.html#c.Npp32sc)*pDst, size_t nLength,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsSet_32sc_Ctx)

-
32-bit integer complex, vector set method.

- Parameters
-
**nValue**– Value used to initialize the vector pDst.**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsSet_32f_Ctx([Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)nValue,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pDst, size_t nLength,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsSet_32f_Ctx)

-
32-bit float, vector set method.

- Parameters
-
**nValue**– Value used to initialize the vector pDst.**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsSet_32fc_Ctx([Npp32fc](https://docs.nvidia.com/nppdefs.html#c.Npp32fc)nValue,[Npp32fc](https://docs.nvidia.com/nppdefs.html#c.Npp32fc)*pDst, size_t nLength,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsSet_32fc_Ctx)

-
32-bit float complex, vector set method.

- Parameters
-
**nValue**– Value used to initialize the vector pDst.**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsSet_64s_Ctx([Npp64s](https://docs.nvidia.com/nppdefs.html#c.Npp64s)nValue,[Npp64s](https://docs.nvidia.com/nppdefs.html#c.Npp64s)*pDst, size_t nLength,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsSet_64s_Ctx)

-
64-bit long long integer, vector set method.

- Parameters
-
**nValue**– Value used to initialize the vector pDst.**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsSet_64sc_Ctx([Npp64sc](https://docs.nvidia.com/nppdefs.html#c.Npp64sc)nValue,[Npp64sc](https://docs.nvidia.com/nppdefs.html#c.Npp64sc)*pDst, size_t nLength,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsSet_64sc_Ctx)

-
64-bit long long integer complex, vector set method.

- Parameters
-
**nValue**– Value used to initialize the vector pDst.**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsSet_64f_Ctx([Npp64f](https://docs.nvidia.com/nppdefs.html#c.Npp64f)nValue,[Npp64f](https://docs.nvidia.com/nppdefs.html#c.Npp64f)*pDst, size_t nLength,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsSet_64f_Ctx)

-
64-bit double, vector set method.

- Parameters
-
**nValue**– Value used to initialize the vector pDst.**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsSet_64fc_Ctx([Npp64fc](https://docs.nvidia.com/nppdefs.html#c.Npp64fc)nValue,[Npp64fc](https://docs.nvidia.com/nppdefs.html#c.Npp64fc)*pDst, size_t nLength,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsSet_64fc_Ctx)

-
64-bit double complex, vector set method.

- Parameters
-
**nValue**– Value used to initialize the vector pDst.**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


## Signal Zero[](https://docs.nvidia.com#signal-zero)

### Zero[](https://docs.nvidia.com#group__signal__zero_1signal_zero)

The set of zero initialization operations available in the library.

Zero

Set signals to zero.

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsZero_8u_Ctx([Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, size_t nLength,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsZero_8u_Ctx)

-
8-bit unsigned char, vector zero method.

- Parameters
-
**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsZero_16s_Ctx([Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pDst, size_t nLength,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsZero_16s_Ctx)

-
16-bit integer, vector zero method.

- Parameters
-
**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsZero_16sc_Ctx([Npp16sc](https://docs.nvidia.com/nppdefs.html#c.Npp16sc)*pDst, size_t nLength,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsZero_16sc_Ctx)

-
16-bit integer complex, vector zero method.

- Parameters
-
**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsZero_32s_Ctx([Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pDst, size_t nLength,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsZero_32s_Ctx)

-
32-bit integer, vector zero method.

- Parameters
-
**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsZero_32sc_Ctx([Npp32sc](https://docs.nvidia.com/nppdefs.html#c.Npp32sc)*pDst, size_t nLength,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsZero_32sc_Ctx)

-
32-bit integer complex, vector zero method.

- Parameters
-
**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsZero_32f_Ctx([Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pDst, size_t nLength,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsZero_32f_Ctx)

-
32-bit float, vector zero method.

- Parameters
-
**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsZero_32fc_Ctx([Npp32fc](https://docs.nvidia.com/nppdefs.html#c.Npp32fc)*pDst, size_t nLength,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsZero_32fc_Ctx)

-
32-bit float complex, vector zero method.

- Parameters
-
**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsZero_64s_Ctx([Npp64s](https://docs.nvidia.com/nppdefs.html#c.Npp64s)*pDst, size_t nLength,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsZero_64s_Ctx)

-
64-bit long long integer, vector zero method.

- Parameters
-
**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsZero_64sc_Ctx([Npp64sc](https://docs.nvidia.com/nppdefs.html#c.Npp64sc)*pDst, size_t nLength,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsZero_64sc_Ctx)

-
64-bit long long integer complex, vector zero method.

- Parameters
-
**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsZero_64f_Ctx([Npp64f](https://docs.nvidia.com/nppdefs.html#c.Npp64f)*pDst, size_t nLength,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsZero_64f_Ctx)

-
64-bit double, vector zero method.

- Parameters
-
**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsZero_64fc_Ctx([Npp64fc](https://docs.nvidia.com/nppdefs.html#c.Npp64fc)*pDst, size_t nLength,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsZero_64fc_Ctx)

-
64-bit double complex, vector zero method.

- Parameters
-
**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


## Signal Copy[](https://docs.nvidia.com#signal-copy)

### Copy[](https://docs.nvidia.com#group__signal__copy_1signal_copy)

The set of copy initialization operations available in the library.

Copy

Copy methods for various type signals.

Copy methods operate on signal data given as a pointer to the underlying data-type (e.g. 8-bit vectors would be passed as pointers to Npp8u type) and length of the vectors, i.e. the number of items.

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsCopy_8u_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, size_t nLength,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsCopy_8u_Ctx)

-
8-bit unsigned char, vector copy method

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsCopy_16s_Ctx(const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrc,[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pDst, size_t nLength,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsCopy_16s_Ctx)

-
16-bit signed short, vector copy method.

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsCopy_32s_Ctx(const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pSrc,[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pDst, size_t nLength,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsCopy_32s_Ctx)

-
32-bit signed integer, vector copy method.

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsCopy_32f_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pDst, size_t nLength,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsCopy_32f_Ctx)

-
32-bit float, vector copy method.

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsCopy_64s_Ctx(const[Npp64s](https://docs.nvidia.com/nppdefs.html#c.Npp64s)*pSrc,[Npp64s](https://docs.nvidia.com/nppdefs.html#c.Npp64s)*pDst, size_t nLength,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsCopy_64s_Ctx)

-
64-bit signed integer, vector copy method.

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsCopy_16sc_Ctx(const[Npp16sc](https://docs.nvidia.com/nppdefs.html#c.Npp16sc)*pSrc,[Npp16sc](https://docs.nvidia.com/nppdefs.html#c.Npp16sc)*pDst, size_t nLength,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsCopy_16sc_Ctx)

-
16-bit complex short, vector copy method.

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsCopy_32sc_Ctx(const[Npp32sc](https://docs.nvidia.com/nppdefs.html#c.Npp32sc)*pSrc,[Npp32sc](https://docs.nvidia.com/nppdefs.html#c.Npp32sc)*pDst, size_t nLength,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsCopy_32sc_Ctx)

-
32-bit complex signed integer, vector copy method.

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsCopy_32fc_Ctx(const[Npp32fc](https://docs.nvidia.com/nppdefs.html#c.Npp32fc)*pSrc,[Npp32fc](https://docs.nvidia.com/nppdefs.html#c.Npp32fc)*pDst, size_t nLength,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsCopy_32fc_Ctx)

-
32-bit complex float, vector copy method.

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsCopy_64sc_Ctx(const[Npp64sc](https://docs.nvidia.com/nppdefs.html#c.Npp64sc)*pSrc,[Npp64sc](https://docs.nvidia.com/nppdefs.html#c.Npp64sc)*pDst, size_t nLength,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsCopy_64sc_Ctx)

-
64-bit complex signed integer, vector copy method.

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsCopy_64fc_Ctx(const[Npp64fc](https://docs.nvidia.com/nppdefs.html#c.Npp64fc)*pSrc,[Npp64fc](https://docs.nvidia.com/nppdefs.html#c.Npp64fc)*pDst, size_t nLength,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsCopy_64fc_Ctx)

-
64-bit complex double, vector copy method.

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pDst**–[Destination Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1destination_signal_pointer).**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).