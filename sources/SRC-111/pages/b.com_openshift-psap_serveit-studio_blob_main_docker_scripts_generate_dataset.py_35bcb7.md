source: https://github.com/openshift-psap/serveit-studio/blob/main/docker/scripts/generate_dataset.py

-
[Notifications](https://github.com/login?return_to=%2Fopenshift-psap%2Fserveit-studio)You must be signed in to change notification settings -
[Fork 1](https://github.com/login?return_to=%2Fopenshift-psap%2Fserveit-studio)


## Expand file tree

/

Copy path# generate_dataset.py

More file actions

725 lines (614 loc) · 31.3 KB

/

Copy path# generate_dataset.py

## File metadata and controls

725 lines (614 loc) · 31.3 KB

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

486

487

488

489

490

491

492

493

494

495

496

497

498

499

500

501

502

503

504

505

506

507

508

509

510

511

512

513

514

515

516

517

518

519

520

521

522

523

524

525

526

527

528

529

530

531

532

533

534

535

536

537

538

539

540

541

542

543

544

545

546

547

548

549

550

551

552

553

554

555

556

557

558

559

560

561

562

563

564

565

566

567

568

569

570

571

572

573

574

575

576

577

578

579

580

581

582

583

584

585

586

587

588

589

590

591

592

593

594

595

596

597

598

599

600

601

602

603

604

605

606

607

608

609

610

611

612

613

614

615

616

617

618

619

620

621

622

623

624

625

626

627

628

629

630

631

632

633

634

635

636

637

638

639

640

641

642

643

644

645

646

647

648

649

650

651

652

653

654

655

656

657

658

659

660

661

662

663

664

665

666

667

668

669

670

671

672

673

674

675

676

677

678

679

680

681

682

683

684

685

686

687

688

689

690

691

692

693

694

695

696

697

698

699

700

701

702

703

704

705

706

707

708

709

710

711

712

713

714

715

716

717

718

719

720

721

722

723

724

725

#!/usr/bin/env python3

"""Generate benchmark datasets for ServeIt Studio.

Usage:

generate_dataset.py --model MODEL --isl ISL --osl OSL --seed SEED --rows ROWS --output PATH [--mode random|cache|corpus] [--hit-pct PCT] [--isl-stdev S] [--osl-stdev S]

Modes:

random — synthetic word-salad prompts (fast, tokenizer-aware)

cache — shared prefix with hit_pct cache hits

prefix_group — N groups with shared prefix + unique suffix

corpus — contiguous prose windows from bundled wikitext-103 corpus;

meaningful text for speculative decoding acceptance measurement

"""

import argparse

import json

import multiprocessing

import os

import random

import sys

import time

def _load_tokenizer(model_name):

"""Load tokenizer and extract vocab. Returns (tokenizer, vocab) or (None, None)."""

try:

from transformers import AutoTokenizer

hf_home = os.environ.get('HF_HOME', '/mnt/storage/.cache/huggingface')

hf_token = os.environ.get('HF_TOKEN')

tokenizer = AutoTokenizer.from_pretrained(

model_name, trust_remote_code=True,

cache_dir=hf_home, token=hf_token

)

vocab = [t for t in tokenizer.get_vocab().keys()

if len(t) > 2 and t.isascii() and t.isalpha()]

if len(vocab) < 500:

return None, None

return tokenizer, vocab

except Exception:

return None, None

def _make_prompt(length_tokens, rng_instance, tokenizer, vocab):

"""Generate a prompt of approximately length_tokens tokens."""

if vocab and tokenizer:

target = int(length_tokens * 1.1)

words = [rng_instance.choice(vocab) for _ in range(target)]

text = ' '.join(words)

tokens = tokenizer.encode(text, add_special_tokens=False)

while len(tokens) < length_tokens:

extra = length_tokens - len(tokens)

words = [rng_instance.choice(vocab) for _ in range(extra + 10)]

text += ' ' + ' '.join(words)

tokens = tokenizer.encode(text, add_special_tokens=False)

if len(tokens) > length_tokens:

text = tokenizer.decode(tokens[:length_tokens], skip_special_tokens=True)

else:

words = []

for _ in range(int(length_tokens * 1.3)):

wlen = rng_instance.randint(3, 10)

words.append(''.join(rng_instance.choices('abcdefghijklmnopqrstuvwxyz', k=wlen)))

text = ' '.join(words)

return text

def _generate_random_chunk(chunk_args):

"""Generate a chunk of random rows in a worker process."""

start_idx, count, seed, isl, osl, isl_stdev, osl_stdev, model_name = chunk_args

pid = os.getpid()

tokenizer, vocab = _load_tokenizer(model_name)

print(f"Worker {pid}: generating {count} rows (idx {start_idx}-{start_idx+count-1})...", file=sys.stderr, flush=True)

rows = []

for i in range(count):

rng = random.Random(seed + start_idx + i + 1)

row_isl = isl + int(rng.random() * isl_stdev) if isl_stdev > 0 else isl

row_osl = osl + int(rng.random() * osl_stdev) if osl_stdev > 0 else osl

prompt = _make_prompt(row_isl, rng, tokenizer, vocab)

rows.append(json.dumps({'prompt': prompt, 'output_tokens_count': row_osl}))

if (i + 1) % 2000 == 0:

print(f"Worker {pid}: {i+1}/{count}", file=sys.stderr, flush=True)

print(f"Worker {pid}: done ({count} rows)", file=sys.stderr, flush=True)

return rows

def generate_random_parallel(args):

"""Generate random dataset using multiprocessing."""

num_workers = min(multiprocessing.cpu_count(), 8)

chunk_size = args.rows // num_workers

remainder = args.rows % num_workers

chunks = []

offset = 0

for w in range(num_workers):

n = chunk_size + (1 if w < remainder else 0)

chunks.append((offset, n, args.seed, args.isl, args.osl, args.isl_stdev, args.osl_stdev, args.model))

offset += n

print(f"Using {num_workers} workers for {args.rows} rows...", file=sys.stderr, flush=True)

t0 = time.time()

with multiprocessing.Pool(num_workers) as pool:

results = pool.map(_generate_random_chunk, chunks)

rows = []

for chunk_rows in results:

rows.extend(chunk_rows)

elapsed = time.time() - t0

print(f"Generation complete: {len(rows)} rows in {elapsed:.1f}s ({len(rows)/max(elapsed,0.1):.0f} rows/s)", file=sys.stderr, flush=True)

return rows

_SHARED_CORPUS = None # Global for fork-inherited corpus tokens

def _generate_cache_chunk(chunk_args):

"""Generate a chunk of cache dataset rows in a worker process."""

start_idx, count, seed, isl, osl, isl_stdev, osl_stdev, model_name, shared_prompt, hit_count, unique_count, use_corpus = chunk_args

pid = os.getpid()

tokenizer, vocab = _load_tokenizer(model_name)

corpus_tokens = _SHARED_CORPUS if use_corpus else None

print(f"Worker {pid}: generating {count} cache rows ({hit_count} hits, {unique_count} unique, ISL {isl}+{isl_stdev})...", file=sys.stderr, flush=True)

if tokenizer:

shared_toks = tokenizer.encode(shared_prompt, add_special_tokens=False)

else:

shared_toks = None

max_isl = isl + (int(isl_stdev) if isl_stdev > 0 else 0)

rows = []

for i in range(hit_count):

rng = random.Random(seed + start_idx + i)

row_isl = isl + int(rng.random() * isl_stdev) if isl_stdev > 0 else isl

row_osl = osl + int(rng.random() * osl_stdev) if osl_stdev > 0 else osl

if isl_stdev > 0 and row_isl < max_isl:

if shared_toks is not None:

prompt = tokenizer.decode(shared_toks[:row_isl], skip_special_tokens=True)

else:

words = shared_prompt.split()

cut = max(1, int(len(words) * row_isl / max_isl))

prompt = ' '.join(words[:cut])

else:

prompt = shared_prompt

rows.append(json.dumps({'prompt': prompt, 'output_tokens_count': row_osl}))

for i in range(unique_count):

rng = random.Random(seed + start_idx + hit_count + i + 1)

row_isl = isl + int(rng.random() * isl_stdev) if isl_stdev > 0 else isl

row_osl = osl + int(rng.random() * osl_stdev) if osl_stdev > 0 else osl

if corpus_tokens is not None and tokenizer:

offset = ((start_idx + hit_count + i) * max_isl * 3) % max(1, len(corpus_tokens) - row_isl)

prompt = _corpus_window(tokenizer, corpus_tokens, offset, row_isl)

if not prompt:

prompt = _make_prompt(row_isl, rng, tokenizer, vocab)

else:

prompt = _make_prompt(row_isl, rng, tokenizer, vocab)

rows.append(json.dumps({'prompt': prompt, 'output_tokens_count': row_osl}))

if (i + 1) % 2000 == 0:

print(f"Worker {pid}: {i+1}/{unique_count} unique rows", file=sys.stderr, flush=True)

print(f"Worker {pid}: done ({count} rows)", file=sys.stderr, flush=True)

return rows

def generate_cache_parallel(args):

"""Generate cache dataset using multiprocessing."""

num_workers = min(multiprocessing.cpu_count(), 8)

max_isl = args.isl + (int(args.isl_stdev) if args.isl_stdev > 0 else 0)

if getattr(args, 'use_corpus', False):

needed = min(5_000_000, max_isl * min(args.rows, 500) * 2)

corpus_tok, corpus_tokens = _load_corpus_tokens(args.model, needed)

shared_prompt = _corpus_window(corpus_tok, corpus_tokens, 0, max_isl)

if not shared_prompt:

print("ERROR: could not cut shared prompt from corpus", file=sys.stderr, flush=True)

sys.exit(1)

print(f"Shared prompt from corpus ({len(shared_prompt)} chars, {max_isl} tokens)", file=sys.stderr, flush=True)

else:

tokenizer, vocab = _load_tokenizer(args.model)

shared_rng = random.Random(args.seed)

shared_prompt = _make_prompt(max_isl, shared_rng, tokenizer, vocab)

print(f"Shared prompt generated ({len(shared_prompt)} chars, max ISL {max_isl})", file=sys.stderr, flush=True)

total_hits = int(args.rows * args.hit_pct / 100)

chunk_size = args.rows // num_workers

remainder = args.rows % num_workers

uc = getattr(args, 'use_corpus', False)

# Distribute hits round-robin across workers for exact count

worker_hits = [0] * num_workers

worker_sizes = []

for w in range(num_workers):

worker_sizes.append(chunk_size + (1 if w < remainder else 0))

for i in range(total_hits):

worker_hits[i % num_workers] += 1

# Clamp hits to worker size

for w in range(num_workers):

worker_hits[w] = min(worker_hits[w], worker_sizes[w])

chunks = []

offset = 0

for w in range(num_workers):

n = worker_sizes[w]

wh = worker_hits[w]

wu = n - wh

chunks.append((offset, n, args.seed, args.isl, args.osl, args.isl_stdev, args.osl_stdev, args.model, shared_prompt, wh, wu, uc))

offset += n

global _SHARED_CORPUS

if uc:

_SHARED_CORPUS = corpus_tokens

print(f"Using {num_workers} workers for {args.rows} rows...", file=sys.stderr, flush=True)

t0 = time.time()

with multiprocessing.Pool(num_workers) as pool:

results = pool.map(_generate_cache_chunk, chunks)

_SHARED_CORPUS = None

rows = []

for chunk_rows in results:

rows.extend(chunk_rows)

random.Random(args.seed + 999).shuffle(rows)

elapsed = time.time() - t0

print(f"Generation complete: {len(rows)} rows in {elapsed:.1f}s ({len(rows)/max(elapsed,0.1):.0f} rows/s)", file=sys.stderr, flush=True)

return rows

def _generate_prefix_group_chunk(chunk_args):

"""Generate a chunk of prefix-group rows: shared prefix + unique suffix per row."""

start_idx, count, seed, isl, isl_stdev, osl, osl_stdev, prefix_pct, model_name, group_prefixes, use_corpus = chunk_args

pid = os.getpid()

tokenizer, vocab = _load_tokenizer(model_name)

corpus_tokens = _SHARED_CORPUS if use_corpus else None

num_groups = len(group_prefixes)

print(f"Worker {pid}: generating {count} prefix-group rows ({num_groups} groups, {prefix_pct}% prefix, ISL {isl}+{isl_stdev})...", file=sys.stderr, flush=True)

rows = []

for i in range(count):

rng = random.Random(seed + start_idx + i + 1)

row_isl = isl + int(rng.random() * isl_stdev) if isl_stdev > 0 else isl

row_prefix_tokens = max(1, int(row_isl * prefix_pct / 100))

row_suffix_tokens = max(1, row_isl - row_prefix_tokens)

group_idx = (start_idx + i) % num_groups

full_prefix = group_prefixes[group_idx]

if tokenizer:

prefix_toks = tokenizer.encode(full_prefix, add_special_tokens=False)[:row_prefix_tokens]

prefix = tokenizer.decode(prefix_toks, skip_special_tokens=True)

else:

words = full_prefix.split()

prefix = ' '.join(words[:max(1, int(row_prefix_tokens * 0.8))])

if corpus_tokens is not None and tokenizer:

offset = ((start_idx + i) * isl * 3) % max(1, len(corpus_tokens) - row_suffix_tokens)

suffix = _corpus_window(tokenizer, corpus_tokens, offset, row_suffix_tokens)

if not suffix:

suffix = _make_prompt(row_suffix_tokens, rng, tokenizer, vocab)

else:

suffix = _make_prompt(row_suffix_tokens, rng, tokenizer, vocab)

prompt = prefix + '\n' + suffix

row_osl = osl + int(rng.random() * osl_stdev) if osl_stdev > 0 else osl

rows.append(json.dumps({'prompt': prompt, 'output_tokens_count': row_osl}))

if (i + 1) % 2000 == 0:

print(f"Worker {pid}: {i+1}/{count}", file=sys.stderr, flush=True)

print(f"Worker {pid}: done ({count} rows)", file=sys.stderr, flush=True)

return rows

def _corpus_prefix_group_worker(worker_args):

"""Worker: build prefix-group rows from fork-shared corpus, streaming to a part file."""

(worker_id, start_idx, count, temp_path, seed, isl, isl_stdev, osl, osl_stdev,

prefix_pct, num_groups, max_isl, group_prefixes, model_name) = worker_args

os.environ['TOKENIZERS_PARALLELISM'] = 'false'

corpus_tokens = _SHARED_CORPUS

tokenizer = _bare_tokenizer(model_name)

group_prefix_toks = [tokenizer.encode(gp, add_special_tokens=False) for gp in group_prefixes]

print(f"Worker {worker_id}: {count} prefix-group rows → {os.path.basename(temp_path)}...", file=sys.stderr, flush=True)

written = 0

with open(temp_path, 'w') as f:

for j in range(count):

i = start_idx + j

rng = random.Random(seed + i + 1)

row_isl = isl + int(rng.random() * isl_stdev) if isl_stdev > 0 else isl

row_osl = osl + int(rng.random() * osl_stdev) if osl_stdev > 0 else osl

row_prefix_tokens = max(1, int(row_isl * prefix_pct / 100))

row_suffix_tokens = max(1, row_isl - row_prefix_tokens)

group_idx = i % num_groups

prefix = tokenizer.decode(group_prefix_toks[group_idx][:row_prefix_tokens], skip_special_tokens=True)

soffset = (i * max_isl * 3) % max(1, len(corpus_tokens) - row_suffix_tokens)

suffix = _corpus_window(tokenizer, corpus_tokens, soffset, row_suffix_tokens)

if not suffix:

suffix = tokenizer.decode(corpus_tokens[soffset:soffset + row_suffix_tokens], skip_special_tokens=True)

f.write(json.dumps({'prompt': prefix + '\n' + suffix, 'output_tokens_count': row_osl}) + '\n')

written += 1

if (j + 1) % 2000 == 0:

print(f"Worker {worker_id}: {j + 1}/{count}", file=sys.stderr, flush=True)

print(f"Worker {worker_id}: done ({written} rows)", file=sys.stderr, flush=True)

return temp_path, written

def generate_prefix_group_parallel(args):

"""Generate prefix-group dataset: N groups, each with a shared prefix + unique suffix per row."""

num_groups = args.prefix_groups

prefix_pct = args.hit_pct if args.hit_pct > 0 else 60

max_isl = args.isl + (int(args.isl_stdev) if args.isl_stdev > 0 else 0)

max_prefix_tokens = max(1, int(max_isl * prefix_pct / 100))

use_corpus = getattr(args, 'use_corpus', False)

if use_corpus:

# Corpus mode: tokenize once in parent, fork-share via _SHARED_CORPUS, and let each

# worker stream its rows to a part file on the PVC. Memory stays flat regardless of row

# count (no 7GB in-memory list), and generation is parallel across workers.

global _SHARED_CORPUS

needed = min(60_000_000, max_isl * min(args.rows, 2000) * 2)

needed = max(needed, max_prefix_tokens * (num_groups + 1) * 3)

corpus_tok, corpus_tokens = _load_corpus_tokens(args.model, needed)

print(f"Generating {num_groups} group prefixes from corpus ({max_prefix_tokens} tokens each)...", file=sys.stderr, flush=True)

group_prefixes = []

for g in range(num_groups):

goffset = g * max_prefix_tokens * 3

prefix = _corpus_window(corpus_tok, corpus_tokens, goffset, max_prefix_tokens)

if not prefix:

grng = random.Random(args.seed + g * 10000)

vocab = [t for t in corpus_tok.get_vocab().keys() if len(t) > 2 and t.isascii() and t.isalpha()]

prefix = _make_prompt(max_prefix_tokens, grng, corpus_tok, vocab)

group_prefixes.append(prefix)

num_workers = min(multiprocessing.cpu_count(), 8, args.rows)

chunk_size = args.rows // num_workers

remainder = args.rows % num_workers

worker_args = []

start_idx = 0

for w in range(num_workers):

n = chunk_size + (1 if w < remainder else 0)

worker_args.append((

w, start_idx, n, f'{args.output}.part{w}', args.seed,

args.isl, args.isl_stdev, args.osl, args.osl_stdev,

prefix_pct, num_groups, max_isl, group_prefixes, args.model,

))

start_idx += n

_SHARED_CORPUS = corpus_tokens

print(f"Using {num_workers} workers (streaming to part files)...", file=sys.stderr, flush=True)

t0 = time.time()

try:

with multiprocessing.Pool(num_workers) as pool:

results = pool.map(_corpus_prefix_group_worker, worker_args)

finally:

_SHARED_CORPUS = None

total = sum(c for _, c in results)

os.makedirs(os.path.dirname(args.output) or '.', exist_ok=True)

meta = _build_meta(args)

meta['rows'] = total

_concat_parts(args.output, [wa[3] for wa in worker_args], meta)

size_mb = os.path.getsize(args.output) / (1024 * 1024)

elapsed = time.time() - t0

print(f"Generated {num_groups} group prefixes (max {max_prefix_tokens} tokens, ISL range {args.isl}-{max_isl})", file=sys.stderr, flush=True)

print(f"Generation complete: {total} rows in {elapsed:.1f}s ({total/max(elapsed,0.1):.0f} rows/s, {size_mb:.1f} MB)", file=sys.stderr, flush=True)

return None # Already written to file, skip the common write path

else:

num_workers = min(multiprocessing.cpu_count(), 8)

tokenizer, vocab = _load_tokenizer(args.model)

print(f"Generating {num_groups} group prefixes ({max_prefix_tokens} max tokens, {prefix_pct}% of ISL)...", file=sys.stderr, flush=True)

group_prefixes = []

for g in range(num_groups):

grng = random.Random(args.seed + g * 10000)

group_prefixes.append(_make_prompt(max_prefix_tokens, grng, tokenizer, vocab))

chunk_size = args.rows // num_workers

remainder = args.rows % num_workers

chunks = []

offset = 0

for w in range(num_workers):

n = chunk_size + (1 if w < remainder else 0)

chunks.append((offset, n, args.seed, args.isl, args.isl_stdev, args.osl, args.osl_stdev, prefix_pct, args.model, group_prefixes, False))

offset += n

print(f"Using {num_workers} workers for {args.rows} rows...", file=sys.stderr, flush=True)

t0 = time.time()

with multiprocessing.Pool(num_workers) as pool:

results = pool.map(_generate_prefix_group_chunk, chunks)

rows = []

for chunk_rows in results:

rows.extend(chunk_rows)

random.Random(args.seed + 999).shuffle(rows)

print(f"Generated {num_groups} group prefixes (max {max_prefix_tokens} tokens, ISL range {args.isl}-{max_isl})", file=sys.stderr, flush=True)

elapsed = time.time() - t0

print(f"Generation complete: {len(rows)} rows in {elapsed:.1f}s ({len(rows)/max(elapsed,0.1):.0f} rows/s)", file=sys.stderr, flush=True)

return rows

CORPUS_PATHS = [

'/app/corpus/wikitext-103.txt',

'/mnt/storage/corpus/wikitext-103.txt',

]

def _find_corpus():

"""Find the bundled wikitext-103 corpus file."""

for path in CORPUS_PATHS:

if os.path.exists(path):

return path

print(f"ERROR: corpus not found at any of: {CORPUS_PATHS}", file=sys.stderr, flush=True)

sys.exit(1)

def _load_corpus_tokens(model_name, min_tokens):

"""Load and tokenize enough corpus text to provide the requested tokens."""

from transformers import AutoTokenizer

hf_home = os.environ.get('HF_HOME', '/mnt/storage/.cache/huggingface')

hf_token = os.environ.get('HF_TOKEN')

tokenizer = AutoTokenizer.from_pretrained(

model_name, trust_remote_code=True,

cache_dir=hf_home, token=hf_token

)

corpus_path = _find_corpus()

print(f"Loading corpus from {corpus_path}...", file=sys.stderr, flush=True)

book_tokens = []

with open(corpus_path, 'r', encoding='utf-8') as f:

while len(book_tokens) < min_tokens:

chunk = f.read(10_000_000)

if not chunk:

break

book_tokens.extend(tokenizer.encode(chunk, add_special_tokens=False))

print(f"Corpus: {len(book_tokens):,} tokens", file=sys.stderr, flush=True)

return tokenizer, book_tokens

def _corpus_window(tokenizer, book_tokens, start, length):

"""Cut an exact-length window from the tokenized corpus."""

end = start + length

for _ in range(8):

if end <= start or end > len(book_tokens):

return None

prompt = tokenizer.decode(

book_tokens[start:end],

skip_special_tokens=False,

clean_up_tokenization_spaces=False,

)

actual = len(tokenizer.encode(prompt, add_special_tokens=False))

if actual == length:

return prompt

end += length - actual

return None

def _bare_tokenizer(model_name):

"""Load just the tokenizer (no vocab filtering) for corpus decode/encode."""

from transformers import AutoTokenizer

hf_home = os.environ.get('HF_HOME', '/mnt/storage/.cache/huggingface')

hf_token = os.environ.get('HF_TOKEN')

return AutoTokenizer.from_pretrained(

model_name, trust_remote_code=True,

cache_dir=hf_home, token=hf_token

)

def _concat_parts(output_path, part_paths, meta):

"""Stream-concatenate worker part files into the final dataset, then remove parts.

Writes the metadata line first, then copies each part in order. Streaming copy

keeps memory flat regardless of dataset size (no in-memory row list). Part files

live in the output directory, so they are guaranteed to be on the same PVC.

"""

import shutil

with open(output_path, 'w') as out:

out.write(json.dumps(meta) + '\n')

for part in part_paths:

if not os.path.exists(part):

continue

with open(part, 'r') as pf:

shutil.copyfileobj(pf, out, 1024 * 1024)

for part in part_paths:

try:

os.remove(part)

except OSError:

pass

def _corpus_worker(worker_args):

"""Worker: cut windows from the fork-shared tokenized corpus, streaming to a part file."""

worker_id, starts, temp_path, isl, osl, model_name, isl_stdev, osl_stdev, seed = worker_args

os.environ['TOKENIZERS_PARALLELISM'] = 'false'

book_tokens = _SHARED_CORPUS

tokenizer = _bare_tokenizer(model_name)

print(f"Worker {worker_id}: cutting {len(starts)} windows → {os.path.basename(temp_path)}...", file=sys.stderr, flush=True)

count = 0

skipped = 0

with open(temp_path, 'w') as f:

for idx, start in enumerate(starts):

rng = random.Random(seed + idx)

row_isl = isl

if isl_stdev > 0:

row_isl = max(isl // 4, int(isl + rng.gauss(0, isl_stdev)))

row_osl = osl

if osl_stdev > 0:

row_osl = max(osl // 4, int(osl + rng.gauss(0, osl_stdev)))

prompt = _corpus_window(tokenizer, book_tokens, start, row_isl)

if prompt:

f.write(json.dumps({

'prompt': prompt,

'prompt_tokens_count': row_isl,

'output_tokens_count': row_osl,

}) + '\n')

count += 1

else:

skipped += 1

if (idx + 1) % 2000 == 0:

print(f"Worker {worker_id}: {idx + 1}/{len(starts)}", file=sys.stderr, flush=True)

print(f"Worker {worker_id}: done ({count} windows, {skipped} skipped)", file=sys.stderr, flush=True)

return temp_path, count

def generate_corpus(args):

"""Generate dataset from bundled wikitext-103 corpus with evenly-spaced windows.

Parallel: the corpus is tokenized once in the parent and fork-shared (copy-on-write)

via _SHARED_CORPUS. Each worker streams its rows to a part file on the PVC, so memory

stays flat no matter how many rows are requested. Returns None (written directly).

"""

global _SHARED_CORPUS

# Read enough corpus to span the requested windows, capped so we never load the

# entire 130M-token corpus. Above the cap, windows just overlap more (still real prose).

needed_tokens = min(args.isl * args.rows * 2, 60_000_000)

needed_tokens = max(needed_tokens, args.isl * 4)

tokenizer, book_tokens = _load_corpus_tokens(args.model, needed_tokens)

if len(book_tokens) < args.isl:

print(f"ERROR: corpus has only {len(book_tokens)} tokens, need at least {args.isl}", file=sys.stderr, flush=True)

sys.exit(1)

max_start = len(book_tokens) - args.isl

if args.rows == 1:

starts = [0]

else:

starts = [round(i * max_start / (args.rows - 1)) for i in range(args.rows)]

stride = starts[1] - starts[0] if len(starts) > 1 else max_start

print(f"Cutting {args.rows} windows (ISL={args.isl}, stride={stride} tokens, overlap={'yes' if stride < args.isl else 'no'})",

file=sys.stderr, flush=True)

num_workers = min(multiprocessing.cpu_count(), 8, args.rows)

chunk_size = args.rows // num_workers

remainder = args.rows % num_workers

worker_args = []

offset = 0

for w in range(num_workers):

n = chunk_size + (1 if w < remainder else 0)

worker_starts = starts[offset:offset + n]

worker_args.append((w, worker_starts, f'{args.output}.part{w}', args.isl, args.osl, args.model, args.isl_stdev, args.osl_stdev, args.seed + offset))

offset += n

_SHARED_CORPUS = book_tokens

print(f"Using {num_workers} workers (streaming to part files)...", file=sys.stderr, flush=True)

t0 = time.time()

try:

with multiprocessing.Pool(num_workers) as pool:

results = pool.map(_corpus_worker, worker_args)

finally:

_SHARED_CORPUS = None

total = sum(c for _, c in results)

if total == 0:

for wa in worker_args:

try:

os.remove(wa[2])

except OSError:

pass

print("ERROR: no windows generated", file=sys.stderr, flush=True)

sys.exit(1)

os.makedirs(os.path.dirname(args.output) or '.', exist_ok=True)

meta = _build_meta(args)

meta['rows'] = total

_concat_parts(args.output, [wa[2] for wa in worker_args], meta)

elapsed = time.time() - t0

size_mb = os.path.getsize(args.output) / (1024 * 1024)

print(f"Generation complete: {total} windows in {elapsed:.1f}s ({total / max(elapsed, 0.1):.0f} rows/s, {size_mb:.1f} MB)", file=sys.stderr, flush=True)

return None

def _build_meta(args):

"""Build metadata dict from all generation parameters."""

return {

'_meta': True,

'model': args.model,

'isl': args.isl,

'osl': args.osl,

'seed': args.seed,

'rows': args.rows,

'mode': args.mode,

'hit_pct': args.hit_pct,

'prefix_tokens': args.prefix_tokens,

'prefix_groups': args.prefix_groups,

'isl_stdev': args.isl_stdev,

'osl_stdev': args.osl_stdev,

'use_corpus': getattr(args, 'use_corpus', False),

}

def _load_meta(path):

"""Read metadata from the first line of a JSONL dataset."""

with open(path, 'r') as f:

first = f.readline().strip()

if first:

meta = json.loads(first)

if meta.get('_meta'):

return meta

return None

def main():

parser = argparse.ArgumentParser(description='Generate benchmark dataset')

parser.add_argument('--model', default=None, help='HuggingFace model name')

parser.add_argument('--isl', type=int, default=None, help='Input sequence length')

parser.add_argument('--osl', type=int, default=None, help='Output sequence length')

parser.add_argument('--seed', type=int, default=None, help='Random seed')

parser.add_argument('--rows', type=int, default=None, help='Number of rows')

parser.add_argument('--output', required=True, help='Output JSONL path')

parser.add_argument('--mode', default='random', choices=['random', 'cache', 'prefix_group', 'corpus'], help='Dataset mode')

parser.add_argument('--hit-pct', type=int, default=100, help='Cache hit percentage (cache mode)')

parser.add_argument('--prefix-tokens', type=int, default=0, help='Shared prefix length in tokens (prefix_group mode)')

parser.add_argument('--prefix-groups', type=int, default=10, help='Number of prefix groups (prefix_group mode)')

parser.add_argument('--isl-stdev', type=float, default=0, help='ISL standard deviation')

parser.add_argument('--osl-stdev', type=float, default=0, help='OSL standard deviation')

parser.add_argument('--use-corpus', action='store_true', default=False, help='Use real prose from bundled corpus')

parser.add_argument('--reproduce', type=str, default=None, help='Base64 workload seed or path to existing dataset file')

args = parser.parse_args()

# Reproduce mode: decode base64 seed or read metadata from file

if args.reproduce:

meta = None

# Try base64 decode first

try:

import base64

decoded = base64.b64decode(args.reproduce).decode('utf-8')

meta = json.loads(decoded)

print("Reproducing from seed", file=sys.stderr, flush=True)

except Exception:

pass

# Fall back to file

if not meta and os.path.isfile(args.reproduce):

meta = _load_meta(args.reproduce)

if meta:

print(f"Reproducing from file: {args.reproduce}", file=sys.stderr, flush=True)

if not meta:

print(f"ERROR: invalid seed or file: {args.reproduce}", file=sys.stderr, flush=True)

sys.exit(1)

for key in ['model', 'isl', 'osl', 'seed', 'rows', 'mode', 'hit_pct',

'prefix_tokens', 'prefix_groups', 'isl_stdev', 'osl_stdev', 'use_corpus']:

if meta.get(key) is not None:

setattr(args, key.replace('-', '_'), meta.get(key))

# Infer mode from seed if not explicitly set

if args.mode == 'random' and meta.get('hit_pct') and meta['hit_pct'] > 0:

if meta.get('prefix_cache_mode') == 'multi_group' or meta.get('structured_prefix'):

args.mode = 'prefix_group'

else:

args.mode = 'cache'

elif args.mode == 'random' and meta.get('use_corpus') and not meta.get('hit_pct'):

args.mode = 'corpus'

if not args.seed:

import hashlib

seed_input = ':'.join(str(meta.get(k, '')) for k in ['model','isl','osl','isl_stdev','osl_stdev','mode','hit_pct'])

args.seed = int(hashlib.sha256(seed_input.encode()).hexdigest()[:8], 16)

if not args.rows:

args.rows = 100000

print(f"Config: model={args.model}, ISL={args.isl}, OSL={args.osl}, seed={args.seed}, "

f"mode={args.mode}, rows={args.rows}, corpus={args.use_corpus}", file=sys.stderr, flush=True)

if not args.model or not args.isl or not args.osl or args.seed is None or not args.rows:

parser.error("--model, --isl, --osl, --seed, and --rows are required (or use --reproduce)")

print(f"Generating {args.mode} dataset: {args.rows} rows, ISL={args.isl}, OSL={args.osl}, seed={args.seed}", file=sys.stderr, flush=True)

if args.mode == 'random':

rows = generate_random_parallel(args)

elif args.mode == 'corpus':

rows = generate_corpus(args)

elif args.mode == 'prefix_group':

if args.hit_pct <= 0:

args.hit_pct = 60

rows = generate_prefix_group_parallel(args)

else:

rows = generate_cache_parallel(args)

# Corpus generators stream directly to disk and return None; nothing left to write.

if rows is not None:

os.makedirs(os.path.dirname(args.output) or '.', exist_ok=True)

meta_line = json.dumps(_build_meta(args))

with open(args.output, 'w') as f:

f.write(meta_line + '\n')

f.write('\n'.join(rows) + '\n')

size_mb = os.path.getsize(args.output) / (1024 * 1024)

print(f"Generated {args.output} ({size_mb:.1f} MB)", file=sys.stderr, flush=True)

print(f"Reproduce with: generate_dataset --reproduce {args.output} --output <new_path>", file=sys.stderr, flush=True)

if __name__ == '__main__':

main()