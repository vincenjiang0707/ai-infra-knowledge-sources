source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1_any.html
lastmod: 

# Class ov::Any[#](https://docs.openvino.ai#class-ov-any)

-
class Any
[#](https://docs.openvino.ai#_CPPv4N2ov3AnyE) This class represents an object to work with different types.

Public Functions

-
Any() = default
[#](https://docs.openvino.ai#_CPPv4N2ov3Any3AnyEv) Default constructor.


-
[Any](https://docs.openvino.ai#_CPPv4N2ov3AnyE)&operator=(const[Any](https://docs.openvino.ai#_CPPv4N2ov3AnyE)&other)[#](https://docs.openvino.ai#_CPPv4N2ov3AnyaSERK3Any) Copy assignment operator.

- Parameters:
**other**– other[Any](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_any)object- Returns:
reference to the current object



-
[Any](https://docs.openvino.ai#_CPPv4N2ov3AnyE)&operator=([Any](https://docs.openvino.ai#_CPPv4N2ov3AnyE)&&other) = default[#](https://docs.openvino.ai#_CPPv4N2ov3AnyaSERR3Any) Default move assignment operator.

- Parameters:
**other**– other[Any](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_any)object- Returns:
reference to the current object



-
~Any()
[#](https://docs.openvino.ai#_CPPv4N2ov3AnyD0Ev) Destructor preserves unloading order of implementation object and reference to library.


-
template<typename T, typename std::enable_if<!std::is_same<decay_t<
[T](https://docs.openvino.ai#_CPPv4I0_NSt9enable_ifIXaantNSt7is_sameI7decay_tI1TE3AnyE5valueEaantNSt11is_abstractI7decay_tI1TEE5valueEntNSt14is_convertibleI7decay_tI1TEN4Base3PtrEE5valueEEbE4typeEEN2ov3Any3AnyERR1T)>,[Any](https://docs.openvino.ai#_CPPv4I0_NSt9enable_ifIXaantNSt7is_sameI7decay_tI1TE3AnyE5valueEaantNSt11is_abstractI7decay_tI1TEE5valueEntNSt14is_convertibleI7decay_tI1TEN4Base3PtrEE5valueEEbE4typeEEN2ov3Any3AnyERR1T)>::value && !std::is_abstract<decay_t<[T](https://docs.openvino.ai#_CPPv4I0_NSt9enable_ifIXaantNSt7is_sameI7decay_tI1TE3AnyE5valueEaantNSt11is_abstractI7decay_tI1TEE5valueEntNSt14is_convertibleI7decay_tI1TEN4Base3PtrEE5valueEEbE4typeEEN2ov3Any3AnyERR1T)>>::value && !std::is_convertible<decay_t<[T](https://docs.openvino.ai#_CPPv4I0_NSt9enable_ifIXaantNSt7is_sameI7decay_tI1TE3AnyE5valueEaantNSt11is_abstractI7decay_tI1TEE5valueEntNSt14is_convertibleI7decay_tI1TEN4Base3PtrEE5valueEEbE4typeEEN2ov3Any3AnyERR1T)>,[Base](https://docs.openvino.ai/classov_1_1_any_1_1_base.html#_CPPv4N2ov3Any4BaseE)::Ptr>::value, bool>::type = true>

inline Any([T](https://docs.openvino.ai#_CPPv4I0_NSt9enable_ifIXaantNSt7is_sameI7decay_tI1TE3AnyE5valueEaantNSt11is_abstractI7decay_tI1TEE5valueEntNSt14is_convertibleI7decay_tI1TEN4Base3PtrEE5valueEEbE4typeEEN2ov3Any3AnyERR1T)&&value)[#](https://docs.openvino.ai#_CPPv4I0_NSt9enable_ifIXaantNSt7is_sameI7decay_tI1TE3AnyE5valueEaantNSt11is_abstractI7decay_tI1TEE5valueEntNSt14is_convertibleI7decay_tI1TEN4Base3PtrEE5valueEEbE4typeEEN2ov3Any3AnyERR1T) Constructor creates any with object.

- Template Parameters:
**T**–[Any](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_any)type- Parameters:
**value**– object


-
Any(const char *str)
[#](https://docs.openvino.ai#_CPPv4N2ov3Any3AnyEPKc) Constructor creates string any from char *.

- Parameters:
**str**– char array


-
Any(const std::nullptr_t)
[#](https://docs.openvino.ai#_CPPv4N2ov3Any3AnyEKNSt9nullptr_tE) Empty constructor.


-
const std::type_info &type_info() const
[#](https://docs.openvino.ai#_CPPv4NK2ov3Any9type_infoEv) Returns type info

- Returns:
type info



-
bool empty() const
[#](https://docs.openvino.ai#_CPPv4NK2ov3Any5emptyEv) Checks that any contains a value

- Returns:
false if any contains a value else false



-
template<class T>

inline bool is() const[#](https://docs.openvino.ai#_CPPv4I0ENK2ov3Any2isEbv) Check that stored type can be casted to specified type. If internal type supports Base.

- Template Parameters:
**T**– Type of value- Returns:
true if type of value is correct. Return false if any is empty



-
template<class T>

inline[T](https://docs.openvino.ai#_CPPv4I0EN2ov3Any2asER1Tv)&as()[#](https://docs.openvino.ai#_CPPv4I0EN2ov3Any2asER1Tv) Dynamic as to specified type

- Template Parameters:
**T**– type- Returns:
reference to caster object



-
template<class T>

inline const[T](https://docs.openvino.ai#_CPPv4I0ENK2ov3Any2asERK1Tv)&as() const[#](https://docs.openvino.ai#_CPPv4I0ENK2ov3Any2asERK1Tv) Dynamic as to specified type

- Template Parameters:
**T**– type- Returns:
const reference to caster object



-
bool operator==(const
[Any](https://docs.openvino.ai#_CPPv4N2ov3AnyE)&other) const[#](https://docs.openvino.ai#_CPPv4NK2ov3AnyeqERK3Any) The comparison operator for the

[Any](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_any).- Parameters:
**other**– object to compare- Returns:
true if objects are equal



-
bool operator==(const std::nullptr_t&) const
[#](https://docs.openvino.ai#_CPPv4NK2ov3AnyeqERKNSt9nullptr_tE) The comparison operator for the

[Any](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_any).- Parameters:
**other**– object to compare- Returns:
true if objects are equal



-
bool operator!=(const
[Any](https://docs.openvino.ai#_CPPv4N2ov3AnyE)&other) const[#](https://docs.openvino.ai#_CPPv4NK2ov3AnyneERK3Any) The comparison operator for the

[Any](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_any).- Parameters:
**other**– object to compare- Returns:
true if objects aren’t equal



-
void print(std::ostream &stream) const
[#](https://docs.openvino.ai#_CPPv4NK2ov3Any5printERNSt7ostreamE) Prints underlying object to the given output stream. Uses operator<< if it is defined, leaves stream unchanged otherwise. In case of empty any or nullptr stream immediately returns.

- Parameters:
**stream**–[Output](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_output)stream object will be printed to.


-
void read(std::istream &stream)
[#](https://docs.openvino.ai#_CPPv4N2ov3Any4readERNSt7istreamE) Read into underlying object from the given input stream. Uses operator>> if it is defined, leaves stream unchanged otherwise. In case of empty any or nullptr stream immediately returns.

- Parameters:
**stream**–[Output](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_output)stream object will be printed to.


-
void *addressof()
[#](https://docs.openvino.ai#_CPPv4N2ov3Any9addressofEv) Returns address to internal value if any is not empty and

`nullptr`

instead.- Returns:
address to internal stored value



-
const void *addressof() const
[#](https://docs.openvino.ai#_CPPv4NK2ov3Any9addressofEv) Returns address to internal value if any is not empty and

`nullptr`

instead.- Returns:
address to internal stored value



-
Any() = default