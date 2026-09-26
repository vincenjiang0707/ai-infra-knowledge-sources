source: https://docs.nvidia.com/cuda/npp/

# NVIDIA 2D Image and Signal Processing Performance Primitives (NPP)[](https://docs.nvidia.com#nvidia-2d-image-and-signal-processing-performance-primitives-npp)

# Indices and Search[](https://docs.nvidia.com#indices-and-search)

-
[What is NPP ?](https://docs.nvidia.com/introduction.html) -
[General Conventions](https://docs.nvidia.com/introduction.html#general-conventions) -
[Image Processing Conventions](https://docs.nvidia.com/introduction.html#image-processing-conventions)[Function Naming](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1nppi_naming)-
[Image Data](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1passing_image_data)[Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1line_step)-
[Parameter Names for Image Data](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1image_data_parameter_names)[Passing Source-Image Data](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image)[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer)[Source-Batch-Images Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_batch_images_pointer)[Source-Planar-Image Pointer Array](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_planar_image_pointer_array)[Source-Planar-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_planar_image_pointer)[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step)[Source-Planar-Image Line Step Array](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_planar_image_line_step_array)[Source-Planar-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_planar_image_line_step)[Passing Destination-Image Data](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image)[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer)[Destination-Batch-Images Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_batch_images_pointer)[Destination-Planar-Image Pointer Array](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_planar_image_pointer_array)[Destination-Planar-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_planar_image_pointer)[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step)[Destination-Planar-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_planar_image_line_step)[Passing In-Place Image Data](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1in_place_image)[In-Place Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1in_place_image_pointer)[In-Place-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1in_place_image_line_step)[Passing Mask-Image Data](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1mask_image)[Mask-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1mask_image_pointer)[Mask-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1mask_image_line_step)[Passing Channel-of-Interest Data](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1channel_of_interest_section)[Channel_of_Interest Number](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1channel_of_interest_number)

[Image Data Alignment Requirements](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1image_data_alignment)[Image Data Related Error Codes](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1image_data_error_codes)

-
[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification) [Masked Operation](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1masked_operation)-
[Channel-of-Interest API](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1channel_of_interest) -
[Source-Image Sampling](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_sampling)

-
[Signal Processing Conventions](https://docs.nvidia.com/introduction.html#signal-processing-conventions) [Data Types, Structs, Enums, and Constants](https://docs.nvidia.com/nppdefs.html)[Core NPP Functions](https://docs.nvidia.com/core_npp.html)-
[Image Arithmetic And Logical Operations](https://docs.nvidia.com/image_arithmetic_and_logical_operations.html) -
[Image Color Conversion Functions](https://docs.nvidia.com/image_color_conversion.html)-
[Color Processing Functions](https://docs.nvidia.com/image_color_conversion.html#color-processing-functions) -
[Color Sampling Format Conversion Functions](https://docs.nvidia.com/image_color_conversion.html#color-sampling-format-conversion-functions)[YCbCr420ToYCbCr411](https://docs.nvidia.com/image_color_conversion.html#ycbcr420toycbcr411)[YCbCr422ToYCbCr422](https://docs.nvidia.com/image_color_conversion.html#ycbcr422toycbcr422)[YCbCr422ToYCrCb422](https://docs.nvidia.com/image_color_conversion.html#ycbcr422toycrcb422)[YCbCr422ToCbYCr422](https://docs.nvidia.com/image_color_conversion.html#ycbcr422tocbycr422)[CbYCr422ToYCbCr411](https://docs.nvidia.com/image_color_conversion.html#cbycr422toycbcr411)[YCbCr422ToYCbCr420](https://docs.nvidia.com/image_color_conversion.html#ycbcr422toycbcr420)[YCrCb420ToYCbCr422](https://docs.nvidia.com/image_color_conversion.html#ycrcb420toycbcr422)[YCbCr422ToYCrCb420](https://docs.nvidia.com/image_color_conversion.html#ycbcr422toycrcb420)[YCbCr422ToYCbCr411](https://docs.nvidia.com/image_color_conversion.html#ycbcr422toycbcr411)[YCrCb422ToYCbCr422](https://docs.nvidia.com/image_color_conversion.html#ycrcb422toycbcr422)[YCrCb422ToYCbCr420](https://docs.nvidia.com/image_color_conversion.html#ycrcb422toycbcr420)[YCrCb422ToYCbCr411](https://docs.nvidia.com/image_color_conversion.html#ycrcb422toycbcr411)[CbYCr422ToYCbCr422](https://docs.nvidia.com/image_color_conversion.html#cbycr422toycbcr422)[CbYCr422ToYCbCr420](https://docs.nvidia.com/image_color_conversion.html#cbycr422toycbcr420)[CbYCr422ToYCrCb420](https://docs.nvidia.com/image_color_conversion.html#cbycr422toycrcb420)[YCbCr420ToYCbCr420](https://docs.nvidia.com/image_color_conversion.html#ycbcr420toycbcr420)[YCbCr420ToYCbCr422](https://docs.nvidia.com/image_color_conversion.html#ycbcr420toycbcr422)[YCbCr420ToCbYCr422](https://docs.nvidia.com/image_color_conversion.html#ycbcr420tocbycr422)[YCbCr420ToYCrCb420](https://docs.nvidia.com/image_color_conversion.html#ycbcr420toycrcb420)[YCrCb420ToCbYCr422](https://docs.nvidia.com/image_color_conversion.html#ycrcb420tocbycr422)[YCrCb420ToYCbYCr420](https://docs.nvidia.com/image_color_conversion.html#ycrcb420toycbycr420)[YCrCb420ToYCbYCr411](https://docs.nvidia.com/image_color_conversion.html#ycrcb420toycbycr411)[YCbCr411ToYCbCr411](https://docs.nvidia.com/image_color_conversion.html#ycbcr411toycbcr411)[YCbCr411ToYCbCr422](https://docs.nvidia.com/image_color_conversion.html#ycbcr411toycbcr422)[YCbCr411ToYCrCb422](https://docs.nvidia.com/image_color_conversion.html#ycbcr411toycrcb422)[YCbCr411ToYCbCr420](https://docs.nvidia.com/image_color_conversion.html#ycbcr411toycbcr420)[YCbCr411ToYCrCb420](https://docs.nvidia.com/image_color_conversion.html#ycbcr411toycrcb420)[NV12ToYUV420](https://docs.nvidia.com/image_color_conversion.html#nv12toyuv420)

-
[Color Model Conversion Functions](https://docs.nvidia.com/image_color_conversion.html#color-model-conversion-functions)[RGBToYUV](https://docs.nvidia.com/image_color_conversion.html#rgbtoyuv)[BGRToYUV](https://docs.nvidia.com/image_color_conversion.html#bgrtoyuv)[YUVToRGB](https://docs.nvidia.com/image_color_conversion.html#yuvtorgb)[YUVToRGBBatch](https://docs.nvidia.com/image_color_conversion.html#yuvtorgbbatch)[YUVToRGBBatchAdvanced](https://docs.nvidia.com/image_color_conversion.html#yuvtorgbbatchadvanced)[YUVToBGR](https://docs.nvidia.com/image_color_conversion.html#yuvtobgr)[YUVToBGRBatch](https://docs.nvidia.com/image_color_conversion.html#yuvtobgrbatch)[YUVToBGRBatchAdvanced](https://docs.nvidia.com/image_color_conversion.html#yuvtobgrbatchadvanced)[RGBToYUV422](https://docs.nvidia.com/image_color_conversion.html#rgbtoyuv422)[YUV422ToRGB](https://docs.nvidia.com/image_color_conversion.html#yuv422torgb)[YUV422ToRGBBatch](https://docs.nvidia.com/image_color_conversion.html#yuv422torgbbatch)[YUV422ToRGBBatchAdvanced](https://docs.nvidia.com/image_color_conversion.html#yuv422torgbbatchadvanced)[YUV422ToBGRBatch](https://docs.nvidia.com/image_color_conversion.html#yuv422tobgrbatch)[YUV422ToBGRBatchAdvanced](https://docs.nvidia.com/image_color_conversion.html#yuv422tobgrbatchadvanced)[RGBToYUV420](https://docs.nvidia.com/image_color_conversion.html#rgbtoyuv420)[YUV420ToRGB](https://docs.nvidia.com/image_color_conversion.html#yuv420torgb)[YUV420ToRGBBatch](https://docs.nvidia.com/image_color_conversion.html#yuv420torgbbatch)[YUV420ToRGBBatchAdvanced](https://docs.nvidia.com/image_color_conversion.html#yuv420torgbbatchadvanced)[NV12ToRGB](https://docs.nvidia.com/image_color_conversion.html#nv12torgb)[NV21ToRGB](https://docs.nvidia.com/image_color_conversion.html#nv21torgb)[BGRToYUV420](https://docs.nvidia.com/image_color_conversion.html#bgrtoyuv420)[YUV420ToBGR](https://docs.nvidia.com/image_color_conversion.html#yuv420tobgr)[YUV420ToBGRBatch](https://docs.nvidia.com/image_color_conversion.html#yuv420tobgrbatch)[YUV420ToBGRBatchAdvanced](https://docs.nvidia.com/image_color_conversion.html#yuv420tobgrbatchadvanced)[NV12ToBGR](https://docs.nvidia.com/image_color_conversion.html#nv12tobgr)[NV21ToBGR](https://docs.nvidia.com/image_color_conversion.html#nv21tobgr)[RGBToYCbCr](https://docs.nvidia.com/image_color_conversion.html#rgbtoycbcr)[YCbCrToRGB](https://docs.nvidia.com/image_color_conversion.html#ycbcrtorgb)[YCbCrToRGBBatch](https://docs.nvidia.com/image_color_conversion.html#ycbcrtorgbbatch)[YCbCrToRGBBatchAdvanced](https://docs.nvidia.com/image_color_conversion.html#ycbcrtorgbbatchadvanced)[YCbCrToBGR](https://docs.nvidia.com/image_color_conversion.html#ycbcrtobgr)[YCbCrToBGRBatch](https://docs.nvidia.com/image_color_conversion.html#ycbcrtobgrbatch)[YCbCrToBGRBatchAdvanced](https://docs.nvidia.com/image_color_conversion.html#ycbcrtobgrbatchadvanced)[YCbCrToBGR709CSC](https://docs.nvidia.com/image_color_conversion.html#ycbcrtobgr709csc)[RGBToYCbCr422](https://docs.nvidia.com/image_color_conversion.html#rgbtoycbcr422)[YCbCr422ToRGB](https://docs.nvidia.com/image_color_conversion.html#ycbcr422torgb)[YCbCr422ToRGBBatch](https://docs.nvidia.com/image_color_conversion.html#ycbcr422torgbbatch)[YCbCr422ToRGBBatchAdvanced](https://docs.nvidia.com/image_color_conversion.html#ycbcr422torgbbatchadvanced)[RGBToYCrCb422](https://docs.nvidia.com/image_color_conversion.html#rgbtoycrcb422)[YCrCb422ToRGB](https://docs.nvidia.com/image_color_conversion.html#ycrcb422torgb)[YCbCr422ToBGR](https://docs.nvidia.com/image_color_conversion.html#ycbcr422tobgr)[YCbCr422ToBGRBatch](https://docs.nvidia.com/image_color_conversion.html#ycbcr422tobgrbatch)[YCbCr422ToBGRBatchAdvanced](https://docs.nvidia.com/image_color_conversion.html#ycbcr422tobgrbatchadvanced)[RGBToCbYCr422](https://docs.nvidia.com/image_color_conversion.html#rgbtocbycr422)[CbYCr422ToRGB](https://docs.nvidia.com/image_color_conversion.html#cbycr422torgb)[BGRToCbYCr422](https://docs.nvidia.com/image_color_conversion.html#bgrtocbycr422)[BGRToCbYCr422 709HDTV](https://docs.nvidia.com/image_color_conversion.html#bgrtocbycr422-709hdtv)[CbYCr422ToBGR](https://docs.nvidia.com/image_color_conversion.html#cbycr422tobgr)[CbYCr422ToBGR 709HDTV](https://docs.nvidia.com/image_color_conversion.html#cbycr422tobgr-709hdtv)[RGBToYCbCr420](https://docs.nvidia.com/image_color_conversion.html#rgbtoycbcr420)[YCbCr420ToRGB](https://docs.nvidia.com/image_color_conversion.html#ycbcr420torgb)[YCbCr420ToRGBBatch](https://docs.nvidia.com/image_color_conversion.html#ycbcr420torgbbatch)[YCbCr420ToRGBBatchAdvanced](https://docs.nvidia.com/image_color_conversion.html#ycbcr420torgbbatchadvanced)[RGBToYCrCb420](https://docs.nvidia.com/image_color_conversion.html#rgbtoycrcb420)[YCrCb420ToRGB](https://docs.nvidia.com/image_color_conversion.html#ycrcb420torgb)[BGRToYCbCr420](https://docs.nvidia.com/image_color_conversion.html#bgrtoycbcr420)[BGRToYCbCr420 709CSC](https://docs.nvidia.com/image_color_conversion.html#bgrtoycbcr420-709csc)[BGRToYCbCr420 709HDTV](https://docs.nvidia.com/image_color_conversion.html#bgrtoycbcr420-709hdtv)[BGRToYCrCb420 709CSC](https://docs.nvidia.com/image_color_conversion.html#bgrtoycrcb420-709csc)[YCbCr420ToBGR](https://docs.nvidia.com/image_color_conversion.html#ycbcr420tobgr)[YCbCr420ToBGRBatch](https://docs.nvidia.com/image_color_conversion.html#ycbcr420tobgrbatch)[YCbCr420ToBGRBatchAdvanced](https://docs.nvidia.com/image_color_conversion.html#ycbcr420tobgrbatchadvanced)[YCbCr420ToBGR 709CSC](https://docs.nvidia.com/image_color_conversion.html#ycbcr420tobgr-709csc)[YCbCr420ToBGR 709HDTV](https://docs.nvidia.com/image_color_conversion.html#ycbcr420tobgr-709hdtv)[BGRToYCrCb420](https://docs.nvidia.com/image_color_conversion.html#bgrtoycrcb420)[BGRToYCbCr411](https://docs.nvidia.com/image_color_conversion.html#bgrtoycbcr411)[BGRToYCbCr](https://docs.nvidia.com/image_color_conversion.html#bgrtoycbcr)[YCbCr411ToBGR](https://docs.nvidia.com/image_color_conversion.html#ycbcr411tobgr)[YCbCr411ToRGB](https://docs.nvidia.com/image_color_conversion.html#ycbcr411torgb)[RGBToXYZ](https://docs.nvidia.com/image_color_conversion.html#rgbtoxyz)[XYZToRGB](https://docs.nvidia.com/image_color_conversion.html#xyztorgb)[RGBToLUV](https://docs.nvidia.com/image_color_conversion.html#rgbtoluv)[LUVToRGB](https://docs.nvidia.com/image_color_conversion.html#luvtorgb)[BGRToLab](https://docs.nvidia.com/image_color_conversion.html#bgrtolab)[LabToBGR](https://docs.nvidia.com/image_color_conversion.html#labtobgr)[RGBToYCC](https://docs.nvidia.com/image_color_conversion.html#rgbtoycc)[YCCToRGB](https://docs.nvidia.com/image_color_conversion.html#ycctorgb)[YCCKToCMYK_JPEG](https://docs.nvidia.com/image_color_conversion.html#yccktocmyk-jpeg)[CMYKOrYCCKJPEGToRGB](https://docs.nvidia.com/image_color_conversion.html#cmykorycckjpegtorgb)[YCCKJPEGOrCMYKToBGR](https://docs.nvidia.com/image_color_conversion.html#ycckjpegorcmyktobgr)[RGBToHLS](https://docs.nvidia.com/image_color_conversion.html#rgbtohls)[HLSToRGB](https://docs.nvidia.com/image_color_conversion.html#hlstorgb)[BGRToHLS](https://docs.nvidia.com/image_color_conversion.html#bgrtohls)[HLSToBGR](https://docs.nvidia.com/image_color_conversion.html#hlstobgr)[RBGToHSV](https://docs.nvidia.com/image_color_conversion.html#rbgtohsv)[HSVToRGB](https://docs.nvidia.com/image_color_conversion.html#hsvtorgb)[JPEG Color Conversion](https://docs.nvidia.com/image_color_conversion.html#jpeg-color-conversion)


-
-
[Image Data Exchange And Initialization Functions](https://docs.nvidia.com/image_data_exchange_and_initialization.html)-
[Set](https://docs.nvidia.com/image_data_exchange_and_initialization.html#group__image__set_1image_set) -
[Masked Set](https://docs.nvidia.com/image_data_exchange_and_initialization.html#group__image__masked__set_1image_masked_set) -
[Channel Set](https://docs.nvidia.com/image_data_exchange_and_initialization.html#group__image__channel__set_1image_channel_set) -
[Copy](https://docs.nvidia.com/image_data_exchange_and_initialization.html#group__image__copy_1image_copy) -
[Masked Copy](https://docs.nvidia.com/image_data_exchange_and_initialization.html#group__image__masked__copy_1image_masked_copy) -
[Channel Copy](https://docs.nvidia.com/image_data_exchange_and_initialization.html#group__image__channel__copy_1image_channel_copy) -
[Extract Channel Copy](https://docs.nvidia.com/image_data_exchange_and_initialization.html#group__image__extract__channel__copy_1image_extract_channel_copy) -
[Insert Channel Copy](https://docs.nvidia.com/image_data_exchange_and_initialization.html#group__image__insert__channel__copy_1image_insert_channel_copy) -
[Packed To Planar Channel Copy](https://docs.nvidia.com/image_data_exchange_and_initialization.html#group__image__packed__to__planar__channel__copy_1image_packed_to_planar_channel_copy) -
[Planar To Packed Channel Copy](https://docs.nvidia.com/image_data_exchange_and_initialization.html#group__image__planar__to__packed__channel__copy_1image_planar_to_packed_channel_copy) -
[Copy Constant Border](https://docs.nvidia.com/image_data_exchange_and_initialization.html#group__image__copy__constant__border_1image_copy_constant_border) -
[Copy Replicate Border](https://docs.nvidia.com/image_data_exchange_and_initialization.html#group__image__copy__replicate__border_1image_copy_replicate_border) -
[Copy Wrap Border](https://docs.nvidia.com/image_data_exchange_and_initialization.html#group__image__copy__wrap__border_1image_copy_wrap_border) -
[Copy Sub-Pixel](https://docs.nvidia.com/image_data_exchange_and_initialization.html#group__image__copy__sub__pixel_1image_copy_sub_pixel) [Convert Bit Depth](https://docs.nvidia.com/image_data_exchange_and_initialization.html#group__image__convert_1image_convert)-
[Convert To Increased Bit Depth](https://docs.nvidia.com/image_data_exchange_and_initialization.html#group__image__convert__increase_1image_convert_increase) -
[Convert To Decreased Bit Depth](https://docs.nvidia.com/image_data_exchange_and_initialization.html#group__image__convert__decrease_1image_convert_decrease) [Scale Bit Depth](https://docs.nvidia.com/image_data_exchange_and_initialization.html#group__image__scale_1image_scale)-
[Scale To Higher Bit Depth](https://docs.nvidia.com/image_data_exchange_and_initialization.html#group__image__scale__to__higher__bit__depth_1image_scale_to_higher_bit_depth) -
[Scale To Lower Bit Depth](https://docs.nvidia.com/image_data_exchange_and_initialization.html#group__image__scale__to__lower__bit__depth_1image_scale_to_lower_bit_depth) -
[Duplicate Channel](https://docs.nvidia.com/image_data_exchange_and_initialization.html#group__image__duplicate__channel_1image_duplicate_channel) -
[Transpose](https://docs.nvidia.com/image_data_exchange_and_initialization.html#group__image__transpose_1image_transpose) [Swap Channels](https://docs.nvidia.com/image_data_exchange_and_initialization.html#group__image__swap__channels_1image_swap_channels)

-
-
[Image Filtering Functions](https://docs.nvidia.com/image_filtering_functions.html)-
[Image 1D Linear Filters](https://docs.nvidia.com/image_filtering_functions.html#image-1d-linear-filters)[1DLinearFilter](https://docs.nvidia.com/image_filtering_functions.html#group__image__1D__linear__filter_1image_1D_linear_filter)-
[Image Filter Column](https://docs.nvidia.com/image_filtering_functions.html#image-filter-column) -
[Image Filter Column Border](https://docs.nvidia.com/image_filtering_functions.html#image-filter-column-border) -
[Image Filter Column 32f](https://docs.nvidia.com/image_filtering_functions.html#image-filter-column-32f) -
[Image Filter Column Border 32f](https://docs.nvidia.com/image_filtering_functions.html#image-filter-column-border-32f) -
[Image Filter Row](https://docs.nvidia.com/image_filtering_functions.html#image-filter-row) -
[Image Filter Row Border](https://docs.nvidia.com/image_filtering_functions.html#image-filter-row-border) -
[Image Filter Row 32f](https://docs.nvidia.com/image_filtering_functions.html#image-filter-row-32f) -
[Image Filter Row Border 32f](https://docs.nvidia.com/image_filtering_functions.html#image-filter-row-border-32f) -
[Image Filter 1D Window Sum](https://docs.nvidia.com/image_filtering_functions.html#image-filter-1d-window-sum) -
[Image Filter 1D Window Column Sum](https://docs.nvidia.com/image_filtering_functions.html#image-filter-1d-window-column-sum) -
[Image Filter 1D Window Row Sum](https://docs.nvidia.com/image_filtering_functions.html#image-filter-1d-window-row-sum) -
[Image Filter 1D Window Sum Border](https://docs.nvidia.com/image_filtering_functions.html#image-filter-1d-window-sum-border) -
[Image Filter 1D Window Column Sum Border](https://docs.nvidia.com/image_filtering_functions.html#image-filter-1d-window-column-sum-border) -
[Image Filter 1D Window Row Sum Border](https://docs.nvidia.com/image_filtering_functions.html#image-filter-1d-window-row-sum-border)

-
[Image Convolution](https://docs.nvidia.com/image_filtering_functions.html#image-convolution) -
[2D Fixed Linear Filters](https://docs.nvidia.com/image_filtering_functions.html#d-fixed-linear-filters) -
[Rank Filters](https://docs.nvidia.com/image_filtering_functions.html#rank-filters) -
[Fixed Filters](https://docs.nvidia.com/image_filtering_functions.html#fixed-filters)[Fixed Filters](https://docs.nvidia.com/image_filtering_functions.html#group__fixed__filters_1fixed_filters)-
[Image Filter Prewitt](https://docs.nvidia.com/image_filtering_functions.html#image-filter-prewitt) -
[Image Filter Prewitt Border](https://docs.nvidia.com/image_filtering_functions.html#image-filter-prewitt-border) -
[Image Filter Scharr](https://docs.nvidia.com/image_filtering_functions.html#image-filter-scharr) -
[Image Filter Scharr Border](https://docs.nvidia.com/image_filtering_functions.html#image-filter-scharr-border) -
[Image Filter Sobel](https://docs.nvidia.com/image_filtering_functions.html#image-filter-sobel) -
[Image Filter Sobel Border](https://docs.nvidia.com/image_filtering_functions.html#image-filter-sobel-border) -
[Image Filter Roberts](https://docs.nvidia.com/image_filtering_functions.html#image-filter-roberts) -
[Image Filter Roberts Border](https://docs.nvidia.com/image_filtering_functions.html#image-filter-roberts-border) -
[Image Filter Laplace](https://docs.nvidia.com/image_filtering_functions.html#image-filter-laplace) -
[Image Filter Laplace Border](https://docs.nvidia.com/image_filtering_functions.html#image-filter-laplace-border) -
[Image Filter Gauss](https://docs.nvidia.com/image_filtering_functions.html#image-filter-gauss) -
[Image Filter Gauss Advanced](https://docs.nvidia.com/image_filtering_functions.html#image-filter-gauss-advanced) -
[Image Filter Gauss Border](https://docs.nvidia.com/image_filtering_functions.html#image-filter-gauss-border) -
[Image Filter Advanced Gauss Border](https://docs.nvidia.com/image_filtering_functions.html#image-filter-advanced-gauss-border) -
[Image Filter Gauss Pyramid Layer Down Border](https://docs.nvidia.com/image_filtering_functions.html#image-filter-gauss-pyramid-layer-down-border) -
[Image Filter Gauss Pyramid Layer Up Border](https://docs.nvidia.com/image_filtering_functions.html#image-filter-gauss-pyramid-layer-up-border) -
[Image Filter Bilateral Gauss Border](https://docs.nvidia.com/image_filtering_functions.html#image-filter-bilateral-gauss-border) -
[Image Filter High Pass](https://docs.nvidia.com/image_filtering_functions.html#image-filter-high-pass) -
[Image Filter High Pass Border](https://docs.nvidia.com/image_filtering_functions.html#image-filter-high-pass-border) -
[Image Filter Low Pass](https://docs.nvidia.com/image_filtering_functions.html#image-filter-low-pass) -
[Image Filter Low Pass Border](https://docs.nvidia.com/image_filtering_functions.html#image-filter-low-pass-border) -
[Image Filter Sharpen](https://docs.nvidia.com/image_filtering_functions.html#image-filter-sharpen) -
[Image Filter Sharpen Border](https://docs.nvidia.com/image_filtering_functions.html#image-filter-sharpen-border) -
[Image Filter Unsharp Border](https://docs.nvidia.com/image_filtering_functions.html#image-filter-unsharp-border) -
[Image Filter Wiener Border](https://docs.nvidia.com/image_filtering_functions.html#image-filter-wiener-border) -
[Image Filter Gradient Vector Prewitt Border](https://docs.nvidia.com/image_filtering_functions.html#image-filter-gradient-vector-prewitt-border) -
[Image Filter Gradient Vector Scharr Border](https://docs.nvidia.com/image_filtering_functions.html#image-filter-gradient-vector-scharr-border) -
[Image Filter Gradient Vector Sobel Border](https://docs.nvidia.com/image_filtering_functions.html#image-filter-gradient-vector-sobel-border)

-
[Computer Vision Filtering Functions](https://docs.nvidia.com/image_filtering_functions.html#computer-vision-filtering-functions) -
[Image Filter Flood Fill](https://docs.nvidia.com/image_filtering_functions.html#image-filter-flood-fill) -
[Label Markers](https://docs.nvidia.com/image_filtering_functions.html#label-markers) [Bound Segments](https://docs.nvidia.com/image_filtering_functions.html#bound-segments)-
[Watershed Segmentation](https://docs.nvidia.com/image_filtering_functions.html#watershed-segmentation)

-
-
[Image Geometry Transforms Functions](https://docs.nvidia.com/image_geometry_transforms.html)[Geometric Transform API Specifics](https://docs.nvidia.com/image_geometry_transforms.html#group__image__geometry__transforms_1geometric_transform_api)[Geometric Transforms and ROIs](https://docs.nvidia.com/image_geometry_transforms.html#group__image__geometry__transforms_1geometric_transform_roi)[Pixel Interpolation](https://docs.nvidia.com/image_geometry_transforms.html#group__image__geometry__transforms_1geometric_transforms_interpolation)[Resize Error Codes](https://docs.nvidia.com/image_geometry_transforms.html#group__image__geometry__transforms_1resize_error_codes)[ResizeSqrPixel](https://docs.nvidia.com/image_geometry_transforms.html#group__image__resize__square__pixel_1image_resize_square_pixel)[Resize](https://docs.nvidia.com/image_geometry_transforms.html#group__image__resize_1image_resize)-
[ResizeBatch](https://docs.nvidia.com/image_geometry_transforms.html#group__image__resize__batch_1image_resize_batch) [Remap](https://docs.nvidia.com/image_geometry_transforms.html#group__image__remap_1image_remap)-
[Error Codes](https://docs.nvidia.com/image_geometry_transforms.html#group__image__remap_1remap_error_codes) [Rotate](https://docs.nvidia.com/image_geometry_transforms.html#group__image__rotate_1image_rotate)-
[Rotate Error Codes](https://docs.nvidia.com/image_geometry_transforms.html#group__image__rotate_1rotate_error_codes) [Rotate Utility Functions](https://docs.nvidia.com/image_geometry_transforms.html#group__rotate__utility__functions_1rotate_utility_functions)[Mirror](https://docs.nvidia.com/image_geometry_transforms.html#group__image__mirror_1image_mirror)-
[Mirror Error Codes](https://docs.nvidia.com/image_geometry_transforms.html#group__image__mirror_1mirror_error_codes) -
[Affine Transforms](https://docs.nvidia.com/image_geometry_transforms.html#affine-transforms) -
[Perspective Transforms](https://docs.nvidia.com/image_geometry_transforms.html#perspective-transforms)

-
[Image Linear Transforms Functions](https://docs.nvidia.com/image_linear_transforms.html) -
[Image Morphological Operations](https://docs.nvidia.com/image_morphological_operations.html) -
[Image Statistics Functions](https://docs.nvidia.com/image_statistics_functions.html)[CommonGetBufferHostSizeParameters](https://docs.nvidia.com/image_statistics_functions.html#group__image__statistics__functions_1CommonGetBufferHostSizeParameters)-
[Image Sum](https://docs.nvidia.com/image_statistics_functions.html#image-sum) -
[Image Min](https://docs.nvidia.com/image_statistics_functions.html#image-min) -
[Image Min Index](https://docs.nvidia.com/image_statistics_functions.html#image-min-index) -
[Image Max](https://docs.nvidia.com/image_statistics_functions.html#image-max) -
[Image Max Index](https://docs.nvidia.com/image_statistics_functions.html#image-max-index) -
[Image MinMax](https://docs.nvidia.com/image_statistics_functions.html#image-minmax) -
[Image Mean](https://docs.nvidia.com/image_statistics_functions.html#image-mean) -
[Image Mean StdDev](https://docs.nvidia.com/image_statistics_functions.html#image-mean-stddev) -
[Image Norms](https://docs.nvidia.com/image_statistics_functions.html#image-norms) -
[Image DotProd](https://docs.nvidia.com/image_statistics_functions.html#image-dotprod) -
[Image Count In Range](https://docs.nvidia.com/image_statistics_functions.html#image-count-in-range) -
[Image MaxEvery](https://docs.nvidia.com/image_statistics_functions.html#image-maxevery) -
[Image MinEvery](https://docs.nvidia.com/image_statistics_functions.html#image-minevery) -
[Image Integral](https://docs.nvidia.com/image_statistics_functions.html#image-integral) -
[Image Square Integral](https://docs.nvidia.com/image_statistics_functions.html#image-square-integral) -
[Image RectStdDev](https://docs.nvidia.com/image_statistics_functions.html#image-rectstddev) -
[Image Histogram Even](https://docs.nvidia.com/image_statistics_functions.html#image-histogram-even) -
[Image Histogram Range](https://docs.nvidia.com/image_statistics_functions.html#image-histogram-range) -
[Image Proximity](https://docs.nvidia.com/image_statistics_functions.html#image-proximity) -
[Image Square Distance Full Norm](https://docs.nvidia.com/image_statistics_functions.html#image-square-distance-full-norm) -
[Image Square Distance Same Norm](https://docs.nvidia.com/image_statistics_functions.html#image-square-distance-same-norm) -
[Image Square Distance Valid Norm](https://docs.nvidia.com/image_statistics_functions.html#image-square-distance-valid-norm) -
[Image Cross Correlation Full Norm](https://docs.nvidia.com/image_statistics_functions.html#image-cross-correlation-full-norm) -
[Image Cross Correlation Same Norm](https://docs.nvidia.com/image_statistics_functions.html#image-cross-correlation-same-norm) -
[Image Cross Correlation Valid Norm](https://docs.nvidia.com/image_statistics_functions.html#image-cross-correlation-valid-norm) -
[Image Cross Correlation Valid](https://docs.nvidia.com/image_statistics_functions.html#image-cross-correlation-valid) -
[Image Cross Correlation Full Norm Level](https://docs.nvidia.com/image_statistics_functions.html#image-cross-correlation-full-norm-level) -
[Image Cross Correlation Same Norm Level](https://docs.nvidia.com/image_statistics_functions.html#image-cross-correlation-same-norm-level) -
[Image Cross Correlation Valid Norm Level](https://docs.nvidia.com/image_statistics_functions.html#image-cross-correlation-valid-norm-level) -
[Image Cross Correlation Full Norm Level Advanced](https://docs.nvidia.com/image_statistics_functions.html#image-cross-correlation-full-norm-level-advanced) -
[Image Cross Correlation Same Norm Level Advanced](https://docs.nvidia.com/image_statistics_functions.html#image-cross-correlation-same-norm-level-advanced) -
[Image Cross Correlation Valid Norm Level Advanced](https://docs.nvidia.com/image_statistics_functions.html#image-cross-correlation-valid-norm-level-advanced) -
[Image Quality Index](https://docs.nvidia.com/image_statistics_functions.html#image-quality-index) -
[Image Maximum Error](https://docs.nvidia.com/image_statistics_functions.html#image-maximum-error) -
[Image Average Error](https://docs.nvidia.com/image_statistics_functions.html#image-average-error) -
[Image Maximum Relative Error](https://docs.nvidia.com/image_statistics_functions.html#image-maximum-relative-error) -
[Image Average Relative Error](https://docs.nvidia.com/image_statistics_functions.html#image-average-relative-error) -
[Image Quality Assessment IQA](https://docs.nvidia.com/image_statistics_functions.html#image-quality-assessment-iqa) -
[Image Batch Quality Assessment](https://docs.nvidia.com/image_statistics_functions.html#image-batch-quality-assessment) -
[Image Advanced Batch Quality Assessment](https://docs.nvidia.com/image_statistics_functions.html#image-advanced-batch-quality-assessment)

-
[Image Threshold And Compare Operations](https://docs.nvidia.com/image_threshold_and_compare_operations.html)-
[Image Threshold Operations](https://docs.nvidia.com/image_threshold_and_compare_operations.html#image-threshold-operations)-
[Threshold Operations](https://docs.nvidia.com/image_threshold_and_compare_operations.html#group__image__threshold__operations_1image_threshold_operations) -
[Image Threshold Greater Than Operations](https://docs.nvidia.com/image_threshold_and_compare_operations.html#image-threshold-greater-than-operations) -
[Image Threshold Less Than Operations](https://docs.nvidia.com/image_threshold_and_compare_operations.html#image-threshold-less-than-operations) -
[Image Threshold Value Operations](https://docs.nvidia.com/image_threshold_and_compare_operations.html#image-threshold-value-operations) -
[Image Threshold Greater Than Value Operations](https://docs.nvidia.com/image_threshold_and_compare_operations.html#image-threshold-greater-than-value-operations) -
[Image Threshold Less Than Value Operations](https://docs.nvidia.com/image_threshold_and_compare_operations.html#image-threshold-less-than-value-operations) -
[Image Fused AbsDiff Threshold Greater Than Value Operations](https://docs.nvidia.com/image_threshold_and_compare_operations.html#image-fused-absdiff-threshold-greater-than-value-operations) -
[Image Threshold Less Than Value Greater Than Value Operations](https://docs.nvidia.com/image_threshold_and_compare_operations.html#image-threshold-less-than-value-greater-than-value-operations)

-
-
[Image Comparison Operations](https://docs.nvidia.com/image_threshold_and_compare_operations.html#image-comparison-operations)

-
[Image Memory Management Functions](https://docs.nvidia.com/image_memory_management.html)-
[Signal Arithmetic And Logical Operations](https://docs.nvidia.com/signal_arithmetic_and_logical_operations.html)-
[Signal Arithmetic Functions](https://docs.nvidia.com/signal_arithmetic_and_logical_operations.html#signal-arithmetic-functions)[Arithmetic Operations](https://docs.nvidia.com/signal_arithmetic_and_logical_operations.html#group__signal__arithmetic_1signal_arithmetic)-
[Signal AddC](https://docs.nvidia.com/signal_arithmetic_and_logical_operations.html#signal-addc) -
[Signal AddProductC](https://docs.nvidia.com/signal_arithmetic_and_logical_operations.html#signal-addproductc) -
[Signal MulC](https://docs.nvidia.com/signal_arithmetic_and_logical_operations.html#signal-mulc) -
[Signal SubC](https://docs.nvidia.com/signal_arithmetic_and_logical_operations.html#signal-subc) -
[Signal SubCRev](https://docs.nvidia.com/signal_arithmetic_and_logical_operations.html#signal-subcrev) -
[Signal DivC](https://docs.nvidia.com/signal_arithmetic_and_logical_operations.html#signal-divc) -
[Signal DivCRev](https://docs.nvidia.com/signal_arithmetic_and_logical_operations.html#signal-divcrev) -
[Signal Add](https://docs.nvidia.com/signal_arithmetic_and_logical_operations.html#signal-add) -
[Signal AddProduct](https://docs.nvidia.com/signal_arithmetic_and_logical_operations.html#signal-addproduct) -
[Signal Mul](https://docs.nvidia.com/signal_arithmetic_and_logical_operations.html#signal-mul) -
[Signal Sub](https://docs.nvidia.com/signal_arithmetic_and_logical_operations.html#signal-sub) -
[Signal Div](https://docs.nvidia.com/signal_arithmetic_and_logical_operations.html#signal-div) -
[Signal Div Round](https://docs.nvidia.com/signal_arithmetic_and_logical_operations.html#signal-div-round) -
[Signal Abs](https://docs.nvidia.com/signal_arithmetic_and_logical_operations.html#signal-abs) -
[Signal Square](https://docs.nvidia.com/signal_arithmetic_and_logical_operations.html#signal-square) -
[Signal Square Root](https://docs.nvidia.com/signal_arithmetic_and_logical_operations.html#signal-square-root) -
[Signal Cube Root](https://docs.nvidia.com/signal_arithmetic_and_logical_operations.html#signal-cube-root) -
[Signal Exp](https://docs.nvidia.com/signal_arithmetic_and_logical_operations.html#signal-exp) -
[Signal Ln](https://docs.nvidia.com/signal_arithmetic_and_logical_operations.html#signal-ln) -
[Signal 10Log10](https://docs.nvidia.com/signal_arithmetic_and_logical_operations.html#signal-10log10) -
[Signal SumLn](https://docs.nvidia.com/signal_arithmetic_and_logical_operations.html#signal-sumln) -
[Signal ArcTan](https://docs.nvidia.com/signal_arithmetic_and_logical_operations.html#signal-arctan) -
[Signal Normalize](https://docs.nvidia.com/signal_arithmetic_and_logical_operations.html#signal-normalize) -
[Signal Cauchy, CouchyD, And CouchyDD2](https://docs.nvidia.com/signal_arithmetic_and_logical_operations.html#signal-cauchy-couchyd-and-couchydd2)

-
[Logical And Shift Operations](https://docs.nvidia.com/signal_arithmetic_and_logical_operations.html#logical-and-shift-operations)

-
-
[Signal Conversion Functions](https://docs.nvidia.com/signal_conversion_functions.html) -
[Signal Filtering Functions](https://docs.nvidia.com/signal_filtering_functions.html) -
[Signal Initialization Functions](https://docs.nvidia.com/signal_initialization.html) -
[Signal Statistical Functions](https://docs.nvidia.com/signal_statistical_functions.html)-
[Signal Min Every Or Max Every](https://docs.nvidia.com/signal_statistical_functions.html#signal-min-every-or-max-every) -
[Signal Sum](https://docs.nvidia.com/signal_statistical_functions.html#signal-sum) -
[Signal Maximum](https://docs.nvidia.com/signal_statistical_functions.html#signal-maximum) -
[Signal Minimum](https://docs.nvidia.com/signal_statistical_functions.html#signal-minimum) -
[Signal Mean](https://docs.nvidia.com/signal_statistical_functions.html#signal-mean) -
[Signal StdDev](https://docs.nvidia.com/signal_statistical_functions.html#signal-stddev) -
[Signal Mean And StdDev](https://docs.nvidia.com/signal_statistical_functions.html#signal-mean-and-stddev) -
[Signal MinMax](https://docs.nvidia.com/signal_statistical_functions.html#signal-minmax) -
[Signal Norms](https://docs.nvidia.com/signal_statistical_functions.html#signal-norms) -
[Signal Dot Product](https://docs.nvidia.com/signal_statistical_functions.html#signal-dot-product) -
[Signal Count In Range](https://docs.nvidia.com/signal_statistical_functions.html#signal-count-in-range) -
[Signal Count Zero Crossings](https://docs.nvidia.com/signal_statistical_functions.html#signal-count-zero-crossings) -
[Signal Maximum Error](https://docs.nvidia.com/signal_statistical_functions.html#signal-maximum-error) -
[Signal Average Error](https://docs.nvidia.com/signal_statistical_functions.html#signal-average-error) -
[Signal Maximum Relative Error](https://docs.nvidia.com/signal_statistical_functions.html#signal-maximum-relative-error) -
[Signal Average Relative Error](https://docs.nvidia.com/signal_statistical_functions.html#signal-average-relative-error)

-
-
[Signal Memory Management Functions](https://docs.nvidia.com/signal_memory_management.html)