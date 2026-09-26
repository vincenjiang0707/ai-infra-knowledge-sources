source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1_coordinate_iterator.html
lastmod: 

# Class ov::CoordinateIterator[#](https://docs.openvino.ai#class-ov-coordinateiterator)

-
class CoordinateIterator
[#](https://docs.openvino.ai#_CPPv4N2ov18CoordinateIteratorE) A useful class that allows to iterate over the tensor coordinates. For example, for tensor with dimensions {2, 3} this iterator produces the following coordinates: {0,0}, {0,1}, {0,2}, {1,0}, {1,1}, {2,2}.

Public Functions

-
inline CoordinateIterator(const
[Shape](https://docs.openvino.ai/classov_1_1_shape.html#_CPPv4N2ov5ShapeE)&target_shape)[#](https://docs.openvino.ai#_CPPv4N2ov18CoordinateIterator18CoordinateIteratorERK5Shape) Coordinates iterator constructor.

- Parameters:
**target_shape**– The target shape for coordinates iteration


-
void operator++()
[#](https://docs.openvino.ai#_CPPv4N2ov18CoordinateIteratorppEv) The postfix operation increment the iterator by one.


-
[CoordinateIterator](https://docs.openvino.ai#_CPPv4N2ov18CoordinateIteratorE)operator++(int)[#](https://docs.openvino.ai#_CPPv4N2ov18CoordinateIteratorppEi) The prefix operation increment the iterator by one.


-
void operator+=(size_t n)
[#](https://docs.openvino.ai#_CPPv4N2ov18CoordinateIteratorpLE6size_t) Increments iterator n times.

- Parameters:
**n**– number of elements it should be advanced


-
const
[Coordinate](https://docs.openvino.ai/classov_1_1_coordinate.html#_CPPv4N2ov10CoordinateE)&operator*() const noexcept[#](https://docs.openvino.ai#_CPPv4NK2ov18CoordinateIteratormlEv) Iterator dereferencing operator returns reference to current pointed coordinate.


-
bool operator!=(const
[CoordinateIterator](https://docs.openvino.ai#_CPPv4N2ov18CoordinateIteratorE)&it) const noexcept[#](https://docs.openvino.ai#_CPPv4NK2ov18CoordinateIteratorneERK18CoordinateIterator) Checks for iterator inequality.

- Parameters:
**it**– second iterator to compare


-
bool operator==(const
[CoordinateIterator](https://docs.openvino.ai#_CPPv4N2ov18CoordinateIteratorE)&it) const noexcept[#](https://docs.openvino.ai#_CPPv4NK2ov18CoordinateIteratoreqERK18CoordinateIterator) Checks for iterator equality.

- Parameters:
**it**– second iterator to compare


-
size_t advance(size_t axis) noexcept
[#](https://docs.openvino.ai#_CPPv4N2ov18CoordinateIterator7advanceE6size_t) Increments iterator using specified axis of the shape n times.

- Parameters:
**axis**– index used for iteration


Public Static Functions

-
static const
[CoordinateIterator](https://docs.openvino.ai#_CPPv4N2ov18CoordinateIteratorE)&end()[#](https://docs.openvino.ai#_CPPv4N2ov18CoordinateIterator3endEv) Useful function to build the last iterator. Returns a singleton that points to the last iterator.


-
inline CoordinateIterator(const