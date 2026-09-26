source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1frontend_1_1_front_end.html
lastmod: 

# Class ov::frontend::FrontEnd[#](https://docs.openvino.ai#class-ov-frontend-frontend)

-
class FrontEnd
[#](https://docs.openvino.ai#_CPPv4N2ov8frontend8FrontEndE) An interface for identifying a frontend for a particular framework. Provides an ability to load and convert of input model.

Unnamed Group

-
void add_extension(const std::string &library_path)
[#](https://docs.openvino.ai#_CPPv4N2ov8frontend8FrontEnd13add_extensionERKNSt6stringE) Registers extension.

- Parameters:
**library_path**– path to library with[ov::Extension](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_extension)


Public Functions

-
FrontEnd()
[#](https://docs.openvino.ai#_CPPv4N2ov8frontend8FrontEnd8FrontEndEv) Default constructor.


-
template<typename ...Types>

inline bool supported(const[Types](https://docs.openvino.ai#_CPPv4IDpENK2ov8frontend8FrontEnd9supportedEbDpRK5Types)&... vars) const[#](https://docs.openvino.ai#_CPPv4IDpENK2ov8frontend8FrontEnd9supportedEbDpRK5Types) Validates if

[FrontEnd](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1frontend_1_1_front_end)can recognize model with parameters specified. Same parameters should be used to load model.- Parameters:
**vars**–[Any](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_any)number of parameters of any type. What kind of parameters are accepted is determined by each[FrontEnd](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1frontend_1_1_front_end)individually, typically it is std::string containing path to the model file. For more information please refer to specific[FrontEnd](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1frontend_1_1_front_end)documentation.- Returns:
true if model recognized, false - otherwise.



-
template<typename ...Types>

inline[InputModel](https://docs.openvino.ai/classov_1_1frontend_1_1_input_model.html#_CPPv4N2ov8frontend10InputModelE)::Ptr load(const[Types](https://docs.openvino.ai#_CPPv4IDpENK2ov8frontend8FrontEnd4loadEN10InputModel3PtrEDpRK5Types)&... vars) const[#](https://docs.openvino.ai#_CPPv4IDpENK2ov8frontend8FrontEnd4loadEN10InputModel3PtrEDpRK5Types) Loads an input model by any specified arguments. Each

[FrontEnd](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1frontend_1_1_front_end)separately defines what arguments it can accept.- Parameters:
**vars**–[Any](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_any)number of parameters of any type. What kind of parameters are accepted is determined by each[FrontEnd](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1frontend_1_1_front_end)individually, typically it is std::string containing path to the model file. For more information please refer to specific[FrontEnd](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1frontend_1_1_front_end)documentation.- Returns:
Loaded input model.



-
virtual std::shared_ptr<
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[Model](https://docs.openvino.ai/classov_1_1_model.html#_CPPv4N2ov5ModelE)> convert(const[InputModel](https://docs.openvino.ai/classov_1_1frontend_1_1_input_model.html#_CPPv4N2ov8frontend10InputModelE)::Ptr &model) const[#](https://docs.openvino.ai#_CPPv4NK2ov8frontend8FrontEnd7convertERKN10InputModel3PtrE) Completely convert and normalize entire

[Model](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_model), throws if it is not possible.

Completely convert the remaining, not converted part of a

[Model](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_model).- Parameters:
**partiallyConverted**– partially converted OV[Model](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_model)


-
virtual std::shared_ptr<
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[Model](https://docs.openvino.ai/classov_1_1_model.html#_CPPv4N2ov5ModelE)> convert_partially(const[InputModel](https://docs.openvino.ai/classov_1_1frontend_1_1_input_model.html#_CPPv4N2ov8frontend10InputModelE)::Ptr &model) const[#](https://docs.openvino.ai#_CPPv4NK2ov8frontend8FrontEnd17convert_partiallyERKN10InputModel3PtrE) Convert only those parts of the model that can be converted leaving others as-is wrapped by FrameworkNode. Converted parts are normalized by additional transformations like it is done in convert method. If part of the graph cannot be converted, it is not guaranteed that the converted regions are completely normalized. Normalize should be called for each completely converted parts individually in this case.


-
virtual std::shared_ptr<
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[Model](https://docs.openvino.ai/classov_1_1_model.html#_CPPv4N2ov5ModelE)> decode(const[InputModel](https://docs.openvino.ai/classov_1_1frontend_1_1_input_model.html#_CPPv4N2ov8frontend10InputModelE)::Ptr &model) const[#](https://docs.openvino.ai#_CPPv4NK2ov8frontend8FrontEnd6decodeERKN10InputModel3PtrE) Convert operations with one-to-one mapping with decoding nodes. Each decoding node is an OV node representing a single FW operation node with all attributes represented in FW-independent way.


Runs normalization passes on

[Model](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_model)that was loaded with partial conversion.- Parameters:
**Model**– partially converted OV[Model](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_model)


-
virtual std::string get_name() const
[#](https://docs.openvino.ai#_CPPv4NK2ov8frontend8FrontEnd8get_nameEv) Gets name of this

[FrontEnd](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1frontend_1_1_front_end). Can be used by clients if frontend is selected automatically by[FrontEndManager::load_by_model](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1frontend_1_1_front_end_manager_1addb6ad60a29ed43c2e7fd2b8c46cab72).- Returns:
Current frontend name. Empty string if not implemented



Register base extension in the

[FrontEnd](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1frontend_1_1_front_end).- Parameters:
**extension**– base extension


Register base extensions in the

[FrontEnd](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1frontend_1_1_front_end).- Parameters:
**extensions**– vector of extensions


-
void add_extension(const std::string &library_path)