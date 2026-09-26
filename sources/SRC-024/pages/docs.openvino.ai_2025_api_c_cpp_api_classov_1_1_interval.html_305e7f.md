source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1_interval.html
lastmod: 

# Class ov::Interval[#](https://docs.openvino.ai#class-ov-interval)

-
class Interval
[#](https://docs.openvino.ai#_CPPv4N2ov8IntervalE) [Interval](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_interval)arithmetic.An interval is the set of integers from m_min_val through m_max_val. The value s_max acts like infinity. The addition, subtraction, or multiplication of intervals is the smallest interval containing the sums, differences, or products of elements of the two intervals. An empty interval is canonicalized to [s_max, s_max].

Public Functions

-
Interval(value_type min_val, value_type max_val)
[#](https://docs.openvino.ai#_CPPv4N2ov8Interval8IntervalE10value_type10value_type) Closed interval {x|min_val <= x <= max_val}.


-
Interval(value_type val)
[#](https://docs.openvino.ai#_CPPv4N2ov8Interval8IntervalE10value_type) Single-valued interval; just contains val.


-
inline size_type size() const
[#](https://docs.openvino.ai#_CPPv4NK2ov8Interval4sizeEv) The number of elements in the interval. Zero if max < min.


-
inline bool empty() const
[#](https://docs.openvino.ai#_CPPv4NK2ov8Interval5emptyEv) Returns true if the interval has no elements.


-
inline value_type get_min_val() const
[#](https://docs.openvino.ai#_CPPv4NK2ov8Interval11get_min_valEv) the inclusive lower bound of the interval


-
inline void set_min_val(value_type val)
[#](https://docs.openvino.ai#_CPPv4N2ov8Interval11set_min_valE10value_type) Set the inclusive lower bound of the interval.


-
inline value_type get_max_val() const
[#](https://docs.openvino.ai#_CPPv4NK2ov8Interval11get_max_valEv) the inclusive upper bound of the interval


-
inline void set_max_val(value_type val)
[#](https://docs.openvino.ai#_CPPv4N2ov8Interval11set_max_valE10value_type) Set the inclusive upper bound of the interval.


-
inline bool has_upper_bound() const
[#](https://docs.openvino.ai#_CPPv4NK2ov8Interval15has_upper_boundEv) True if the upper bound is finite.


-
[Interval](https://docs.openvino.ai#_CPPv4N2ov8IntervalE)operator+(const[Interval](https://docs.openvino.ai#_CPPv4N2ov8IntervalE)&interval) const[#](https://docs.openvino.ai#_CPPv4NK2ov8IntervalplERK8Interval) The interval whose elements are a sum of an element from each interval.


-
[Interval](https://docs.openvino.ai#_CPPv4N2ov8IntervalE)&operator+=(const[Interval](https://docs.openvino.ai#_CPPv4N2ov8IntervalE)&interval)[#](https://docs.openvino.ai#_CPPv4N2ov8IntervalpLERK8Interval) Extend this interval to sums of elements in this interval and interval.


-
[Interval](https://docs.openvino.ai#_CPPv4N2ov8IntervalE)operator-(const[Interval](https://docs.openvino.ai#_CPPv4N2ov8IntervalE)&interval) const[#](https://docs.openvino.ai#_CPPv4NK2ov8IntervalmiERK8Interval) The interval whose elements are a difference of an element from each interval.


-
[Interval](https://docs.openvino.ai#_CPPv4N2ov8IntervalE)&operator-=(const[Interval](https://docs.openvino.ai#_CPPv4N2ov8IntervalE)&interval)[#](https://docs.openvino.ai#_CPPv4N2ov8IntervalmIERK8Interval) Extend this interval to differences of elements in this interval and interval.


-
[Interval](https://docs.openvino.ai#_CPPv4N2ov8IntervalE)operator*(const[Interval](https://docs.openvino.ai#_CPPv4N2ov8IntervalE)&interval) const[#](https://docs.openvino.ai#_CPPv4NK2ov8IntervalmlERK8Interval) The smallest interval whose elements are a product of an element from each interval.


-
[Interval](https://docs.openvino.ai#_CPPv4N2ov8IntervalE)&operator*=(const[Interval](https://docs.openvino.ai#_CPPv4N2ov8IntervalE)&interval)[#](https://docs.openvino.ai#_CPPv4N2ov8IntervalmLERK8Interval) Extend this interval to products of elements in this interval and interval.


-
[Interval](https://docs.openvino.ai#_CPPv4N2ov8IntervalE)operator&(const[Interval](https://docs.openvino.ai#_CPPv4N2ov8IntervalE)&interval) const[#](https://docs.openvino.ai#_CPPv4NK2ov8IntervalanERK8Interval) The interval that is the intersection of this interval and interval.


-
[Interval](https://docs.openvino.ai#_CPPv4N2ov8IntervalE)&operator&=(const[Interval](https://docs.openvino.ai#_CPPv4N2ov8IntervalE)&interval)[#](https://docs.openvino.ai#_CPPv4N2ov8IntervalaNERK8Interval) Change this interval to only include elements also in interval.


-
inline bool contains(value_type value) const
[#](https://docs.openvino.ai#_CPPv4NK2ov8Interval8containsE10value_type) True if this interval includes value.


Public Static Attributes

-
static constexpr value_type s_max = {std::numeric_limits<value_type>::max()}
[#](https://docs.openvino.ai#_CPPv4N2ov8Interval5s_maxE) The value used for no upper bound.


-
Interval(value_type min_val, value_type max_val)