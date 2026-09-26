source: https://github.com/vllm-project/speculators/blob/73ec09f604f962f22f40859e86a39fd5b6ec1ba3/src/speculators/utils/registry.py

-
[Notifications](https://github.com/login?return_to=%2Fvllm-project%2Fspeculators)You must be signed in to change notification settings -
[Fork 232](https://github.com/login?return_to=%2Fvllm-project%2Fspeculators)


## Expand file tree

/

Copy path# registry.py

More file actions

186 lines (149 loc) · 6.96 KB

/

Copy path# registry.py

## File metadata and controls

186 lines (149 loc) · 6.96 KB

1

2

3

4

5

6

7

8

9

10

11

12

13

14

15

16

17

18

19

20

21

22

23

24

25

26

27

28

29

30

31

32

33

34

35

36

37

38

39

40

41

42

43

44

45

46

47

48

49

50

51

52

53

54

55

56

57

58

59

60

61

62

63

64

65

66

67

68

69

70

71

72

73

74

75

76

77

78

79

80

81

82

83

84

85

86

87

88

89

90

91

92

93

94

95

96

97

98

99

100

101

102

103

104

105

106

107

108

109

110

111

112

113

114

115

116

117

118

119

120

121

122

123

124

125

126

127

128

129

130

131

132

133

134

135

136

137

138

139

140

141

142

143

144

145

146

147

148

149

150

151

152

153

154

155

156

157

158

159

160

161

162

163

164

165

166

167

168

169

170

171

172

173

174

175

176

177

178

179

180

181

182

183

184

185

186

"""

Registry system for classes in the Speculators library.

This module provides a flexible class registration and discovery system used

throughout the Speculators library. It enables automatic registration of classes

and discovery of implementations through class decorators and module imports.

The registry system is used to track different implementations of token proposal

methods, speculative decoding algorithms, and speculator models, allowing for

dynamic discovery and instantiation based on configuration parameters.

Classes:

ClassRegistryMixin: Base mixin for creating class registries with decorators

and optional auto-discovery capabilities through registry_auto_discovery flag.

AutoClassRegistryMixin: A backward-compatible version of ClassRegistryMixin with

auto-discovery enabled by default

"""

from collections.abc import Callable

from typing import Any, ClassVar

__all__ = ["ClassRegistryMixin"]

class ClassRegistryMixin:

"""

A mixin class that provides a registration system for tracking class

implementations with optional auto-discovery capabilities.

This mixin allows classes to maintain a registry of subclasses that can be

dynamically discovered and instantiated. Classes that inherit from this mixin

can use the @register decorator to add themselves to the registry.

The registry is class-specific, meaning each class that inherits from this mixin

will have its own separate registry of implementations.

The mixin can also be configured to automatically discover and register classes

from specified packages by setting registry_auto_discovery=True and defining

an auto_package class variable to specify which package(s) should be automatically

imported to discover implementations.

Example:

```python

class BaseAlgorithm(ClassRegistryMixin):

pass

@BaseAlgorithm.register()

class ConcreteAlgorithm(BaseAlgorithm):

pass

@BaseAlgorithm.register("custom_name")

class AnotherAlgorithm(BaseAlgorithm):

pass

# Get all registered algorithm implementations

algorithms = BaseAlgorithm.registered_classes()

```

Example with auto-discovery:

```python

class TokenProposal(ClassRegistryMixin):

registry_auto_discovery = True

auto_package = "speculators.proposals"

# This will automatically import all modules in the proposals package

# and register any classes decorated with @TokenProposal.register()

proposals = TokenProposal.registered_classes()

```

:cvar registry: A dictionary mapping class names to classes that have been

registered to the extending subclass through the @subclass.register() decorator

:cvar registry_auto_discovery: A flag that enables automatic discovery and import of

modules from the auto_package when set to True. Default is False.

:cvar registry_populated: A flag that tracks whether the registry has been

populated with classes from the specified package(s).

"""

registry: ClassVar[dict[str, type[Any]] | None] = None

registry_auto_discovery: ClassVar[bool] = False

registry_populated: ClassVar[bool] = False

@classmethod

def register(cls, name: str | None = None) -> Callable[[type[Any]], type[Any]]:

"""

An invoked class decorator that registers that class with the registry under

either the provided name or the class name if no name is provided.

Example:

```python

@ClassRegistryMixin.register()

class ExampleClass:

...

@ClassRegistryMixin.register("custom_name")

class AnotherExampleClass:

...

```

:param name: Optional name to register the class under. If None, the class name

is used as the registry key.

:return: A decorator function that registers the decorated class.

:raises ValueError: If name is provided but is not a string.

"""

if name is not None and not isinstance(name, str):

raise ValueError(

"ClassRegistryMixin.register() name must be a string or None. "

f"Got {name}."

)

return lambda subclass: cls.register_decorator(subclass, name=name)

@classmethod

def register_decorator(cls, clazz: type[Any], name: str | None = None) -> type[Any]:

"""

A non-invoked class decorator that registers the class with the registry.

If passed through a lambda, then name can be passed in as well.

Otherwise, the only argument is the decorated class.

Example:

```python

@ClassRegistryMixin.register_decorator

class ExampleClass:

...

```

:param clazz: The class to register

:param name: Optional name to register the class under. If None, the class name

is used as the registry key.

:return: The registered class.

:raises TypeError: If the decorator is used incorrectly or if the class is not

a type.

:raises ValueError: If the class is already registered or if name is provided

but is not a string.

"""

if not isinstance(clazz, type):

raise TypeError(

"ClassRegistryMixin.register_decorator must be used as a class "

"decorator and without invocation."

f"Got improper clazz arg {clazz}."

)

if not name:

name = clazz.__name__

elif not isinstance(name, str):

raise ValueError(

"ClassRegistryMixin.register_decorator must be used as a class "

"decorator and without invocation. "

f"Got imporoper name arg {name}."

)

if cls.registry is None:

cls.registry = {}

if name in cls.registry:

raise ValueError(

f"ClassRegistryMixin.register_decorator cannot register a class "

f"{clazz} with the name {name} because it is already registered."

)

cls.registry[name] = clazz

return clazz

@classmethod

def registered_classes(cls) -> tuple[type[Any], ...]:

"""

Returns a tuple of all classes that have been registered with this registry.

If registry_auto_discovery is True, this method will first call

auto_populate_registry to ensure that all available implementations from

the specified auto_package are discovered and registered before returning

the list.

:return: A tuple containing all registered class implementations, including

those discovered through auto-importing when registry_auto_discovery==True.

:raises ValueError: If called before any classes have been registered.

"""

if cls.registry is None:

raise ValueError(

"ClassRegistryMixin.registered_classes() must be called after "

"registering classes with ClassRegistryMixin.register()."

)

return tuple(cls.registry.values())