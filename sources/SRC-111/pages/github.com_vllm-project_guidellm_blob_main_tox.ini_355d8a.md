source: https://github.com/vllm-project/guidellm/blob/main/tox.ini

-
[Notifications](https://github.com/login?return_to=%2Fvllm-project%2Fguidellm)You must be signed in to change notification settings -
[Fork 238](https://github.com/login?return_to=%2Fvllm-project%2Fguidellm)


## Expand file tree

/

Copy path# tox.ini

More file actions

133 lines (108 loc) · 2.85 KB

/

Copy path# tox.ini

## File metadata and controls

133 lines (108 loc) · 2.85 KB

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

[tox]

min_version = 4.22

env_list = {lint,type,translation}-check,test-{unit,integration,e2e}

[testenv:tests]

description = Run all tests

runner = uv-venv-lock-runner

dependency_groups = dev

commands =

python -m pytest {posargs:tests/}

[testenv:test-unit]

description = Run unit tests

base = tests

commands =

python -m pytest tests/unit {posargs}

[testenv:test-integration]

description = Run integration tests

base = tests

commands =

python -m pytest tests/integration --timeout=240 {posargs}

[testenv:test-e2e]

description = Run end-to-end tests

base = tests

commands =

python -m pytest tests/e2e {posargs}

[testenv:test-html-js]

description = Run HTML report Node/jsdom smoke tests

base = tests

allowlist_externals =

npm

node

passenv =

PATH

setenv =

GUIDELLM_HTML_FIXTURE = {envtmpdir}/benchmarks.html

PYTHONPATH = {toxinidir}

commands =

python tests/js/generate_fixture.py {env:GUIDELLM_HTML_FIXTURE}

npm install --prefix tests/js

npm test --prefix tests/js

[testenv:lint-check]

description = Run all quality checks

base = tests

commands =

ruff format --check --diff

ruff check

import-linter lint

python -m mdformat --check README.md DEVELOPING.md CONTRIBUTING.md CODE_OF_CONDUCT.md docs/ src/ tests/

python docs/scripts/check_translations.py

[testenv:lint-fix]

description = Run style checks and fixes

base = tests

commands =

ruff format

ruff check --fix

import-linter lint

python -m mdformat README.md DEVELOPING.md CONTRIBUTING.md CODE_OF_CONDUCT.md docs/ src/ tests/

[testenv:type-check]

description = Run type checks

base = tests

commands =

mypy --check-untyped-defs {posargs}

[testenv:link-check]

description = Run link checks for root and docs markdown files

base = tests

commands =

mkdocs-linkcheck ./

mkdocs-linkcheck docs/

[testenv:translation-check]

description = Validate translated documentation metadata and structure

runner = uv-venv-lock-runner

skip_install = true

commands =

python docs/scripts/check_translations.py

[testenv:build]

description = Build the project

dependency_groups = dev

setenv =

GUIDELLM_BUILD_TYPE = {env:GUIDELLM_BUILD_TYPE:dev}

GUIDELLM_BUILD_ITERATION = {env:GUIDELLM_BUILD_ITERATION:}

commands =

python -m build

[testenv:clean]

description = Clean up build, dist, and cache files

runner = virtualenv

skip_install = true

env_log_dir = /tmp/.tox_clean

allowlist_externals =

find

rm

commands =

rm -rf build

rm -rf dist

rm -rf *.egg-info

find . -type f -name "*.pyc" -delete

find . -type d -name "__pycache__" -exec rm -r {} +

rm -rf .mypy_cache

rm -rf .pytest_cache

rm -rf .ruff_cache

rm -rf .coverage

rm -rf .tox

[testenv:lock]

description = Update pylock

runner = virtualenv

skip_install = true

allowlist_externals = ./scripts/lock.sh

deps = uv

commands =

./scripts/lock.sh {posargs}