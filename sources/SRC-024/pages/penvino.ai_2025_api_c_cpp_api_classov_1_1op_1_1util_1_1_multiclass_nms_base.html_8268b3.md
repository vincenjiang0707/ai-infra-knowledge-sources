source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1op_1_1util_1_1_multiclass_nms_base.html
lastmod: 

# Class ov::op::util::MulticlassNmsBase[#](https://docs.openvino.ai#class-ov-op-util-multiclassnmsbase)

-
class MulticlassNmsBase : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[Op](https://docs.openvino.ai/classov_1_1op_1_1_op.html#_CPPv4N2ov2op2OpE)[#](https://docs.openvino.ai#_CPPv4N2ov2op4util17MulticlassNmsBaseE) Base class for operations MulticlassNMS

[v8](https://docs.openvino.ai/group__ov__transformation__common__api.html#namespaceov_1_1op_1_1v8)and MulticlassNMS[v9](https://docs.openvino.ai/group__ov__transformation__common__api.html#namespaceov_1_1op_1_1v9).Subclassed by

[ov::op::v8::MulticlassNms](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v8_1_1_multiclass_nms),[ov::op::v9::MulticlassNms](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v9_1_1_multiclass_nms)Public Functions

-
MulticlassNmsBase() = default
[#](https://docs.openvino.ai#_CPPv4N2ov2op4util17MulticlassNmsBase17MulticlassNmsBaseEv) Constructs a conversion operation.


-
MulticlassNmsBase(const OutputVector &arguments, const
[Attributes](https://docs.openvino.ai/structov_1_1op_1_1util_1_1_multiclass_nms_base_1_1_attributes.html#_CPPv4N2ov2op4util17MulticlassNmsBase10AttributesE)&attrs)[#](https://docs.openvino.ai#_CPPv4N2ov2op4util17MulticlassNmsBase17MulticlassNmsBaseERK12OutputVectorRK10Attributes) Constructs a

[MulticlassNmsBase](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1util_1_1_multiclass_nms_base)operation.- Parameters:
**arguments**–[Node](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_node)list producing the box coordinates, scores, etc.**attrs**–[Attributes](https://docs.openvino.ai/group__ov__transformation__common__api.html#structov_1_1op_1_1util_1_1_multiclass_nms_base_1_1_attributes)of the operation



-
inline const
[Attributes](https://docs.openvino.ai/structov_1_1op_1_1util_1_1_multiclass_nms_base_1_1_attributes.html#_CPPv4N2ov2op4util17MulticlassNmsBase10AttributesE)&get_attrs() const[#](https://docs.openvino.ai#_CPPv4NK2ov2op4util17MulticlassNmsBase9get_attrsEv) Returns attributes of the operation

[MulticlassNmsBase](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1util_1_1_multiclass_nms_base).

-
struct Attributes
[#](https://docs.openvino.ai#_CPPv4N2ov2op4util17MulticlassNmsBase10AttributesE) Structure that specifies attributes of the operation.


-
MulticlassNmsBase() = default