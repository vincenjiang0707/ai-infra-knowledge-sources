source: https://docs.openvino.ai/2025/api/ie_python_api/_autosummary/openvino.experimental.set_tensor_type.html
lastmod: 

# openvino.experimental.set_tensor_type[#](https://docs.openvino.ai#openvino-experimental-set-tensor-type)

-
openvino.experimental.set_tensor_type(
*tensor: openvino._pyopenvino.DescriptorTensor*,*element_type:*,[openvino._pyopenvino.Type](https://docs.openvino.ai/openvino.Type.html#openvino.Type)*partial_shape:*) None[openvino._pyopenvino.PartialShape](https://docs.openvino.ai/openvino.PartialShape.html#openvino.PartialShape)[#](https://docs.openvino.ai#openvino.experimental.set_tensor_type) Changes element type and partial shape of a tensor descriptor in the OV model graph.

- Parameters:
**tensor**() – The tensor descriptor whose element type is to be set.*openvino.Tensor***element_type**() – A new element type of the tensor descriptor.*openvino.Type***partial_shape**() – A new partial shape of the tensor desriptor.*openvino.PartialShape*