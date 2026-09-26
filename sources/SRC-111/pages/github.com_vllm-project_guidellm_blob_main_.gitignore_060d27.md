source: https://github.com/vllm-project/guidellm/blob/main/.gitignore

-
[Notifications](https://github.com/login?return_to=%2Fvllm-project%2Fguidellm)You must be signed in to change notification settings -
[Fork 238](https://github.com/login?return_to=%2Fvllm-project%2Fguidellm)


## Expand file tree

/

Copy path# .gitignore

More file actions

241 lines (195 loc) · 4.4 KB

/

Copy path# .gitignore

## File metadata and controls

241 lines (195 loc) · 4.4 KB

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

187

188

189

190

191

192

193

194

195

196

197

198

199

200

201

202

203

204

205

206

207

208

209

210

211

212

213

214

215

216

217

218

219

220

221

222

223

224

225

226

227

228

229

230

231

232

233

234

235

236

237

238

239

240

241

## Python

# build version files

src/guidellm/version.txt

src/guidellm/version.py

# Output files

benchmarks.json

benchmarks.yaml

benchmarks.csv

benchmarks.html

benchmarks.png

benchmarks.jpg

benchmarks.jpeg

benchmarks.svg

benchmarks.pdf

# Byte-compiled / optimized / DLL files

__pycache__/

*.py[cod]

*$py.class

# C extensions

*.so

# Distribution / packaging

.Python

build/

develop-eggs/

dist/

downloads/

eggs/

.eggs/

lib/

lib64/

parts/

sdist/

var/

wheels/

share/python-wheels/

*.egg-info/

.installed.cfg

*.egg

MANIFEST

# PyInstaller

# Usually these files are written by a python script from a template

# before PyInstaller builds the exe, so as to inject date/other infos into it.

*.manifest

*.spec

# Installer logs

pip-log.txt

pip-delete-this-directory.txt

# Unit test / coverage reports

htmlcov/

.tox/

.nox/

.coverage

.coverage.*

.cache

nosetests.xml

coverage.xml

*.cover

*.py,cover

.hypothesis/

.pytest_cache/

cover/

# Translations

*.mo

*.pot

# Django stuff:

*.log

local_settings.py

db.sqlite3

db.sqlite3-journal

# Flask stuff:

instance/

.webassets-cache

# Scrapy stuff:

.scrapy

# Sphinx documentation

docs/_build/

# PyBuilder

.pybuilder/

target/

# Jupyter Notebook

.ipynb_checkpoints

# IPython

profile_default/

ipython_config.py

# pyenv

# For a library or package, you might want to ignore these files since the code is

# intended to run in multiple environments; otherwise, check them in:

.python-version

# pipenv

# According to pypa/pipenv#598, it is recommended to include Pipfile.lock in version control.

# However, in case of collaboration, if having platform-specific dependencies or dependencies

# having no cross-platform support, pipenv may install dependencies that don't work, or not

# install all needed dependencies.

#Pipfile.lock

# poetry

# Similar to Pipfile.lock, it is generally recommended to include poetry.lock in version control.

# This is especially recommended for binary packages to ensure reproducibility, and is more

# commonly ignored for libraries.

# https://python-poetry.org/docs/basic-usage/#commit-your-poetrylock-file-to-version-control

#poetry.lock

# pdm

# Similar to Pipfile.lock, it is generally recommended to include pdm.lock in version control.

#pdm.lock

# pdm stores project-wide configurations in .pdm.toml, but it is recommended to not include it

# in version control.

# https://pdm.fming.dev/latest/usage/project/#working-with-version-control

.pdm.toml

.pdm-python

.pdm-build/

# PEP 582; used by e.g. github.com/David-OConnor/pyflow and github.com/pdm-project/pdm

__pypackages__/

# Celery stuff

celerybeat-schedule

celerybeat.pid

# SageMath parsed files

*.sage.py

# Environments

.env

.venv

env/

venv/

ENV/

env.bak/

venv.bak/

# Spyder project settings

.spyderproject

.spyproject

# Rope project settings

.ropeproject

# mkdocs documentation

/site

# mypy

.mypy_cache/

.dmypy.json

dmypy.json

# Pyre type checker

.pyre/

# pytype static type analyzer

.pytype/

# Cython debug symbols

cython_debug/

# PyCharm

# JetBrains specific template is maintained in a separate JetBrains.gitignore that can

# be found at https://github.com/github/gitignore/blob/main/Global/JetBrains.gitignore

# and can be added to the global gitignore or merged into this file. For a more nuclear

# option (not recommended) you can uncomment the following to ignore the entire idea folder.

.idea/

# MacOS files

.DS_Store

# Project specific files

*.json

*.yaml

# But not scenarios

!src/guidellm/schemas/benchmark/scenarios/*.json

!src/guidellm/schemas/benchmark/scenarios/**/*.json

# HTML report Node smoke-test manifests (needed by tox -e test-html-js)

!tests/js/package.json

!tests/js/package-lock.json

# Vendored offline tokenizer fixtures for tests (no Hub downloads)

!tests/fixtures/tokenizers/**/*.json

!tests/fixtures/tokenizers/**/*.yaml

## AI

# Ignore any AI memory files except for AGENTS.md and shared agent skills

# Shared Agent Skills (agentskills.io) — track these

# Canonical location: .agents/skills/

# Claude code

# .claude is linked to .agents

# CLAUDE.md is linked to AGENTS.md

# Cursor

# Use AGENTS.md & .agents/skills/ to manage Cursor skills & rules

.cursor/

.cursorrules/

# Gemini CLI

.gemini/

# Optional local Node tooling leftovers

/node_modules/

tests/js/node_modules/

/.pnp

.pnp.*

.yarn/*

!.yarn/patches

!.yarn/plugins

!.yarn/releases

!.yarn/versions

coverage/

build/

*.pem

npm-debug.log*

yarn-debug.log*

yarn-error.log*

.pnpm-debug.log*

*.tsbuildinfo

.eslintcache

# e2e tests

bin/