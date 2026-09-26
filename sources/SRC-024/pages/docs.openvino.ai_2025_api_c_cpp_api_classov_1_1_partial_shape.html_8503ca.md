source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1_partial_shape.html
lastmod: 

# Class ov::PartialShape[#](https://docs.openvino.ai#class-ov-partialshape)

-
class PartialShape
[#](https://docs.openvino.ai#_CPPv4N2ov12PartialShapeE) Class representing a shape that may be partially or totally dynamic.

A

[PartialShape](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_partial_shape)may have:Dynamic rank. (Informal notation:

`?`

)Static rank, but dynamic dimensions on some or all axes. (Informal notation examples:

`{1,2,?,4}`

,`{?,?,?}`

)Static rank, and static dimensions on all axes. (Informal notation examples:

`{1,2,3,4}`

,`{6}`

,`{}`

)

Public Functions

-
PartialShape(std::initializer_list<
[Dimension](https://docs.openvino.ai/classov_1_1_dimension.html#_CPPv4N2ov9DimensionE)> init)[#](https://docs.openvino.ai#_CPPv4N2ov12PartialShape12PartialShapeENSt16initializer_listI9DimensionEE) Constructs a shape with static rank from an initializer list of

[Dimension](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_dimension).Examples:

PartialShape s{2,3,4}; // rank=3, all dimensions static PartialShape s{}; // rank=0 PartialShape s{2,Dimension::dynamic(),3}; // rank=3, dimension 1 dynamic

- Parameters:
**init**– The[Dimension](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_dimension)values for the constructed shape.


-
PartialShape(std::vector<
[Dimension](https://docs.openvino.ai/classov_1_1_dimension.html#_CPPv4N2ov9DimensionE)> dimensions)[#](https://docs.openvino.ai#_CPPv4N2ov12PartialShape12PartialShapeENSt6vectorI9DimensionEE) Constructs a

[PartialShape](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_partial_shape)with static rank from a vector of[Dimension](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_dimension).- Parameters:
**dimensions**– The[Dimension](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_dimension)values for the constructed shape.


-
PartialShape(const std::vector<
[Dimension](https://docs.openvino.ai/classov_1_1_dimension.html#_CPPv4N2ov9DimensionE)::value_type> &dimensions)[#](https://docs.openvino.ai#_CPPv4N2ov12PartialShape12PartialShapeERKNSt6vectorIN9Dimension10value_typeEEE) Constructs a

[PartialShape](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_partial_shape)with static rank from a vector of dimensions values.- Parameters:
**dimensions**– The[Dimension](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_dimension)values for the constructed shape.


-
PartialShape()
[#](https://docs.openvino.ai#_CPPv4N2ov12PartialShape12PartialShapeEv) Constructs a static

[PartialShape](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_partial_shape)with zero rank (the shape of a scalar).

-
PartialShape(const
[Shape](https://docs.openvino.ai/classov_1_1_shape.html#_CPPv4N2ov5ShapeE)&shape)[#](https://docs.openvino.ai#_CPPv4N2ov12PartialShape12PartialShapeERK5Shape) Constructs a static

[PartialShape](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_partial_shape)from a[PartialShape](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_partial_shape).- Parameters:
**shape**– The[PartialShape](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_partial_shape)to convert into[PartialShape](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_partial_shape).


-
PartialShape(const std::string &shape)
[#](https://docs.openvino.ai#_CPPv4N2ov12PartialShape12PartialShapeERKNSt6stringE) Constructs a static

[PartialShape](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_partial_shape)from a string.- Parameters:
**shape**– The string to parse into[PartialShape](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_partial_shape).


-
bool is_static() const
[#](https://docs.openvino.ai#_CPPv4NK2ov12PartialShape9is_staticEv) Check if this shape is static.

A shape is considered static if it has static rank, and all dimensions of the shape are static.

- Returns:
`true`

if this shape is static, else`false`

.


-
inline bool is_dynamic() const
[#](https://docs.openvino.ai#_CPPv4NK2ov12PartialShape10is_dynamicEv) Check if this shape is dynamic.

A shape is considered static if it has static rank, and all dimensions of the shape are static.

- Returns:
`false`

if this shape is static, else`true`

.


-
inline Rank rank() const
[#](https://docs.openvino.ai#_CPPv4NK2ov12PartialShape4rankEv) Get the rank of the shape.

- Returns:
The rank of the shape. This will be

[Rank::dynamic()](https://docs.openvino.ai/group__ov__transformation__common__api.html#group__ov__element__cpp__api_1ga65a44781c293f3559c2e037eb29c0f14)if the rank of the shape is dynamic.


-
bool compatible(const
[PartialShape](https://docs.openvino.ai#_CPPv4N2ov12PartialShapeE)&s) const[#](https://docs.openvino.ai#_CPPv4NK2ov12PartialShape10compatibleERK12PartialShape) Check whether this shape is compatible with the argument, i.e., whether it is possible to merge them.

Two shapes are compatible if

one or both of them has dynamic rank, or

both shapes have dynamic and equal rank, and their dimensions are elementwise compatible (see

[Dimension::compatible()](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_dimension_1a930fe268cb5c954ac8696c97a974ca5b)).

- Parameters:
**s**– The shape to be checked for compatibility with this shape.- Returns:
`true`

if this shape is compatible with`s`

, else`false`

.


-
bool same_scheme(const
[PartialShape](https://docs.openvino.ai#_CPPv4N2ov12PartialShapeE)&s) const[#](https://docs.openvino.ai#_CPPv4NK2ov12PartialShape11same_schemeERK12PartialShape) Check whether this shape represents the same scheme as the argument.

Two shapes

`s1`

and`s2`

represent the same scheme ifthey both have dynamic rank, or

they both have static and equal rank

`r`

, and for every`i`

from`0`

to`r-1`

,`s1[i]`

represents the same scheme as`s2[i]`

(see[Dimension::same_scheme()](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_dimension_1a8a463f7fdc62f36e22317d11b43d9f4c)).

- Parameters:
**s**– The shape whose scheme is being compared with this shape.- Returns:
`true`

if this shape represents the same scheme as`s`

, else`false`

.


-
bool relaxes(const
[PartialShape](https://docs.openvino.ai#_CPPv4N2ov12PartialShapeE)&s) const[#](https://docs.openvino.ai#_CPPv4NK2ov12PartialShape7relaxesERK12PartialShape) Check whether this shape is a relaxation of the argument.

Intuitively, a

[PartialShape](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_partial_shape)`s1`

is said to*relax*`s2`

(or*is a relaxation*of`s2`

) if it is “more permissive” than`s2`

. In other words,`s1`

is a relaxation of`s2`

if anything you can form by plugging things into the dynamic dimensions of`s2`

is also something you can form by plugging things into the dynamic dimensions of`s1`

, but not necessarily the other way around.`s1.relaxes(s2)`

is equivalent to`s2.refines(s1)`

.Formally,

[PartialShape](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_partial_shape)`s1`

is said to*relax*[PartialShape](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_partial_shape)`s2`

if:For every

`i`

from`0`

to`r-1`

, either`s1[i]`

contains s2[i].

- Parameters:
**s**– The shape which is being compared against this shape.- Returns:
`true`

if this shape relaxes`s`

, else`false`

.


-
bool refines(const
[PartialShape](https://docs.openvino.ai#_CPPv4N2ov12PartialShapeE)&s) const[#](https://docs.openvino.ai#_CPPv4NK2ov12PartialShape7refinesERK12PartialShape) Check whether this shape is a refinement of the argument.

Intuitively, a

[PartialShape](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_partial_shape)`s1`

is said to*relax*`s2`

(or*is a relaxation*of`s2`

) if it is “less permissive” than`s2`

. In other words,`s1`

is a relaxation of`s2`

if anything you can form by plugging things into the dynamic dimensions of`s1`

is also something you can form by plugging things into the dynamic dimensions of`s2`

, but not necessarily the other way around.`s1.refines(s2)`

is equivalent to`s2.relaxes(s1)`

.Formally,

[PartialShape](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_partial_shape)`s1`

is said to*refine*[PartialShape](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_partial_shape)`s2`

if:`s2`

has dynamic rank, or`s1`

and`s2`

both have static rank`r`

, and for every`i`

from`0`

to`r-1`

, either`s2[i]`

is dynamic, or`s1[i]`

==`s2[i]`

.

- Parameters:
**s**– The shape which is being compared against this shape.- Returns:
`true`

if this shape refines`s`

, else`false`

.


-
bool merge_rank(const Rank &r)
[#](https://docs.openvino.ai#_CPPv4N2ov12PartialShape10merge_rankERK4Rank) Checks that this shape’s rank is compatible with

`r`

, and, if this shape’s rank is dynamic and`r`

is static, updates this shape to have a rank of`r`

with dimensions all dynamic.- Returns:
`true`

if this shape’s rank is compatible with`r`

, else`false`

.


-
[Shape](https://docs.openvino.ai/classov_1_1_shape.html#_CPPv4N2ov5ShapeE)to_shape() const[#](https://docs.openvino.ai#_CPPv4NK2ov12PartialShape8to_shapeEv) Convert a static

[PartialShape](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_partial_shape)to a[PartialShape](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_partial_shape).- Throws:
std::invalid_argument – If this

[PartialShape](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_partial_shape)is dynamic.- Returns:
A new

[PartialShape](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_partial_shape)`s`

where`s[i] = size_t((*this)[i])`

.


-
bool all_non_negative() const
[#](https://docs.openvino.ai#_CPPv4NK2ov12PartialShape16all_non_negativeEv) Returns

`true`

if all static dimensions of the tensor are non-negative, else`false`

.

-
[Dimension](https://docs.openvino.ai/classov_1_1_dimension.html#_CPPv4N2ov9DimensionE)&operator[](std::ptrdiff_t i)[#](https://docs.openvino.ai#_CPPv4N2ov12PartialShapeixENSt9ptrdiff_tE) Index operator for

[PartialShape](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_partial_shape), with bound checking.- Parameters:
**i**– The index of the dimension being selected in range [-rank, rank).- Returns:
A reference to the

`i`

th[Dimension](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_dimension)of this shape.


-
const
[Dimension](https://docs.openvino.ai/classov_1_1_dimension.html#_CPPv4N2ov9DimensionE)&operator[](std::ptrdiff_t i) const[#](https://docs.openvino.ai#_CPPv4NK2ov12PartialShapeixENSt9ptrdiff_tE) Index operator for

[PartialShape](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_partial_shape), with bound checking.- Parameters:
**i**– The index of the dimension being selected in range [-rank, rank).- Returns:
A reference to the

`i`

th[Dimension](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_dimension)of this shape.


-
inline explicit operator std::vector<
[Dimension](https://docs.openvino.ai/classov_1_1_dimension.html#_CPPv4N2ov9DimensionE)>() const[#](https://docs.openvino.ai#_CPPv4NK2ov12PartialShapecvNSt6vectorI9DimensionEEEv) Returns a vector of the dimensions. This has no meaning if dynamic.


-
inline iterator begin() noexcept
[#](https://docs.openvino.ai#_CPPv4N2ov12PartialShape5beginEv) Returns a read/write iterator that points to the first element in the shape. Iteration is done in ordinary element order.


-
inline const_iterator begin() const noexcept
[#](https://docs.openvino.ai#_CPPv4NK2ov12PartialShape5beginEv) Returns a read-only (constant) iterator that points to the first element in the shape. Iteration is done in ordinary element order.


-
inline iterator end() noexcept
[#](https://docs.openvino.ai#_CPPv4N2ov12PartialShape3endEv) Returns a read/write iterator that points one past the last element in the shape. Iteration is done in ordinary element order.


-
inline const_iterator end() const noexcept
[#](https://docs.openvino.ai#_CPPv4NK2ov12PartialShape3endEv) Returns a read-only (constant) iterator that points one past the last element in the shape. Iteration is done in ordinary element order.


-
inline reverse_iterator rbegin() noexcept
[#](https://docs.openvino.ai#_CPPv4N2ov12PartialShape6rbeginEv) Returns a read/write reverse iterator that points to the last element in the shape. Iteration is done in reverse element order.


-
inline const_reverse_iterator rbegin() const noexcept
[#](https://docs.openvino.ai#_CPPv4NK2ov12PartialShape6rbeginEv) Returns a read-only (constant) reverse iterator that points to the last element in the shape. Iteration is done in reverse element order.


-
inline reverse_iterator rend() noexcept
[#](https://docs.openvino.ai#_CPPv4N2ov12PartialShape4rendEv) Returns a read/write reverse iterator that points to one before the first element in the shape. Iteration is done in reverse element order.


-
inline const_reverse_iterator rend() const noexcept
[#](https://docs.openvino.ai#_CPPv4NK2ov12PartialShape4rendEv) Returns a read-only (constant) reverse iterator that points to one before the first element in the shape. Iteration is done in reverse element order.


-
inline const_iterator cbegin() const noexcept
[#](https://docs.openvino.ai#_CPPv4NK2ov12PartialShape6cbeginEv) Returns a read-only (constant) iterator that points to the first element in the shape. Iteration is done in ordinary element order.


-
inline const_iterator cend() const noexcept
[#](https://docs.openvino.ai#_CPPv4NK2ov12PartialShape4cendEv) Returns a read-only (constant) iterator that points one past the last element in the shape. Iteration is done in ordinary element order.


-
inline const_reverse_iterator crbegin() const noexcept
[#](https://docs.openvino.ai#_CPPv4NK2ov12PartialShape7crbeginEv) Returns a read-only (constant) reverse iterator that points to the last element in the shape. Iteration is done in reverse element order.


-
inline const_reverse_iterator crend() const noexcept
[#](https://docs.openvino.ai#_CPPv4NK2ov12PartialShape5crendEv) Returns a read-only (constant) reverse iterator that points to one before the first element in the shape. Iteration is done in reverse element order.


-
inline void resize(size_t count)
[#](https://docs.openvino.ai#_CPPv4N2ov12PartialShape6resizeE6size_t) Resizes dimensions container to contain count elements.


-
inline size_t size() const
[#](https://docs.openvino.ai#_CPPv4NK2ov12PartialShape4sizeEv) Returns size of dimension vector. Requires rank to be static.


-
inline iterator insert(iterator position, const
[Dimension](https://docs.openvino.ai/classov_1_1_dimension.html#_CPPv4N2ov9DimensionE)&val)[#](https://docs.openvino.ai#_CPPv4N2ov12PartialShape6insertE8iteratorRK9Dimension) Returns a read/write iterator that points to the inserted element in the shape.


-
inline void insert(iterator position, size_t n, const
[Dimension](https://docs.openvino.ai/classov_1_1_dimension.html#_CPPv4N2ov9DimensionE)&val)[#](https://docs.openvino.ai#_CPPv4N2ov12PartialShape6insertE8iterator6size_tRK9Dimension) Inserts count copies of the value before position.


-
template<class InputIterator>

inline void insert(iterator position,[InputIterator](https://docs.openvino.ai#_CPPv4I0EN2ov12PartialShape6insertEv8iterator13InputIterator13InputIterator)first,[InputIterator](https://docs.openvino.ai#_CPPv4I0EN2ov12PartialShape6insertEv8iterator13InputIterator13InputIterator)last)[#](https://docs.openvino.ai#_CPPv4I0EN2ov12PartialShape6insertEv8iterator13InputIterator13InputIterator) Inserts elements from range [first, last) before position.


-
inline void reserve(size_t n)
[#](https://docs.openvino.ai#_CPPv4N2ov12PartialShape7reserveE6size_t) Requests that the dimensions vector capacity be enough to contain n elements.


-
template<class ...Args>

inline void emplace_back([Args](https://docs.openvino.ai#_CPPv4IDpEN2ov12PartialShape12emplace_backEvDpRR4Args)&&... args)[#](https://docs.openvino.ai#_CPPv4IDpEN2ov12PartialShape12emplace_backEvDpRR4Args) emplace element to the end of partial shape


-
std::string to_string() const
[#](https://docs.openvino.ai#_CPPv4NK2ov12PartialShape9to_stringEv) String representation of

[PartialShape](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_partial_shape).

Public Static Functions

-
static
[PartialShape](https://docs.openvino.ai#_CPPv4N2ov12PartialShapeE)dynamic(Rank r = Rank::dynamic())[#](https://docs.openvino.ai#_CPPv4N2ov12PartialShape7dynamicE4Rank) Construct a

[PartialShape](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_partial_shape)with the given rank and all dimensions (if any) dynamic.- Returns:
A

[PartialShape](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_partial_shape)with the given rank, and all dimensions (if any) dynamic.


-
static bool merge_into(
[PartialShape](https://docs.openvino.ai#_CPPv4N2ov12PartialShapeE)&dst, const[PartialShape](https://docs.openvino.ai#_CPPv4N2ov12PartialShapeE)&src)[#](https://docs.openvino.ai#_CPPv4N2ov12PartialShape10merge_intoER12PartialShapeRK12PartialShape) Try to merge one shape into another.

Merges

`src`

into`dst`

, returning`true`

on success and`false`

on failure. If`false`

is returned, the effect on`dst`

is unspecified.To merge two partial shapes

`s1`

and`s2`

is to find the most permissive partial shape`s`

that is no more permissive than`s1`

or`s2`

, if`s`

exists. For example:merge(?,?) -> ? merge(?,{?,?}) -> {?,?} merge({?,?},{?,?}) -> {?,?} merge({1,2,3,4},?) -> {1,2,3,4} merge({1,2},{1,?}) -> {1,2} merge({1,2,?,?},{1,?,3,?}) -> {1,2,3,?} merge({1,2,3},{1,2,3}) -> {1,2,3} merge({1,?},{2,?}) fails [dimension 0 constraints are inconsistent] merge({?,?},{?,?,?}) fails [ranks are inconsistent]

This function (merge_into) performs the “merge” operation described above on

`dst`

and`src`

, but overwrites`dst`

with the result and returns`true`

if merging is successful; if merging is unsuccessful, the function returns`false`

and may make unspecified changes to`dst`

.- Parameters:
**dst**–**[inout]**The shape that`src`

will be merged into.**src**– The shape that will be merged into`dst`

.

- Returns:
`true`

if merging succeeds, else`false`

.


-
static bool broadcast_merge_into(
[PartialShape](https://docs.openvino.ai#_CPPv4N2ov12PartialShapeE)&dst, const[PartialShape](https://docs.openvino.ai#_CPPv4N2ov12PartialShapeE)&src, const[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[AutoBroadcastSpec](https://docs.openvino.ai/structov_1_1op_1_1_auto_broadcast_spec.html#_CPPv4N2ov2op17AutoBroadcastSpecE)&autob)[#](https://docs.openvino.ai#_CPPv4N2ov12PartialShape20broadcast_merge_intoER12PartialShapeRK12PartialShapeRKN2ov2op17AutoBroadcastSpecE) Try to merge one shape into another along with implicit broadcasting.


Friends

- friend OPENVINO_API std::ostream & operator<< (std::ostream &str, const PartialShape &shape)
Inserts a human-readable representation of a

[PartialShape](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_partial_shape)into an output stream.The output to the stream is in “informal” notation. In other words:

If

`shape`

has dynamic rank, inserts the string`?`

.If

`shape`

has static rank, inserts the string`{`

, then inserts each dimension of`shape`

into the output stream separated by commas, then inserts`}`

.

PartialShape s1{PartialShape::dynamic())}; PartialShape s2{}; PartialShape s3{1,Dimension::dynamic(),2,3}; PartialShape s4{2,3,4}; std::cout << s1 << std::endl << s2 << std::endl << s3 << std::endl << s4 << std::endl;

? {} {1,?,2,3} {2,3,4}

- Parameters:
**str**– The output stream targeted for insertion.**shape**– The shape to be inserted into`str`

.

- Returns:
A reference to

`str`

after insertion.


- friend OPENVINO_API PartialShape operator+ (const PartialShape &s1, const PartialShape &s2)
Elementwise addition of two

[PartialShape](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_partial_shape)objects.If

`s1`

or`s2`

has dynamic rank, returns[PartialShape::dynamic()](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_partial_shape_1a5f8ce4b26f65232d9de8ab4e5e3b375d).If

`s1 and`

s2` both have static rank, and their ranks are unequal, throws std::invalid_argument.If

`s1`

and`s2`

both have static rank, and their ranks are equal, returns a new shape whose`i`

th dimension is`s1[i] + s2[i]`

.

- Parameters:
**s1**– Left operand for addition.**s2**– Right operand for addition.

- Throws:
std::invalid_argument – If

`s1`

and`s2`

have inconsistent ranks.- Returns:
The result of elementwise adding

`s1`

to`s2`

(see description).