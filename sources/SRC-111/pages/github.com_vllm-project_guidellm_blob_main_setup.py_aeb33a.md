source: https://github.com/vllm-project/guidellm/blob/main/setup.py

-
[Notifications](https://github.com/login?return_to=%2Fvllm-project%2Fguidellm)You must be signed in to change notification settings -
[Fork 238](https://github.com/login?return_to=%2Fvllm-project%2Fguidellm)


## Expand file tree

/

Copy path# setup.py

More file actions

127 lines (105 loc) · 4.74 KB

/

Copy path# setup.py

## File metadata and controls

127 lines (105 loc) · 4.74 KB

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

import os

import re

from pathlib import Path

from packaging.version import Version

from setuptools import setup

from setuptools_git_versioning import count_since, get_branch, get_sha, get_tags

LAST_RELEASE_VERSION = Version("0.4.0")

TAG_VERSION_PATTERN = re.compile(r"^v(\d+\.\d+\.\d+)$")

def get_last_version_diff() -> tuple[Version, str | None, int | None]:

"""

Get the last version, last tag, and the number of commits since the last tag.

If no tags are found, return the last release version and None for the tag/commits.

:returns: A tuple containing the last version, last tag, and number of commits since

the last tag.

"""

tagged_versions = [

(Version(match.group(1)), tag)

for tag in get_tags(root=Path(__file__).parent)

if (match := TAG_VERSION_PATTERN.match(tag))

]

tagged_versions.sort(key=lambda tv: tv[0])

last_version, last_tag = (

tagged_versions[-1] if tagged_versions else (LAST_RELEASE_VERSION, None)

)

commits_since_last = (

count_since(last_tag + "^{commit}", root=Path(__file__).parent)

if last_tag

else None

)

return last_version, last_tag, commits_since_last

def get_next_version(

build_type: str, build_iteration: str | int | None

) -> tuple[Version, str | None, int]:

"""

Get the next version based on the build type and iteration.

- build_type == release: take the last version and add a post if build iteration

- build_type == candidate: increment to next minor, add 'rc' with build iteration

- build_type == nightly: increment to next minor, add 'a' with build iteration

- build_type == alpha: increment to next minor, add 'a' with build iteration

- build_type == dev: increment to next minor, add 'dev' with build iteration

:param build_type: The type of build (release, candidate, nightly, alpha, dev).

:param build_iteration: The build iteration number. If None, defaults to the number

of commits since the last tag or 0 if no commits since the last tag.

:returns: A tuple containing the next version, the last tag the version is based

off of (if any), and the final build iteration used.

"""

version, tag, commits_since_last = get_last_version_diff()

if not build_iteration and build_iteration != 0:

build_iteration = commits_since_last or 0

elif isinstance(build_iteration, str):

build_iteration = int(build_iteration)

if build_type == "release":

if commits_since_last:

# add post since we have commits since last tag

version = Version(f"{version.base_version}.post{build_iteration}")

return version, tag, build_iteration

# not in release pathway, so need to increment to target next release version

version_next = Version(f"{version.major}.{version.minor + 1}.0")

if build_type == "candidate":

# add 'rc' since we are in candidate pathway

version = Version(f"{version_next}.rc{build_iteration}")

elif build_type in ["nightly", "alpha"]:

# add 'a' since we are in nightly or alpha pathway

version = Version(f"{version_next}.a{build_iteration}")

# assume 'dev' if not in any of the above pathways

# None indicates git failed to find last tag

# 0 indicates no new commits since last tag

elif commits_since_last != 0:

version = Version(f"{version_next}.dev{build_iteration}")

return version, tag, build_iteration

def write_version_files() -> tuple[Path, Path]:

"""

Write the version information to version.txt and version.py files.

version.txt contains the version string.

version.py contains the version plus additional metadata.

:returns: A tuple containing the paths to the version.txt and version.py files.

"""

build_type = os.getenv("GUIDELLM_BUILD_TYPE", "dev").lower()

version, tag, build_iteration = get_next_version(

build_type=build_type,

build_iteration=os.getenv("GUIDELLM_BUILD_ITERATION"),

)

module_path = Path(__file__).parent / "src" / "guidellm"

version_txt_path = module_path / "version.txt"

version_py_path = module_path / "version.py"

with version_txt_path.open("w") as file:

file.write(str(version))

with version_py_path.open("w") as file:

file.writelines(

[

f'version = "{version}"\n',

f'build_type = "{build_type}"\n',

f'build_iteration = "{build_iteration}"\n',

f'git_commit = "{get_sha()}"\n',

f'git_branch = "{get_branch()}"\n',

f'git_last_tag = "{tag}"\n',

]

)

return version_txt_path, version_py_path

setup(

setuptools_git_versioning={

"enabled": True,

"version_file": str(write_version_files()[0]),

}

)