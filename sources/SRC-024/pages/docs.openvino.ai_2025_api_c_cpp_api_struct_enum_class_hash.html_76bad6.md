source: https://docs.openvino.ai/2025/api/c_cpp_api/struct_enum_class_hash.html
lastmod: 

# Struct EnumClassHash[#](https://docs.openvino.ai#struct-enumclasshash)

-
struct EnumClassHash
ConvertPrecision transformation convert precision for entire

[ov::Model](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_model)List of supported precision conversion: FROM -> TO u8 -> i32 u16 -> i32 u32 -> i32 u64 -> i32 i64 -> i32 f16 -> f32 bool -> u8 bool -> i32.For all operations from opset1-opset4 this conversions can be applied without adding Conversion operations. That is possible because all operations that produces “FROM” type can produce “TO” type. And for this operations we have created special fuse_type_into_<type> function (can be found in cpp file) that performs type fusion into operation. m_additional_type_to_fuse_map allows to rewrite existing type convertors.

List of operations that are supported by this transformations for i64 -> i32 conversion: opset4::Parameter opset4::Convert opset4::ShapeOf opset4::Range opset3::NonMaxSuppression opset4::NonMaxSuppression opset4::TopK opset4::NonZero opset4::Bucketize

List of operations that are supported by this transformations for bool -> u8 conversion: LogicalAnd LogicalNot LogicalOr LogicalXor ReduceLogicalAnd ReduceLogicalOr Equal NotEqual Greater GreaterEqual Less LessEqual