source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1frontend_1_1_front_end_manager.html
lastmod: 

# Class ov::frontend::FrontEndManager[#](https://docs.openvino.ai#class-ov-frontend-frontendmanager)

-
class FrontEndManager
[#](https://docs.openvino.ai#_CPPv4N2ov8frontend15FrontEndManagerE) Frontend management class, loads available frontend plugins on construction Allows load of frontends for particular framework, register new and list available frontends This is a main frontend entry point for client applications.

Public Functions

-
FrontEndManager()
[#](https://docs.openvino.ai#_CPPv4N2ov8frontend15FrontEndManager15FrontEndManagerEv) Default constructor. Searches and loads of available frontends.


-
FrontEndManager(
[FrontEndManager](https://docs.openvino.ai#_CPPv4N2ov8frontend15FrontEndManager15FrontEndManagerERR15FrontEndManager)&&) noexcept[#](https://docs.openvino.ai#_CPPv4N2ov8frontend15FrontEndManager15FrontEndManagerERR15FrontEndManager) Default move constructor.


-
[FrontEndManager](https://docs.openvino.ai#_CPPv4N2ov8frontend15FrontEndManagerE)&operator=([FrontEndManager](https://docs.openvino.ai#_CPPv4N2ov8frontend15FrontEndManagerE)&&) noexcept[#](https://docs.openvino.ai#_CPPv4N2ov8frontend15FrontEndManageraSERR15FrontEndManager) Default move assignment operator.


-
~FrontEndManager()
[#](https://docs.openvino.ai#_CPPv4N2ov8frontend15FrontEndManagerD0Ev) Default destructor.


-
[FrontEnd](https://docs.openvino.ai/classov_1_1frontend_1_1_front_end.html#_CPPv4N2ov8frontend8FrontEndE)::Ptr load_by_framework(const std::string &framework)[#](https://docs.openvino.ai#_CPPv4N2ov8frontend15FrontEndManager17load_by_frameworkERKNSt6stringE) Loads frontend by name of framework and capabilities.

- Parameters:
**framework**– Framework name. Throws exception if name is not in list of available frontends- Returns:
Frontend interface for further loading of models



-
template<typename ...Types>

inline[FrontEnd](https://docs.openvino.ai/classov_1_1frontend_1_1_front_end.html#_CPPv4N2ov8frontend8FrontEndE)::Ptr load_by_model(const[Types](https://docs.openvino.ai#_CPPv4IDpEN2ov8frontend15FrontEndManager13load_by_modelEN8FrontEnd3PtrEDpRK5Types)&... vars)[#](https://docs.openvino.ai#_CPPv4IDpEN2ov8frontend15FrontEndManager13load_by_modelEN8FrontEnd3PtrEDpRK5Types) Loads frontend by model fragments described by each

[FrontEnd](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1frontend_1_1_front_end)documentation. Selects and loads appropriate frontend depending on model file extension and other file info (header)- Parameters:
**vars**–[Any](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_any)number of parameters of any type. What kind of parameters are accepted is determined by each[FrontEnd](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1frontend_1_1_front_end)individually, typically it is std::string containing path to the model file. For more information please refer to specific[FrontEnd](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1frontend_1_1_front_end)documentation.- Returns:
Frontend interface for further loading of model. Returns ‘nullptr’ if no suitable frontend is found



-
std::vector<std::string> get_available_front_ends()
[#](https://docs.openvino.ai#_CPPv4N2ov8frontend15FrontEndManager24get_available_front_endsEv) Gets list of registered frontends.

[Any](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_any)not loaded frontends will be loaded by this call.

-
void register_front_end(const std::string &name,
[FrontEndFactory](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov8frontend15FrontEndFactoryE)creator)[#](https://docs.openvino.ai#_CPPv4N2ov8frontend15FrontEndManager18register_front_endERKNSt6stringE15FrontEndFactory) Register frontend with name and factory creation method.

- Parameters:
**name**– Name of front end**creator**– Creation factory callback. Will be called when frontend is about to be created



-
void register_front_end(const std::string &name, const std::string &library_path)
[#](https://docs.openvino.ai#_CPPv4N2ov8frontend15FrontEndManager18register_front_endERKNSt6stringERKNSt6stringE) Register frontend with name and factory loaded from provided library.

- Parameters:
**name**– Name of front end**library_path**– Path (absolute or relative) or name of a frontend library. If name is provided, depending on platform, it will be wrapped with shared library suffix and prefix to identify library full name



-
FrontEndManager()