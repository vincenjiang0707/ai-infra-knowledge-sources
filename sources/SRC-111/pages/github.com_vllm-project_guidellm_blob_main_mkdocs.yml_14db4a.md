source: https://github.com/vllm-project/guidellm/blob/main/mkdocs.yml

-
[Notifications](https://github.com/login?return_to=%2Fvllm-project%2Fguidellm)You must be signed in to change notification settings -
[Fork 238](https://github.com/login?return_to=%2Fvllm-project%2Fguidellm)


## Expand file tree

/

Copy path# mkdocs.yml

More file actions

131 lines (123 loc) · 3.01 KB

/

Copy path# mkdocs.yml

## File metadata and controls

131 lines (123 loc) · 3.01 KB

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

site_name: GuideLLM Docs

site_description: Documentation for GuideLLM focused on evaluating the deployability of an LLM for real-world inference

site_url: https://vllm-project.github.io/guidellm

repo_url: https://github.com/vllm-project/guidellm

edit_uri: https://github.com/vllm-project/guidellm/tree/main/docs

exclude_docs: |

en/**/*.md

theme:

name: material

font:

text: Roboto

code: Roboto Mono

language: en

logo: assets/guidellm-icon-light.png

favicon: assets/guidellm-icon-blue.png

features:

- content.action.edit

- content.code.annotate

- content.code.copy

- content.code.select

- navigation.footer

- navigation.indexes

- navigation.instant

- navigation.path

- navigation.top

- navigation.tracking

- search.highlight

- search.share

- search.suggest

- toc.follow

palette:

# Palette toggle for automatic mode

- media: "(prefers-color-scheme)"

toggle:

icon: material/brightness-auto

name: Switch to light mode

# Palette toggle for light mode

- media: "(prefers-color-scheme: light)"

scheme: youtube

toggle:

icon: material/brightness-7

name: Switch to dark mode

# Palette toggle for dark mode

- media: "(prefers-color-scheme: dark)"

scheme: slate

toggle:

icon: material/brightness-4

name: Switch to system preference

markdown_extensions:

- abbr

- admonition

- attr_list

- def_list

- footnotes

- md_in_html

- pymdownx.arithmatex:

generic: true

- pymdownx.blocks.caption

- pymdownx.details

- pymdownx.emoji:

emoji_index: !!python/name:material.extensions.emoji.twemoji

emoji_generator: !!python/name:material.extensions.emoji.to_svg

- pymdownx.highlight:

anchor_linenums: true

line_spans: __span

pygments_lang_class: true

- pymdownx.inlinehilite

- pymdownx.mark

- pymdownx.smartsymbols

- pymdownx.snippets

- pymdownx.superfences:

custom_fences:

- name: mermaid

class: mermaid

format: !!python/name:pymdownx.superfences.fence_code_format

- pymdownx.tabbed:

alternate_style: true

- pymdownx.tasklist:

custom_checkbox: true

- pymdownx.tilde

- tables

plugins:

- api-autonav:

modules: ['src/guidellm']

- gen-files:

scripts:

- docs/scripts/gen_files.py

- mike

- minify:

minify_html: true

- mkdocs-nav-weight

- mkdocstrings:

default_handler: python

handlers:

python:

options:

docstring_style: sphinx

- search

- section-index

- social

- tags

extra:

generator: false

alternate:

- name: English

link: /guidellm/

lang: en

- name: 简体中文

link: /guidellm/zh/

lang: zh

version:

provider: mike

alias: true

default:

- stable

- development

extra_css:

- stylesheets/style.css

extra_javascript:

- scripts/translation-map.js

- scripts/language-switcher.js

- scripts/mathjax.js

- https://unpkg.com/mathjax@3/es5/tex-mml-chtml.js