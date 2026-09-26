source: https://github.com/vllm-project/guidellm/blob/main/pyproject.toml

-
[Notifications](https://github.com/login?return_to=%2Fvllm-project%2Fguidellm)You must be signed in to change notification settings -
[Fork 238](https://github.com/login?return_to=%2Fvllm-project%2Fguidellm)


## Expand file tree

/

Copy path# pyproject.toml

More file actions

383 lines (340 loc) · 11.9 KB

/

Copy path# pyproject.toml

## File metadata and controls

383 lines (340 loc) · 11.9 KB

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

242

243

244

245

246

247

248

249

250

251

252

253

254

255

256

257

258

259

260

261

262

263

264

265

266

267

268

269

270

271

272

273

274

275

276

277

278

279

280

281

282

283

284

285

286

287

288

289

290

291

292

293

294

295

296

297

298

299

300

301

302

303

304

305

306

307

308

309

310

311

312

313

314

315

316

317

318

319

320

321

322

323

324

325

326

327

328

329

330

331

332

333

334

335

336

337

338

339

340

341

342

343

344

345

346

347

348

349

350

351

352

353

354

355

356

357

358

359

360

361

362

363

364

365

366

367

368

369

370

371

372

373

374

375

376

377

378

379

380

381

382

383

[build-system]

requires = ["setuptools >= 61.0", "setuptools-git-versioning>=2.0,<3"]

build-backend = "setuptools.build_meta"

[tool.setuptools.packages.find]

where = ["src"]

include = ["*"]

[tool.setuptools.package-data]

guidellm = ["py.typed"]

"guidellm.schemas.benchmark.scenarios" = ["*.json", "**/*.json"]

"guidellm.benchmark.outputs.html_report" = ["*.html", "*.css", "*.js"]

[tool.uv]

required-environments = [

"sys_platform == 'darwin' and platform_machine == 'arm64'",

"sys_platform == 'linux' and platform_machine == 'x86_64'",

"sys_platform == 'linux' and platform_machine == 'aarch64'",

]

[[tool.uv.index]]

name = "pytorch-cpu"

url = "https://download.pytorch.org/whl/cpu"

explicit = true

[tool.uv.sources]

torch = { index = "pytorch-cpu" }

torchcodec = { index = "pytorch-cpu" }

# ************************************************

# ********** Project Metadata **********

# ************************************************

[project]

dynamic = ["version"]

name = "guidellm"

description = "Guidance platform for deploying and managing large language models."

readme = { file = "README.md", content-type = "text/markdown" }

requires-python = ">=3.10.0,<4.0"

license = { text = "Apache-2.0" }

authors = [{ name = "Red Hat" }]

keywords = [

"ai",

"benchmarking",

"deep-learning",

"deployment",

"evaluation",

"guidance",

"inference",

"language-models",

"large-language-model",

"llm",

"machine-learning",

"model-benchmark",

"model-evaluation",

"nlp",

"performance",

"vllm",

]

dependencies = [

"click~=8.4.0",

"culsans~=0.10.0",

"datasets>=5.0.1",

"eval_type_backport",

"faker",

"ftfy>=6.0.0",

"httpx[http2]<1.0.0",

"loguru",

"msgpack",

"numpy>=2.0.0",

"protobuf",

"pydantic>=2.11.7",

"pydantic-settings>=2.0.0",

"pyyaml>=6.0.0",

"rich",

"sanic",

"tabulate",

"transformers",

"uvloop>=0.18",

"torch",

"more-itertools>=10.8.0",

"typing-extensions>=4.15.0",

"websockets>=13.0"

]

[project.optional-dependencies]

# Meta Extras

all = ["guidellm[perf,tokenizers,audio,vision,plot]"]

recommended = ["guidellm[perf,tokenizers]"]

# Feature Extras

plot = ["matplotlib>=3.10.9"]

perf = ["orjson", "msgpack", "msgspec", "uvloop"]

tokenizers = ["tiktoken", "blobfile", "mistral-common"]

audio = [

# Version with stable aarch64 CPU-only wheels

"datasets[audio]>=4.1.0",

# Torchcodec 0.11 requires PyTorch == 2.11

# Torchcodec >=0.12 requires PyTorch >= 2.11

"torch>=2.11",

"torchcodec>=0.11",

]

vision = [

"datasets[vision]",

"pillow",

"imageio[ffmpeg]",

]

[dependency-groups]

build = [

"build>=1.0.0",

"setuptools>=61.0",

"setuptools-git-versioning>=2.0,<3",

]

quality = [

# code quality

"mypy~=2.1.0",

"ruff~=0.15.20",

"import-linter~=2.13.0",

# docs quality

"mdformat~=1.0.0",

"mdformat-footnote~=0.1.3",

"mdformat-frontmatter~=2.0.10",

"mdformat-gfm~=1.0.0",

# type-checking

"pandas-stubs",

"types-PyYAML~=6.0.1",

# link checking

"mkdocs-linkcheck~=1.0.6",

]

test = [

# Install all optional dependencies

"guidellm[all]",

"pytest~=9.1.1",

"pytest-asyncio~=1.4.0",

"pytest-cov~=7.1.0",

"pytest-mock~=3.15.1",

"pytest-rerunfailures~=16.4",

"pytest-timeout~=2.4.0",

"pytest-httpx~=0.36.2",

"respx~=0.23.1",

"trio~=0.33.0",

"logot~=1.7.0",

]

env = [

"pre-commit",

"tox",

"tox-uv",

]

dev = [

{include-group = "build"},

{include-group = "quality"},

{include-group = "test"},

{include-group = "env"},

]

[project.urls]

homepage = "https://github.com/vllm-project/guidellm"

source = "https://github.com/vllm-project/guidellm"

issues = "https://github.com/vllm-project/guidellm/issues"

docs = "https://github.com/vllm-project/guidellm/tree/main/docs"

[project.entry-points.console_scripts]

guidellm = "guidellm.__main__:cli"

# ************************************************

# ********** Code Quality Tools **********

# ************************************************

[tool.isort]

profile = "black"

[tool.mypy]

files = ["src/guidellm"]

python_version = '3.10'

warn_redundant_casts = true

warn_unused_ignores = false

show_error_codes = true

namespace_packages = true

exclude = ["venv", ".tox"]

# Silence "type import errors" as our 3rd-party libs does not have types

# Check: https://mypy.readthedocs.io/en/latest/config_file.html#import-discovery

follow_imports = 'silent'

[[tool.mypy.overrides]]

module = [

"datasets.*",

"transformers.*",

"setuptools.*",

"setuptools_git_versioning.*",

"torchcodec.*",

"vllm",

"vllm.*"

]

ignore_missing_imports = true

[tool.ruff]

target-version = "py310"

line-length = 88

indent-width = 4

exclude = ["build", "dist", "env", ".venv*"]

[tool.ruff.format]

quote-style = "double"

indent-style = "space"

line-ending = "lf"

[tool.ruff.lint]

ignore = [

"COM812", # ignore trailing comma errors due to older Python versions

"PD011", # ignore .values usage since ruff assumes it's a Pandas DataFrame

"PLR0913", # ignore too many arguments in function definitions

"PLW1514", # allow Path.open without encoding

"RET505", # allow `else` blocks

"RET506", # allow `else` blocks

"S311", # allow standard pseudo-random generators

"TC001", # ignore imports used only for type checking

"TC002", # ignore imports used only for type checking

"TC003", # ignore imports used only for type checking

"FIX002", # Allow TODO comments

"FIX004", # Allow HACK comments

]

select = [

# Rules reference: https://docs.astral.sh/ruff/rules/

# Code Style / Formatting

"E", # pycodestyle: checks adherence to PEP 8 conventions including spacing, indentation, and line length

"W", # pycodestyle: checks adherence to PEP 8 conventions including spacing, indentation, and line length

"A", # flake8-builtins: prevents shadowing of Python built-in names

"C", # Convention: ensures code adheres to specific style and formatting conventions

"COM", # flake8-commas: enforces the correct use of trailing commas

"ERA", # eradicate: detects commented-out code that should be removed

"I", # isort: ensures imports are sorted in a consistent manner

"ICN", # flake8-import-conventions: enforces import conventions for better readability

"N", # pep8-naming: enforces PEP 8 naming conventions for classes, functions, and variables

"NPY", # NumPy: enforces best practices for using the NumPy library

"PD", # pandas-vet: enforces best practices for using the pandas library

"PT", # flake8-pytest-style: enforces best practices and style conventions for pytest tests

"PTH", # flake8-use-pathlib: encourages the use of pathlib over os.path for file system operations

"Q", # flake8-quotes: enforces consistent use of single or double quotes

"TCH", # flake8-type-checking: enforces type checking practices and standards

"TID", # flake8-tidy-imports: enforces tidy and well-organized imports

"RUF022", # flake8-ruff: enforce sorting of __all__ in modules

# Code Structure / Complexity

"C4", # flake8-comprehensions: improves readability and performance of list, set, and dict comprehensions

"C90", # mccabe: checks for overly complex code using cyclomatic complexity

"ISC", # flake8-implicit-str-concat: prevents implicit string concatenation

"PIE", # flake8-pie: identifies and corrects common code inefficiencies and mistakes

"R", # Refactor: suggests improvements to code structure and readability

"SIM", # flake8-simplify: simplifies complex expressions and improves code readability

# Code Security / Bug Prevention

"ARG", # flake8-unused-arguments: detects unused function and method arguments

"ASYNC", # flake8-async: identifies incorrect or inefficient usage patterns in asynchronous code

"B", # flake8-bugbear: detects common programming mistakes and potential bugs

"BLE", # flake8-blind-except: prevents blind exceptions that catch all exceptions without handling

"E", # Error: detects and reports errors in the code

"F", # Pyflakes: detects unused imports, shadowed imports, undefined variables, and various formatting errors in string operations

"INP", # flake8-no-pep420: prevents implicit namespace packages by requiring __init__.py

"PGH", # pygrep-hooks: detects deprecated and dangerous code patterns

"PL", # Pylint: comprehensive source code analyzer for enforcing coding standards and detecting errors

"RSE", # flake8-raise: ensures exceptions are raised correctly

"S", # flake8-bandit: detects security issues and vulnerabilities in the code

"SLF", # flake8-self: prevents incorrect usage of the self argument in class methods

"T10", # flake8-debugger: detects the presence of debugging tools such as pdb

"T20", # flake8-print: detects print statements left in the code

"UP", # pyupgrade: automatically upgrades syntax for newer versions of Python

"W", # Warning: provides warnings about potential issues in the code

"YTT", # flake8-2020: identifies code that will break with future Python releases

# Code Documentation

"FIX", # flake8-fixme: detects FIXMEs and other temporary comments that should be resolved

]

[tool.ruff.lint.extend-per-file-ignores]

"tests/**/*.py" = [

"S101", # asserts allowed in tests

"ARG", # Unused function args allowed in tests

"PLR2004", # Magic value used in comparison

"TCH002", # No import only type checking in tests

"SLF001", # enable private member access in tests

"S105", # allow hardcoded passwords in tests

"S311", # allow standard pseudo-random generators in tests

"PT011", # allow generic exceptions in tests

"N806", # allow uppercase variable names in tests

"PGH003", # allow general ignores in tests

"S106", # allow hardcoded passwords in tests

"PLR0915", # allow complex statements in tests

]

"scripts/**/*.py" = [

"T201", # print statements are the primary output mechanism for scripts

"INP001", # scripts/ is not a package

]

"tests/js/**/*.py" = [

"INP001", # Node test helpers live beside package.json, not as a Python package

]

[tool.ruff.lint.isort]

known-first-party = ["guidellm", "tests"]

[tool.importlinter]

root_package = "guidellm"

exclude_type_checking_imports = true

include_external_packages = true

[[tool.importlinter.contracts]]

name = "Enforce import layers"

type = "layers"

containers = ["guidellm"]

layers = [

"__main__",

"cli",

"entrypoints",

"benchmark | mock_server",

"data | backends",

"scheduler",

# utils/extras/schemas can interdepend so treat

# them as one layer and check with a separate rule

"utils : extras : schemas",

"logger",

"settings",

]

exhaustive = true

exhaustive_ignores = ["version"]

[[tool.importlinter.contracts]]

name = "Check acyclic siblings on utility modules"

type = "acyclic_siblings"

ancestors = [

"guidellm.utils",

"guidellm.schemas",

"guidellm.extras",

]

[[tool.importlinter.contracts]]

name = "Avoid slow importing libraries in the worker hot-path"

type = "forbidden"

source_modules = [

"guidellm.scheduler",

"guidellm.backends",

"guidellm.schemas",

"guidellm.schemas.**",

]

forbidden_modules = [

"datasets",

"transformers",

"torch",

"numpy",

]

[[tool.importlinter.contracts]]

name = "Disallow importing entrypoint modules directly"

type = "protected"

protected_modules = [

"guidellm.benchmark",

"guidellm.mock_server",

]

allowed_importers = [

"guidellm.entrypoints",

]

[tool.pytest.ini_options]

addopts = '-s -vvv --cache-clear'

logot_capturer = "logot.loguru.LoguruCapturer"

markers = [

"smoke: quick tests to check basic functionality",

"sanity: detailed tests to ensure major functions work correctly",

"regression: tests to ensure that new changes do not break existing functionality",

"slow: marks tests that are slow to run, e.g. those that download or load real models/tokenizers",

]