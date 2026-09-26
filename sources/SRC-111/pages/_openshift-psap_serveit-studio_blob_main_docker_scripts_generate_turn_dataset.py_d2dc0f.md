source: https://github.com/openshift-psap/serveit-studio/blob/main/docker/scripts/generate_turn_dataset.py

-
[Notifications](https://github.com/login?return_to=%2Fopenshift-psap%2Fserveit-studio)You must be signed in to change notification settings -
[Fork 1](https://github.com/login?return_to=%2Fopenshift-psap%2Fserveit-studio)


## Expand file tree

/

Copy path# generate_turn_dataset.py

More file actions

485 lines (409 loc) · 20.4 KB

/

Copy path# generate_turn_dataset.py

## File metadata and controls

485 lines (409 loc) · 20.4 KB

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

384

385

386

387

388

389

390

391

392

393

394

395

396

397

398

399

400

401

402

403

404

405

406

407

408

409

410

411

412

413

414

415

416

417

418

419

420

421

422

423

424

425

426

427

428

429

430

431

432

433

434

435

436

437

438

439

440

441

442

443

444

445

446

447

448

449

450

451

452

453

454

455

456

457

458

459

460

461

462

463

464

465

466

467

468

469

470

471

472

473

474

475

476

477

478

479

480

481

482

483

484

485

#!/usr/bin/env python3

"""Generate multi-turn conversation dataset using guidellm's SyntheticTextDataset.

Produces a JSONL file compatible with guidellm's file-based dataset loading,

preserving the exact same data format that guidellm generates in-memory.

Uses multiprocessing for parallel generation (up to 8 workers or CPU count).

Each worker generates a subset of conversations with a different seed offset,

ensuring first_prompt_tokens applies correctly to turn 0 of every conversation.

Usage:

generate_turn_dataset \

--model RedHatAI/NVIDIA-Nemotron-3-Ultra-550B-A55B-FP8-block \

--prompt-tokens 1500 --output-tokens 425 \

--first-prompt-tokens 160000 \

--prefix-tokens 3000 --prefix-count 1 \

--turns 540 --rows 100 --seed 42 \

--output /mnt/storage/datasets/nemotron-agentic.jsonl

"""

import argparse

import array

import json

import multiprocessing

import os

import time

def _build_config(args):

"""Build guidellm SyntheticTextDataArgs from CLI args."""

from guidellm.data.deserializers.synthetic import (

SyntheticTextDataArgs,

SyntheticTextPrefixBucketConfig,

)

kwargs = {

'kind': 'synthetic_text',

'prompt_tokens': args.prompt_tokens,

'output_tokens': args.output_tokens,

'turns': args.turns,

}

for cli_attr, config_key in [

('prompt_tokens_stdev', 'prompt_tokens_stdev'),

('prompt_tokens_min', 'prompt_tokens_min'),

('prompt_tokens_max', 'prompt_tokens_max'),

('output_tokens_stdev', 'output_tokens_stdev'),

('output_tokens_min', 'output_tokens_min'),

('output_tokens_max', 'output_tokens_max'),

('first_prompt_tokens', 'first_prompt_tokens'),

('first_prompt_tokens_stdev', 'first_prompt_tokens_stdev'),

('first_prompt_tokens_min', 'first_prompt_tokens_min'),

('first_prompt_tokens_max', 'first_prompt_tokens_max'),

('first_output_tokens', 'first_output_tokens'),

('first_output_tokens_stdev', 'first_output_tokens_stdev'),

]:

val = getattr(args, cli_attr, None)

if val:

kwargs[config_key] = val

if args.prefix_tokens > 0:

kwargs['prefix_buckets'] = [

SyntheticTextPrefixBucketConfig(

bucket_weight=100,

prefix_count=args.prefix_count,

prefix_tokens=args.prefix_tokens,

)

]

return SyntheticTextDataArgs(**kwargs)

def _worker_generate(worker_args):

"""Worker function: generate a chunk of conversations."""

worker_id, model_name, config_dict, num_rows, start_idx, seed = worker_args

import sys

print(f"Worker {worker_id}: generating {num_rows} conversations (idx {start_idx}-{start_idx + num_rows - 1})...",

file=sys.stderr, flush=True)

from guidellm.data.deserializers.synthetic import (

SyntheticTextDataArgs,

SyntheticTextDataset,

SyntheticTextPrefixBucketConfig,

)

from transformers import AutoTokenizer

if 'prefix_buckets' in config_dict and config_dict['prefix_buckets']:

config_dict['prefix_buckets'] = [

SyntheticTextPrefixBucketConfig(**pb) for pb in config_dict['prefix_buckets']

]

config = SyntheticTextDataArgs(**config_dict)

tokenizer = AutoTokenizer.from_pretrained(model_name)

ds = SyntheticTextDataset(config=config, processor=tokenizer, random_seed=seed)

results = []

count = 0

progress_interval = max(num_rows // 5, 1)

for sample in ds:

results.append(json.dumps(sample))

count += 1

if count % progress_interval == 0:

print(f"Worker {worker_id}: {count}/{num_rows}", file=sys.stderr, flush=True)

if count >= num_rows:

break

print(f"Worker {worker_id}: done ({count} conversations)", file=sys.stderr, flush=True)

return results

CORPUS_PATHS = ['/app/corpus/wikitext-103.txt', '/mnt/storage/corpus/wikitext-103.txt']

# Full tokenized corpus, shared with fork workers via copy-on-write inheritance.

# Stored as a compact array('I') so 120M token ids use ~480MB instead of ~4.3GB

# as Python int objects. Set by the parent in generate_corpus_turns BEFORE the

# Pool is created. NEVER pass this through pool.map args: pickling it into every

# worker reconstructs per-worker copies that OOM the pod (24Gi cap, 8 workers).

_CORPUS_TOKENS = None

def _find_corpus():

for path in CORPUS_PATHS:

if os.path.exists(path):

return path

import sys as _sys

print("ERROR: corpus not found", file=_sys.stderr, flush=True)

_sys.exit(1)

def _corpus_window(tokenizer, tokens, start, length):

"""Cut an exact-length window from tokenized corpus."""

end = start + length

for _ in range(8):

if end <= start or end > len(tokens):

return None

text = tokenizer.decode(tokens[start:end], skip_special_tokens=False, clean_up_tokenization_spaces=False)

actual = len(tokenizer.encode(text, add_special_tokens=False))

if actual == length:

return text

end += length - actual

return None

def _corpus_turn_worker(worker_args):

"""Worker: build conversations from corpus windows, streaming to its own file."""

worker_id, num_rows, start_idx, model_name, prompt_tokens, output_tokens, turns, \

first_prompt_tokens, prefix_text, corpus_tokens_slice_start, stdev_args, output_path = worker_args

import sys, random

from transformers import AutoTokenizer

global _CORPUS_TOKENS

corpus_tokens = _CORPUS_TOKENS

print(f"Worker {worker_id}: building {num_rows} conversations...", file=sys.stderr, flush=True)

hf_home = os.environ.get('HF_HOME', '/mnt/storage/.cache/huggingface')

hf_token = os.environ.get('HF_TOKEN')

tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True, cache_dir=hf_home, token=hf_token)

isl_stdev = stdev_args.get('isl_stdev', 0) or 0

isl_min = stdev_args.get('isl_min')

isl_max = stdev_args.get('isl_max')

osl_stdev = stdev_args.get('osl_stdev', 0) or 0

osl_min = stdev_args.get('osl_min')

osl_max = stdev_args.get('osl_max')

fp_stdev = stdev_args.get('fp_stdev', 0) or 0

fp_min = stdev_args.get('fp_min')

fp_max = stdev_args.get('fp_max')

def _vary(base, stdev, lo, hi, rng):

if not stdev:

return base

val = int(base + rng.gauss(0, stdev))

if lo is not None:

val = max(val, lo)

else:

val = max(val, base // 4)

if hi is not None:

val = min(val, hi)

return max(10, val)

part_path = f"{output_path}.worker{worker_id}"

offset = corpus_tokens_slice_start

count = 0

prefix_len = 0

if prefix_text:

prefix_len = len(tokenizer.encode(prefix_text, add_special_tokens=False))

with open(part_path, 'w') as out:

for row in range(num_rows):

rng = random.Random(start_idx + row)

conversation = []

for t in range(turns):

if t == 0 and first_prompt_tokens:

isl = _vary(first_prompt_tokens, fp_stdev, fp_min, fp_max, rng)

else:

isl = _vary(prompt_tokens, isl_stdev, isl_min, isl_max, rng)

osl = _vary(output_tokens, osl_stdev, osl_min, osl_max, rng)

prompt = _corpus_window(tokenizer, corpus_tokens, offset, isl)

if not prompt:

offset = 0

prompt = _corpus_window(tokenizer, corpus_tokens, offset, isl)

if not prompt:

print(f"Worker {worker_id}: could not cut {isl}-token window, skipping", file=sys.stderr, flush=True)

break

if prefix_text and t == 0:

prompt = prefix_text + '\n' + prompt

conversation.append({

'prompt': prompt,

'prompt_tokens_count': isl + prefix_len,

'output_tokens_count': osl,

})

offset += isl + prompt_tokens

if conversation:

out.write(json.dumps({'conversation_turns': conversation}) + '\n')

out.flush()

count += 1

if (row + 1) % max(num_rows // 5, 1) == 0:

print(f"Worker {worker_id}: {row + 1}/{num_rows}", file=sys.stderr, flush=True)

print(f"Worker {worker_id}: done ({count} conversations)", file=sys.stderr, flush=True)

return count

def generate_corpus_turns(args):

"""Generate multi-turn conversations using corpus text."""

import sys

from transformers import AutoTokenizer

global _CORPUS_TOKENS

hf_home = os.environ.get('HF_HOME', '/mnt/storage/.cache/huggingface')

hf_token = os.environ.get('HF_TOKEN')

first_isl = args.first_prompt_tokens or args.prompt_tokens

tokens_per_conv = first_isl + (args.turns - 1) * args.prompt_tokens

needed = tokens_per_conv * args.rows * 2

print(f"Corpus mode: {args.turns} turns, first={first_isl}, rest={args.prompt_tokens}, ~{tokens_per_conv} tokens/conv", file=sys.stderr, flush=True)

corpus_path = _find_corpus()

print(f"Loading corpus from {corpus_path}...", file=sys.stderr, flush=True)

tokenizer = AutoTokenizer.from_pretrained(args.model, trust_remote_code=True, cache_dir=hf_home, token=hf_token)

corpus_tokens = array.array('I')

with open(corpus_path, 'r', encoding='utf-8') as f:

while len(corpus_tokens) < needed:

chunk = f.read(10_000_000)

if not chunk:

break

corpus_tokens.extend(tokenizer.encode(chunk, add_special_tokens=False))

print(f" tokenized {len(corpus_tokens):,} tokens...", file=sys.stderr, flush=True)

print(f"Corpus: {len(corpus_tokens):,} tokens", file=sys.stderr, flush=True)

if needed > len(corpus_tokens):

print(f"WARNING: needed ~{needed:,} tokens but corpus has only {len(corpus_tokens):,}; "

f"windows will wrap/reuse corpus content", file=sys.stderr, flush=True)

prefix_text = None

if args.prefix_tokens > 0:

prefix_text = _corpus_window(tokenizer, corpus_tokens, 0, args.prefix_tokens)

if prefix_text:

print(f"Shared prefix from corpus: {args.prefix_tokens} tokens", file=sys.stderr, flush=True)

num_workers = min(multiprocessing.cpu_count(), 8, args.rows)

chunk_size = args.rows // num_workers

remainder = args.rows % num_workers

stdev_args = {

'isl_stdev': args.prompt_tokens_stdev,

'isl_min': args.prompt_tokens_min,

'isl_max': args.prompt_tokens_max,

'osl_stdev': args.output_tokens_stdev,

'osl_min': args.output_tokens_min,

'osl_max': args.output_tokens_max,

'fp_stdev': args.first_prompt_tokens_stdev,

'fp_min': args.first_prompt_tokens_min,

'fp_max': args.first_prompt_tokens_max,

}

# Share the tokenized corpus with workers via fork COW inheritance (set the

# global BEFORE creating the Pool). Passing it in worker_args would pickle a

# copy into every worker and blow the pod memory limit.

_CORPUS_TOKENS = corpus_tokens

worker_args = []

start_idx = 0

corpus_offset = args.prefix_tokens * 2 if prefix_text else 0

for w in range(num_workers):

n = chunk_size + (1 if w < remainder else 0)

worker_args.append((

w, n, start_idx, args.model, args.prompt_tokens, args.output_tokens,

args.turns, args.first_prompt_tokens, prefix_text,

corpus_offset, stdev_args, args.output

))

corpus_offset += n * tokens_per_conv * 2

start_idx += n

print(f"Using {num_workers} workers for {args.rows} conversations...", file=sys.stderr, flush=True)

start = time.time()

with multiprocessing.Pool(num_workers) as pool:

pool.map(_corpus_turn_worker, worker_args)

os.makedirs(os.path.dirname(args.output) or '.', exist_ok=True)

total = 0

with open(args.output, 'w') as f:

f.write(json.dumps(_build_turn_meta(args)) + '\n')

for w in range(num_workers):

part_path = f"{args.output}.worker{w}"

with open(part_path, 'r') as part:

for line in part:

f.write(line)

total += 1

os.remove(part_path)

elapsed = time.time() - start

file_size = os.path.getsize(args.output)

print(f"Generation complete: {total} conversations in {elapsed:.1f}s ({file_size / 1024 / 1024:.1f} MB)", file=sys.stderr, flush=True)

print(f"Reproduce with: generate_turn_dataset --reproduce {args.output} --output <new_path>", file=sys.stderr, flush=True)

def _build_turn_meta(args):

"""Build metadata dict from all multi-turn generation parameters."""

return {

'_meta': True,

'type': 'multi_turn',

'model': args.model,

'prompt_tokens': args.prompt_tokens,

'output_tokens': args.output_tokens,

'prompt_tokens_stdev': args.prompt_tokens_stdev,

'prompt_tokens_min': args.prompt_tokens_min,

'prompt_tokens_max': args.prompt_tokens_max,

'output_tokens_stdev': args.output_tokens_stdev,

'output_tokens_min': args.output_tokens_min,

'output_tokens_max': args.output_tokens_max,

'first_prompt_tokens': args.first_prompt_tokens,

'first_prompt_tokens_stdev': args.first_prompt_tokens_stdev,

'first_prompt_tokens_min': args.first_prompt_tokens_min,

'first_prompt_tokens_max': args.first_prompt_tokens_max,

'first_output_tokens': args.first_output_tokens,

'first_output_tokens_stdev': args.first_output_tokens_stdev,

'prefix_tokens': args.prefix_tokens,

'prefix_count': args.prefix_count,

'turns': args.turns,

'rows': args.rows,

'seed': args.seed,

'use_corpus': getattr(args, 'use_corpus', False),

}

def main():

parser = argparse.ArgumentParser(description='Generate multi-turn conversation dataset')

parser.add_argument('--model', default=None, help='HuggingFace model for tokenizer')

parser.add_argument('--prompt-tokens', type=int, default=None, help='Average prompt tokens per turn')

parser.add_argument('--output-tokens', type=int, default=None, help='Average output tokens per turn')

parser.add_argument('--prompt-tokens-stdev', type=int, default=0)

parser.add_argument('--prompt-tokens-min', type=int, default=None)

parser.add_argument('--prompt-tokens-max', type=int, default=None)

parser.add_argument('--output-tokens-stdev', type=int, default=0)

parser.add_argument('--output-tokens-min', type=int, default=None)

parser.add_argument('--output-tokens-max', type=int, default=None)

parser.add_argument('--first-prompt-tokens', type=int, default=None, help='First turn prompt override')

parser.add_argument('--first-prompt-tokens-stdev', type=int, default=None)

parser.add_argument('--first-prompt-tokens-min', type=int, default=None)

parser.add_argument('--first-prompt-tokens-max', type=int, default=None)

parser.add_argument('--first-output-tokens', type=int, default=None)

parser.add_argument('--first-output-tokens-stdev', type=int, default=None)

parser.add_argument('--prefix-tokens', type=int, default=0, help='Shared system prompt tokens')

parser.add_argument('--prefix-count', type=int, default=1, help='Number of unique prefixes')

parser.add_argument('--turns', type=int, default=1, help='Turns per conversation')

parser.add_argument('--rows', type=int, default=100, help='Number of conversations to generate')

parser.add_argument('--seed', type=int, default=42)

parser.add_argument('--output', required=True, help='Output JSONL file path')

parser.add_argument('--use-corpus', action='store_true', default=False, help='Use real prose from bundled corpus')

parser.add_argument('--reproduce', type=str, default=None, help='Path to existing dataset — reproduce from its embedded metadata')

args = parser.parse_args()

import sys

if args.reproduce:

import base64 as _b64

meta = None

try:

decoded = _b64.b64decode(args.reproduce).decode('utf-8')

meta = json.loads(decoded)

print("Reproducing from seed", file=sys.stderr, flush=True)

except Exception:

pass

if not meta and os.path.isfile(args.reproduce):

with open(args.reproduce, 'r') as f:

first = f.readline().strip()

meta = json.loads(first) if first else {}

if not meta.get('_meta'):

meta = None

else:

print(f"Reproducing from file: {args.reproduce}", file=sys.stderr, flush=True)

if not meta:

print(f"ERROR: invalid seed or file: {args.reproduce}", file=sys.stderr, flush=True)

sys.exit(1)

# Map seed fields to args (handle both UI seed format and file metadata format)

field_map = {

'model': 'model', 'prompt_tokens': 'prompt_tokens', 'output_tokens': 'output_tokens',

'isl': 'prompt_tokens', 'osl': 'output_tokens',

'isl_stdev': 'prompt_tokens_stdev', 'osl_stdev': 'output_tokens_stdev',

'prompt_tokens_stdev': 'prompt_tokens_stdev', 'prompt_tokens_min': 'prompt_tokens_min',

'prompt_tokens_max': 'prompt_tokens_max', 'output_tokens_stdev': 'output_tokens_stdev',

'output_tokens_min': 'output_tokens_min', 'output_tokens_max': 'output_tokens_max',

'first_prompt_tokens': 'first_prompt_tokens', 'first_prompt_tokens_stdev': 'first_prompt_tokens_stdev',

'first_prompt_tokens_min': 'first_prompt_tokens_min', 'first_prompt_tokens_max': 'first_prompt_tokens_max',

'first_output_tokens': 'first_output_tokens', 'first_output_tokens_stdev': 'first_output_tokens_stdev',

'prefix_tokens': 'prefix_tokens', 'prefix_count': 'prefix_count',

'turns': 'turns', 'rows': 'rows', 'seed': 'seed', 'use_corpus': 'use_corpus',

}

for key, attr in field_map.items():

if meta.get(key) is not None and (getattr(args, attr, None) is None or attr != 'model'):

setattr(args, attr, meta[key])

if not args.seed:

args.seed = 42

if not args.rows:

args.rows = 100

if not args.model or not args.prompt_tokens or not args.output_tokens:

parser.error("--model, --prompt-tokens, and --output-tokens are required (or use --reproduce)")

print(f"Generating multi-turn dataset: {args.rows} conversations, {args.turns} turns each", file=sys.stderr, flush=True)

print(f"Model: {args.model}", file=sys.stderr, flush=True)

print(f"Prompt: mean={args.prompt_tokens}, stdev={args.prompt_tokens_stdev}", file=sys.stderr, flush=True)

if args.first_prompt_tokens:

print(f"First turn: mean={args.first_prompt_tokens}, stdev={args.first_prompt_tokens_stdev}", file=sys.stderr, flush=True)

if args.prefix_tokens:

print(f"Prefix: {args.prefix_tokens} tokens, {args.prefix_count} unique", file=sys.stderr, flush=True)

if getattr(args, 'use_corpus', False):

generate_corpus_turns(args)

return

config = _build_config(args)

config_dict = config.model_dump()

num_workers = min(multiprocessing.cpu_count(), 8)

if args.rows < num_workers:

num_workers = args.rows

chunk_size = args.rows // num_workers

remainder = args.rows % num_workers

worker_args = []

start_idx = 0

for w in range(num_workers):

n = chunk_size + (1 if w < remainder else 0)

worker_seed = args.seed + w * 10000

worker_args.append((w, args.model, config_dict, n, start_idx, worker_seed))

start_idx += n

print(f"Using {num_workers} workers for {args.rows} conversations...", file=sys.stderr, flush=True)

os.makedirs(os.path.dirname(args.output) or '.', exist_ok=True)

start = time.time()

with multiprocessing.Pool(num_workers) as pool:

chunks = pool.map(_worker_generate, worker_args)

with open(args.output, 'w') as f:

f.write(json.dumps(_build_turn_meta(args)) + '\n')

total = 0

for chunk in chunks:

for line in chunk:

f.write(line + '\n')

total += 1

elapsed = time.time() - start

file_size = os.path.getsize(args.output)

rate = total / elapsed if elapsed > 0 else 0

print(f"Generation complete: {total} conversations in {elapsed:.1f}s ({rate:.1f}/s, {file_size / 1024 / 1024:.1f} MB)",

file=sys.stderr, flush=True)

print(f"Reproduce with: generate_turn_dataset --reproduce {args.output} --output <new_path>", file=sys.stderr, flush=True)

if __name__ == '__main__':

main()