source: https://docs.openvino.ai/2025/api/c_cpp_api/group__ov__cpp__api.html
lastmod: 

# Group OpenVINO Runtime C++ API[#](https://docs.openvino.ai#group-openvino-runtime-c-api)

[Basics](https://docs.openvino.ai/group__ov__model__cpp__api.html)`shape_size()`

`shape_size()`

`ov::Dimension`

`Dimension()`

`Dimension()`

`Dimension()`

`Dimension()`

`is_static()`

`is_dynamic()`

`get_length()`

`get_interval()`

`same_scheme()`

`compatible()`

`relaxes()`

`refines()`

`operator+()`

`operator-()`

`operator/()`

`operator/=()`

`operator*()`

`operator+=()`

`operator*=()`

`operator&()`

`operator&=()`

`to_string()`

`has_symbol()`

`get_symbol()`

`set_symbol()`

`merge()`

`broadcast_merge()`

`dynamic()`

`swap`


`ov::Extension`

`ov::Model`

`Model()`

`Model()`

`get_output_size()`

`get_output_op()`

`clone()`

`outputs()`

`inputs()`

`get_output_element_type()`

`get_output_shape()`

`get_output_partial_shape()`

`get_result()`

`get_name()`

`set_friendly_name()`

`get_friendly_name()`

`get_graph_size()`

`is_dynamic()`

`replace_parameter()`

`get_parameters()`

`get_results()`

`get_parameter_index()`

`get_result_index()`

`get_result_index()`

`evaluate()`

`evaluate()`

`get_sinks()`

`add_sinks()`

`remove_sink()`

`add_results()`

`remove_result()`

`add_parameters()`

`remove_parameter()`

`add_variables()`

`remove_variable()`

`get_variables()`

`get_variable_by_id()`

`get_rt_info()`

`get_rt_info()`

`get_rt_info()`

`get_rt_info()`

`has_rt_info()`

`has_rt_info()`

`set_rt_info()`

`set_rt_info()`


`ov::Node`

`validate_and_infer_types()`

`get_autob()`

`has_evaluate()`

`evaluate()`

`evaluate()`

`decompose_op()`

`get_type_info()`

`set_arguments()`

`set_arguments()`

`set_argument()`

`set_output_size()`

`description()`

`get_name()`

`set_friendly_name()`

`get_friendly_name()`

`write_description()`

`get_control_dependencies()`

`get_control_dependents()`

`add_control_dependency()`

`remove_control_dependency()`

`clear_control_dependencies()`

`clear_control_dependents()`

`add_node_control_dependencies()`

`add_node_control_dependents()`

`transfer_control_dependents()`

`get_output_size()`

`get_output_element_type()`

`get_element_type()`

`get_output_shape()`

`get_output_partial_shape()`

`get_default_output()`

`get_default_output_index()`

`no_default_index()`

`get_shape()`

`get_output_tensor()`

`get_input_size()`

`get_input_element_type()`

`get_input_shape()`

`get_input_partial_shape()`

`has_same_type()`

`get_users()`

`operator<()`

`inputs()`

`inputs()`

`input_values()`

`outputs()`

`outputs()`

`input()`

`input()`

`output()`

`output()`


`ov::Input< Node >`

`ov::Input< const Node >`

`ov::Output< Node >`

`ov::Output< const Node >`

`ov::PartialShape`

`PartialShape()`

`PartialShape()`

`PartialShape()`

`PartialShape()`

`PartialShape()`

`PartialShape()`

`is_static()`

`is_dynamic()`

`rank()`

`compatible()`

`same_scheme()`

`relaxes()`

`refines()`

`merge_rank()`

`to_shape()`

`all_non_negative()`

`operator[]()`

`operator[]()`

`operator std::vector< Dimension >()`

`get_max_shape()`

`get_min_shape()`

`get_shape()`

`begin()`

`begin()`

`end()`

`end()`

`rbegin()`

`rbegin()`

`rend()`

`rend()`

`cbegin()`

`cend()`

`crbegin()`

`crend()`

`resize()`

`size()`

`insert()`

`insert()`

`insert()`

`reserve()`

`push_back()`

`emplace_back()`

`to_string()`

`dynamic()`

`merge_into()`

`broadcast_merge_into()`


`ov::preprocess::PrePostProcessor`

`ov::Shape`

`ov::Symbol`

`ov::DiscreteTypeInfo`


[Operations](https://docs.openvino.ai/group__ov__ops__cpp__api.html)`ov::op::internal::AUGRUCell`

`ov::op::internal::AUGRUSequence`

`ov::op::v0::Abs`

`ov::op::v0::Acos`

`ov::op::v3::Acosh`

`ov::op::v8::AdaptiveAvgPool`

`ov::op::v8::AdaptiveMaxPool`

`ov::op::v1::Add`

`ov::op::v0::Asin`

`ov::op::v3::Assign`

`ov::op::v6::Assign`

`ov::op::v0::Atan`

`ov::op::v3::Atanh`

`ov::op::v1::AvgPool`

`ov::op::v14::AvgPool`

`ov::op::v16::AvgPool`

`ov::op::v0::BatchNormInference`

`ov::op::v5::BatchNormInference`

`ov::op::v1::BatchToSpace`

`ov::op::v1::BinaryConvolution`

`ov::op::v13::BitwiseAnd`

`ov::op::v15::BitwiseLeftShift`

`ov::op::v13::BitwiseNot`

`ov::op::v13::BitwiseOr`

`ov::op::v15::BitwiseRightShift`

`ov::op::v13::BitwiseXor`

`ov::op::v3::Broadcast`

`ov::op::v1::Broadcast`

`ov::op::v3::Bucketize`

`ov::op::v0::Ceiling`

`ov::op::v0::Clamp`

`ov::op::v15::Col2Im`

`ov::op::v0::Concat`

`ov::op::v0::Constant`

`Constant()`

`Constant()`

`Constant()`

`Constant()`

`Constant()`

`Constant()`

`Constant()`

`validate_and_infer_types()`

`evaluate()`

`has_evaluate()`

`get_shape_val()`

`get_strides_val()`

`get_coordinate_val()`

`get_coordinate_diff_val()`

`get_axis_vector_val()`

`get_axis_set_val()`

`get_byte_size()`

`get_value_strings()`

`get_vector()`

`cast_vector()`

`get_tensor_view()`

`get_strides()`

`create()`

`create()`

`create()`


`ov::op::v0::Convert`

`ov::op::v1::ConvertLike`

`ov::op::v14::ConvertPromoteTypes`

`ov::op::v1::Convolution`

`ov::op::v1::ConvolutionBackpropData`

`ov::op::v0::Cos`

`ov::op::v0::Cosh`

`ov::op::v0::CTCGreedyDecoder`

`ov::op::v6::CTCGreedyDecoderSeqLen`

`ov::op::v4::CTCLoss`

`ov::op::v0::CumSum`

`ov::op::v1::DeformableConvolution`

`ov::op::v8::DeformableConvolution`

`ov::op::v1::DeformablePSROIPooling`

`ov::op::v0::DepthToSpace`

`ov::op::v7::DFT`

`ov::op::v1::Divide`

`ov::op::v7::Einsum`

`ov::op::v0::Elu`

`ov::op::v3::EmbeddingSegmentsSum`

`ov::op::v15::EmbeddingBagOffsets`

`ov::op::v3::EmbeddingBagOffsetsSum`

`ov::op::v15::EmbeddingBagPacked`

`ov::op::v3::EmbeddingBagPackedSum`

`ov::op::v1::Equal`

`ov::op::v0::Erf`

`ov::op::v0::Exp`

`ov::op::v6::ExperimentalDetectronDetectionOutput`

`ov::op::v6::ExperimentalDetectronGenerateProposalsSingleImage`

`ov::op::v6::ExperimentalDetectronPriorGridGenerator`

`ov::op::v6::ExperimentalDetectronROIFeatureExtractor`

`ov::op::v6::ExperimentalDetectronTopKROIs`

`ov::op::v3::ExtractImagePatches`

`ov::op::v9::Eye`

`ov::op::v13::FakeConvert`

`ov::op::v0::FakeQuantize`

`ov::op::v0::Floor`

`ov::op::v1::FloorMod`

`ov::op::v1::Gather`

`ov::op::v7::Gather`

`ov::op::v8::Gather`

`ov::op::v6::GatherElements`

`ov::op::v5::GatherND`

`ov::op::v8::GatherND`

`ov::op::v1::GatherTree`

`ov::op::v0::Gelu`

`ov::op::v7::Gelu`

`ov::op::v1::Greater`

`ov::op::v1::GreaterEqual`

`ov::op::v9::GridSample`

`ov::op::v12::GroupNormalization`

`ov::op::v3::GRUCell`

`ov::op::v5::GRUSequence`

`ov::op::v0::HardSigmoid`

`ov::op::v5::HSigmoid`

`ov::op::v4::HSwish`

`ov::op::v8::I420toBGR`

`ov::op::v8::I420toRGB`

`ov::op::v16::Identity`

`ov::op::v7::IDFT`

`ov::op::v8::If`

`ov::op::v0::Interpolate`

`ov::op::v4::Interpolate`

`ov::op::v11::Interpolate`

`ov::op::v14::Inverse`

`ov::op::v10::IsFinite`

`ov::op::v10::IsInf`

`ov::op::v10::IsNaN`

`ov::op::v16::ISTFT`

`ov::op::v1::Less`

`ov::op::v1::LessEqual`

`ov::op::v0::Log`

`ov::op::v5::LogSoftmax`

`ov::op::v1::LogicalAnd`

`ov::op::v1::LogicalNot`

`ov::op::v1::LogicalOr`

`ov::op::v1::LogicalXor`

`ov::op::v5::Loop`

`ov::op::v0::LRN`

`ov::op::v0::LSTMCell`

`ov::op::v4::LSTMCell`

`ov::op::v5::LSTMSequence`

`ov::op::v0::MatMul`

`ov::op::v8::MatrixNms`

`ov::op::v1::MaxPool`

`ov::op::v8::MaxPool`

`ov::op::v14::MaxPool`

`ov::op::v1::Maximum`

`ov::op::v1::Minimum`

`ov::op::v4::Mish`

`ov::op::v1::Mod`

`ov::op::v13::Multinomial`

`ov::op::v1::Multiply`

`ov::op::v0::MVN`

`ov::op::v6::MVN`

`ov::op::v0::Negative`

`ov::op::v1::NonMaxSuppression`

`ov::op::v3::NonMaxSuppression`

`ov::op::v4::NonMaxSuppression`

`ov::op::v5::NonMaxSuppression`

`ov::op::v3::NonZero`

`ov::op::v0::NormalizeL2`

`ov::op::v1::NotEqual`

`ov::op::v8::NV12toBGR`

`ov::op::v8::NV12toRGB`

`ov::op::v1::OneHot`

`ov::op::v16::OneHot`

`ov::op::Op`

`ov::op::v1::Pad`

`ov::op::v12::Pad`

`ov::op::v0::Parameter`

`ov::op::v1::Power`

`ov::op::v0::PRelu`

`ov::op::v0::PriorBox`

`ov::op::v8::PriorBox`

`ov::op::v0::PriorBoxClustered`

`ov::op::v0::Proposal`

`ov::op::v4::Proposal`

`ov::op::v0::PSROIPooling`

`ov::op::v8::RandomUniform`

`ov::op::v4::Range`

`ov::op::v0::Range`

`ov::op::v3::ReadValue`

`ov::op::v6::ReadValue`

`ov::op::v4::ReduceL1`

`ov::op::v4::ReduceL2`

`ov::op::v1::ReduceLogicalAnd`

`ov::op::v1::ReduceLogicalOr`

`ov::op::v1::ReduceMax`

`ov::op::v1::ReduceMean`

`ov::op::v1::ReduceMin`

`ov::op::v1::ReduceProd`

`ov::op::v1::ReduceSum`

`ov::op::v0::RegionYolo`

`ov::op::v0::Relu`

`ov::op::v0::ReorgYolo`

`ov::op::v1::Reshape`

`ov::op::v0::Result`

`ov::op::v1::Reverse`

`ov::op::v0::ReverseSequence`

`ov::op::v0::RNNCell`

`ov::op::v5::RNNSequence`

`ov::op::v3::ROIAlign`

`ov::op::v15::ROIAlignRotated`

`ov::op::v0::ROIPooling`

`ov::op::v7::Roll`

`ov::op::v5::Round`

`ov::op::v13::ScaledDotProductAttention`

`ov::op::v3::ScatterElementsUpdate`

`ov::op::v3::ScatterNDUpdate`

`ov::op::v15::ScatterNDUpdate`

`ov::op::v3::ScatterUpdate`

`ov::op::v15::SearchSorted`

`ov::op::v16::SegmentMax`

`ov::op::v1::Select`

`ov::op::v0::Selu`

`ov::op::v3::ShapeOf`

`ov::op::v0::ShapeOf`

`ov::op::v0::ShuffleChannels`

`ov::op::v0::Sigmoid`

`ov::op::v0::Sign`

`ov::op::v0::Sin`

`ov::op::v0::Sinh`

`ov::op::Sink`

`ov::op::v8::Slice`

`ov::op::v15::SliceScatter`

`ov::op::v1::Softmax`

`ov::op::v8::Softmax`

`ov::op::v4::SoftPlus`

`ov::op::v1::SpaceToBatch`

`ov::op::v0::SpaceToDepth`

`ov::op::v16::SparseFillEmptyRows`

`ov::op::v1::Split`

`ov::op::v0::Sqrt`

`ov::op::v0::SquaredDifference`

`ov::op::v0::Squeeze`

`ov::op::v15::Squeeze`

`ov::op::v15::STFT`

`ov::op::v1::StridedSlice`

`ov::op::v15::StringTensorPack`

`ov::op::v15::StringTensorUnpack`

`ov::op::v1::Subtract`

`ov::op::v4::Swish`

`ov::op::v0::Tan`

`ov::op::v0::Tanh`

`ov::op::v0::TensorIterator`

`ov::op::v0::Tile`

`ov::op::v1::TopK`

`ov::op::v3::TopK`

`ov::op::v11::TopK`

`ov::op::v1::Transpose`

`ov::op::v10::Unique`

`ov::op::v0::Unsqueeze`

`ov::op::util::SqueezeBase`

`ov::op::v1::VariadicSplit`

`ov::op::v0::Xor`


[Operation sets](https://docs.openvino.ai/group__ov__opset__cpp__api.html)[Transformation passes](https://docs.openvino.ai/group__ov__pass__cpp__api.html)`ov::pass::ConstantFolding`

`ov::pass::ConvertFP32ToFP16`

`ov::pass::GraphRewrite`

`ov::pass::LowLatency2`

`ov::pass::MakeStateful`

`ov::pass::Manager`

`ov::pass::MatcherPass`

`ov::pass::PassBase`

`ov::pass::ModelPass`

`ov::pass::PassConfig`

`ov::pass::SDPAToPagedAttention`

`ov::pass::SDPAToVLSDPA`

`ov::pass::Serialize`

`ov::pass::StreamSerialize`

`ov::pass::StatefulToStateless`

`ov::pass::Validate`

`ov::pass::VisualizeTree`


[Inference](https://docs.openvino.ai/group__ov__runtime__cpp__api.html)`SupportedOpsMap`

`ov::Allocator`

`ov::Tensor`

`data()`

`data()`

`data()`

`Tensor()`

`Tensor()`

`Tensor()`

`operator=()`

`Tensor()`

`operator=()`

`~Tensor()`

`Tensor()`

`Tensor()`

`Tensor()`

`Tensor()`

`Tensor()`

`Tensor()`

`Tensor()`

`set_shape()`

`get_element_type()`

`get_shape()`

`copy_to()`

`is_continuous()`

`get_size()`

`get_byte_size()`

`get_strides()`

`operator!()`

`operator bool()`

`is()`

`as()`

`type_check()`


`ov::CompiledModel`

`ov::Core`

`read_model()`

`read_model()`

`compile_model()`

`compile_model()`

`compile_model()`

`compile_model()`

`add_extension()`

`Core()`

`get_versions()`

`read_model()`

`compile_model()`

`compile_model()`

`compile_model()`

`compile_model()`

`compile_model()`

`compile_model()`

`compile_model()`

`compile_model()`

`add_extension()`

`add_extension()`

`add_extension()`

`add_extension()`

`add_extension()`

`add_extension()`

`import_model()`

`import_model()`

`import_model()`

`import_model()`

`import_model()`

`import_model()`

`import_model()`

`import_model()`

`query_model()`

`query_model()`

`set_property()`

`set_property()`

`set_property()`

`set_property()`

`get_property()`

`get_property()`

`get_property()`

`get_property()`

`get_property()`

`get_property()`

`get_available_devices()`

`register_plugin()`

`unload_plugin()`

`register_plugins()`

`create_context()`

`create_context()`

`get_default_context()`


`ov::Cancelled`

`ov::Busy`

`ov::InferRequest`

`InferRequest()`

`InferRequest()`

`operator=()`

`InferRequest()`

`operator=()`

`~InferRequest()`

`set_tensor()`

`set_tensor()`

`set_tensor()`

`set_tensors()`

`set_tensors()`

`set_input_tensor()`

`set_input_tensor()`

`set_input_tensors()`

`set_input_tensors()`

`set_output_tensor()`

`set_output_tensor()`

`get_tensor()`

`get_tensor()`

`get_tensor()`

`get_input_tensor()`

`get_input_tensor()`

`get_output_tensor()`

`get_output_tensor()`

`infer()`

`cancel()`

`get_profiling_info()`

`start_async()`

`wait()`

`wait_for()`

`set_callback()`

`query_state()`

`reset_state()`

`get_compiled_model()`

`operator!()`

`operator bool()`

`operator!=()`

`operator==()`


`ov::RemoteContext`

`ov::RemoteTensor`

`ov::VariableState`

`ov::ProfilingInfo`