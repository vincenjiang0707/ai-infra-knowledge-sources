#!/usr/bin/env python3
"""Scan .md files under sources/, identify un-fenced code blocks, optionally wrap.

识别规则:
  1. 4-space/tab 缩进块 (indent run) - 强信号, 验证后置到合并后
  2. 连续非空行块 (bare run) - 弱信号, 需多数行像代码
  3. <details>...</details> 内 - 放宽阈值 (≥50%), 且缩进行并入 run
  4. 合并: 相邻段 gap ≤2 空行 → 一段, 合并后复检 (失败不合并)
  5. 断点 (separator): fenced / HTML 标签 / 列表项 / 标题(#) / 引用(>) /
     表格(|) / setext 下划线 / 缩进散文续行
  6. 块首尾散文行 trim (短标签行 / 句末标点收尾行)

判定通道 (is_code_block):
  A 首行 code marker + ratio ≥ 阈值 (0.8 / 0.5 in-html)
  B 首行 shell 命令形态 + ratio ≥ 阈值 (含 PROSE_END / > 防线)
  C n≥4 + ratio ≥ 0.9
  D 语言结构特征 (go/python/rust/js)
  E key: value 行密度 ≥0.6 (yaml-ish)
  块级否决: 非注释行句末标点率 >0.4 且无结构特征 → 散文

CLI:
  --dry-run           只列, 不写
  --apply             原地修改
  --bak               apply 时额外写 .bak (默认不写, git 已兜底)
  --review            生成 review 候选文件
  --stats             末尾输出判定通道统计
  --only SRC-XXX      只处理某 SRC
  --root PATH         改 ROOT (默认 sources/)
  --force             忽略已执行记录, 全量处理

增量: apply 成功后把文件内容 sha1 记入 scrape/.fence_md_done.json;
后续运行跳过内容未变的文件 (新抓取覆盖会改变 hash → 重新处理).
"""
import argparse
import hashlib
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SOURCES = os.path.join(ROOT, 'sources')
STATE_PATH = os.path.join(ROOT, 'scrape', '.fence_md_done.json')

# 判定通道统计 (--stats)
STATS = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'reject': 0}

# 单行代码标记
CODE_MARK = re.compile(
    r'^('
    r'[{]'                              # literal {
    r'|\[='                             # [= (字面匹配, 不含裸 [ — 防 [link](url))
    r'|<>|>'                            # <> or >
    r'|"[^"]+"\s*:'                    # JSON key
    r"|'[^']+'\s*:"                    # YAML/JSON single-quote key
    r'|\d+\.\s+\w'                      # enum 1. foo
    r'|\d+\)\s+\w'                     # enum 1) foo
    r'|\d+:\s+\w'                      # dict-style 1: foo
    r'|\([\w$@]'                       # ( followed by word/$/@
    r'|\w+\s*:='                       # Go/Rust 赋值
    r'|\w+\.\w+\('                     # 方法/属性调用
    r'|^func\s|^return\s|^if\s.*\{|^for\s.*\{'  # Go/Rust 关键字
    r'|^#'                              # Python/shell 注释 (标题已被 separator 排除)
    r'|def\s|class\s|import\s|from\s|async\s|const\s|let\s|var\s'
    r'|function\s|fn\s|pub\s|struct\s|impl\s|@[\w]'
    r'|#!|Traceback|panic:'
    r'|[A-Za-z_][\w.-]*\s*=\s*\S'      # shell var: key=value
    r')'
)
# shell 风格
SHELL_MARK = re.compile(r'^(export\s|--?[A-Za-z_][\w-]*\s|=[\w]|[$>]\s?|\w+\s*=\s*\S)')
# bare 行可能代码的扩展标记 (比 CODE_MARK 宽松, 用于判定中间行).
# 注意: search() 作用于 lstrip 后的行, ^ 锚定行首.
LINE_CODE_HINT = re.compile(
    r'('
    r'[{]'                              # literal {
    r'|<[A-Za-z/!]'                     # 标签形态 <div </p <! (不含 "a < b")
    r'|"[^"]+"\s*:'
    r"|'[^']+'\s*:"
    r'|(?:\A|\w)\([\w$@]'              # foo(x / 行首(x; " (see docs)" 不命中
    r'|\w+\s*:='                       # Go/Rust 赋值
    r'|\w+\.\w+\('                     # 方法/属性调用
    r'|def\s|class\s|import\s|from\s|async\s|const\s|let\s|var\s'
    r'|function\s|fn\s|pub\s|struct\s|impl\s'
    r'|^@[\w.]'                         # 行首装饰器 (mid-line @ 是邮箱/mention)
    r'|#!|Traceback|panic:'
    r'|export\s'
    r'|^--?[A-Za-z_]\w*'                 # shell flag (行首)
    r'|\$\w+|\${\w'                     # shell var
    r'|[A-Z_][A-Z0-9_]+\s*=\s*\S'      # ALL_CAPS=val
    r'|[a-z][a-z0-9_-]*\s+.*\\$'       # shell 多行续行 (vllm serve ...\)
    r'|^[}\]]'                          # JSON/YAML 闭合 (行首)
    r'|if\s.*\{|for\s.*\{|\bfunc\s|\breturn\s'  # Go/Rust 关键字
    r'|^if\s.*:|^elif\s|^else\s*:|^for\s.*:|^while\s.*:|^except\s|^finally\s|^with\s|^try\s|^yield\s|^raise\s'  # Python 关键字
    r'|\w+\]?\s*=\s*\S'                # 字典/属性赋值 (base['x'] = ...)
    r'|\+=|-=|\*=|/=|%=|\*\*='          # 增强赋值 (page += 1)
    r'|^(pip3?|python3?|uv|npm|npx|yarn|pnpm|cargo|go|docker|podman|kubectl|helm|git|curl|wget|make|cd|conda|mamba|brew|apt(?:-get)?|sudo|bash|sh|zsh|source|echo|mkdir|rm|cp|mv|ln|tar|unzip|chmod|chown|grep|sed|awk|cat|vllm|deepspeed|torchrun|accelerate)\b'  # 常见命令行首词
    r')'
)
# key: value 行 (yaml-ish, ASCII key — 中文 "注意:" 不命中)
KV_LINE = re.compile(r'^[A-Za-z_][\w.-]*\s*:(?:\s|$)')
# 缩进结构化续行 (html 外, 2+ 空格缩进行仅当命中才并入当前 run)
STRUCTURED_CONT = re.compile(
    r'^\s*('
    r'[A-Za-z_][\w.-]*\s*:'            # name: test
    r'|[}\]]'                           # 闭合括号
    r'|-\s+\S+\s*:'                    # yaml 列表项 - key: v
    r'|</?[\w]'                         # 标签续行
    r')'
)
# CSS 标记
CSS_LINE = re.compile(r'^\s*[\w-]+\s*:\s*[^;{]+;\s*$')
# 独立 HTML 标签行 (<details>, </summary>, <pre ...> 等) - 跳过, 不参与 bare run
HTML_TAG_LINE = re.compile(r'^<\/?[\w-][\w.-]*(?:\s[^>]*)?>$')
# HTML 容器开标签 (容忍属性: <details open>, <pre class="x">)
DETAILS_OPEN_RE = re.compile(r'<details\b[^>]*>', re.I)
PRE_OPEN_RE = re.compile(r'<pre\b[^>]*>', re.I)
# fence 行: ≤3 空格缩进 (CommonMark; ≥4 缩进的 ``` 是代码内容)
FENCE_LINE = re.compile(r'^ {0,3}(?:```|~~~)')

# bare run 断点
HEADING_RE = re.compile(r'^#{1,6}(?:\s|$)')
# 引用: '>' 连run 长度 1-2 且内容非空白/数字/比较符 ("> 0" 是比较续行, ">>> x" 是 REPL)
BLOCKQUOTE_ANY_RE = re.compile(
    r'^\s*(?:>(?!>)\s*(?:$|[^=\d<>\s])|>{2}(?!>)\s*[^=\d<>\s])'
)
TABLE_RE = re.compile(r'^\s*\|.*\|')   # ≥2 管道才是表格; "| X" 是 python 联合类型续行
SETEXT_RE = re.compile(r'^\s*(?:={3,}|-{3,})\s*$')
# 页面元数据行 (frontmatter / GitHub meta) — 值为 URL / ISO 日期 / md 链接的 key: value
META_LINE = re.compile(
    r'^\s*[A-Za-z_][\w-]*\s*:\s*('
    r'https?://'
    r'|\d{4}-\d{2}-\d{2}'
    r'|\[[^]]*\]\('
    r')'
)
# 元数据 key 黑名单 (爬取产物页头: source/state/labels 等, 非 content)
META_KEY_RE = re.compile(
    r'^(source|lastmod|state|labels|title|author|updated|created|published|tags|url)\s*:',
    re.I
)

# 排除
LIST_RE = re.compile(r'^[-*+]\s')
NUM_LIST_RE = re.compile(r'^\d+[.)]\s+\S')
BLOCKQUOTE_RE = re.compile(r'^>\s')
PROSE_END = re.compile(r'[。.!?]\s*$')   # 行末中文/英文句号
PROSE_START = re.compile(r'^[A-Z][a-z]+(\s+[a-z]+){2,}')  # 英文多词开头像散文
# 语言关键字开头行不作 leading label 剥离 (else "hf" 等)
KW_FIRST = re.compile(
    r'^(else|elif|try|except|finally|return|raise|yield|if|for|while|with|switch|'
    r'case|default|break|continue|pass|import|from|as|not|and|or|in|is|lambda|'
    r'then|do|done|fi|esac|export|local|global|nonlocal|assert|del|async|await)\b'
)


def find_fences(lines):
    """返回 (排除行集合, 是否闭合, 最后一个 fence 行号).

    fence 行本身 + 内部行全部排除. 未闭合时后半文件全被排除, 调用方应警告.
    """
    inside = set()
    in_fence = False
    last_fence = -1
    for i, line in enumerate(lines):
        if FENCE_LINE.match(line):
            inside.add(i)
            last_fence = i
            in_fence = not in_fence
        elif in_fence:
            inside.add(i)
    return inside, not in_fence, last_fence


def find_html_blocks(lines):
    """返回 list of (start, end_inclusive) for <details>/<pre> 容器 (容忍属性)."""
    blocks = []
    i = 0
    while i < len(lines):
        dm = DETAILS_OPEN_RE.search(lines[i])
        pm = PRE_OPEN_RE.search(lines[i]) if not dm else None
        if dm or pm:
            tag = 'details' if dm else 'pre'
            close = f'</{tag}>'
            start = i
            j = i + 1
            while j < len(lines) and close not in lines[j].lower():
                j += 1
            end = j  # 含 tag_close
            blocks.append((start, end))
            i = j + 1
        else:
            i += 1
    return blocks


def find_indent_runs(lines, fenced):
    """4-space/tab indent runs, excluding fenced lines and markdown list items.

    不在此处做长度过滤 — 验证后置到 merge 之后 (空行切碎的短片段靠合并挽回).
    """
    runs = []
    cur = None
    for i, line in enumerate(lines):
        if i in fenced:
            if cur is not None: runs.append(cur); cur = None
            continue
        if line.startswith('    ') or line.startswith('\t'):
            # markdown 列表项 (- * + / 1. 2)) 缩进在 4-space 下不当代码块
            stripped = line.lstrip()
            if LIST_RE.match(stripped) or NUM_LIST_RE.match(stripped):
                if cur is not None: runs.append(cur); cur = None
                continue
            if cur is None: cur = [i, i]
            else: cur[1] = i
        else:
            if cur is not None: runs.append(cur); cur = None
    if cur is not None: runs.append(cur)
    return runs


def _html_state(i, html_blocks):
    """行 i 的 html 归属: 'skip' (容器边界标签) / True (内部) / False."""
    for s, e in html_blocks:
        if s <= i <= e:
            if i == s or i == e:
                return 'skip'
            return True
    return False


def find_bare_runs(lines, fenced, html_blocks):
    """连续非空行块 (无缩进), 排除 fenced lines.

    断点: fenced / html 容器边界 / 独立 HTML 标签行 / 引用 > / 表格 | /
    setext 下划线 / 标题 # (前后有空行才判标题) / 列表项 / 缩进散文续行 / 空行.
    html 容器内缩进行直接并入 run; 容器外仅 STRUCTURED_CONT 命中才并入.

    返回 list of [start, end_inclusive, in_html_bool].
    """
    runs = []
    cur = None
    n = len(lines)
    for i, line in enumerate(lines):
        if i in fenced:
            if cur is not None: runs.append(cur); cur = None
            continue
        state = _html_state(i, html_blocks)
        if state == 'skip':
            if cur is not None: runs.append(cur); cur = None
            continue
        in_any_html = state
        if HTML_TAG_LINE.match(line.strip()):
            if cur is not None: runs.append(cur); cur = None
            continue
        s = line.lstrip()
        # 引用 / 表格 / setext 下划线 / 页面元数据行: 恒断点
        if (BLOCKQUOTE_ANY_RE.match(line) or TABLE_RE.match(line) or SETEXT_RE.match(line)
                or META_LINE.match(line) or META_KEY_RE.match(s)):
            if cur is not None: runs.append(cur); cur = None
            continue
        # 标题: 仅非深缩进 + 前或后有空行 (代码内注释通常紧邻代码行)
        if HEADING_RE.match(s) and not line.startswith('    ') and not line.startswith('\t'):
            prev_blank = (i == 0) or (not lines[i - 1].strip())
            next_blank = (i + 1 >= n) or (not lines[i + 1].strip())
            if prev_blank or next_blank:
                if cur is not None: runs.append(cur); cur = None
                continue
        # markdown 列表项 (- * + / 1. 2)) 当 separator, 不参与 bare run
        if LIST_RE.match(s) or NUM_LIST_RE.match(s):
            if cur is not None: runs.append(cur); cur = None
            continue
        # 缩进行: html 内直接并入; html 外仅结构化续行并入 (挡列表/散文续行)
        if not in_any_html and re.match(r'^ {2,}\S', line):
            if cur is not None and STRUCTURED_CONT.match(line):
                cur[1] = i
                continue
            if cur is not None: runs.append(cur); cur = None
            continue
        if line.strip() == '':
            if cur is not None: runs.append(cur); cur = None
            continue
        if cur is None:
            cur = [i, i, bool(in_any_html)]
        else:
            cur[1] = i
            if in_any_html: cur[2] = True
    if cur is not None: runs.append(cur)
    return runs


def first_code_marker(line):
    s = line.lstrip()
    if LIST_RE.match(s) or NUM_LIST_RE.match(s):
        return None
    if BLOCKQUOTE_RE.match(s):
        return None
    if PROSE_START.match(s):
        return None
    # 注释行 (Python/shell 等) 即使末尾有句号也算代码
    if s.startswith('#'):
        m = CODE_MARK.match(s)
        return m.group(1) if m else '#'
    if PROSE_END.search(s):
        return None
    m = CODE_MARK.match(s)
    return m.group(1) if m else None


def _score_go(block_lines):
    """Go 语言特征打分. 返回匹配特征的行数."""
    score = 0
    for l in block_lines:
        s = l.lstrip()
        # struct tag `` `key:"val"` `` (Go 独有)
        if re.search(r'`\w+:"[^"]+"`', l):
            score += 1
        # type ... struct/interface
        elif re.match(r'^type\s+\w+\s+(struct|interface)\b', s):
            score += 1
        # func 声明
        elif re.match(r'^func\s+(\(\w+\s+\*?\w+\)\s+)?\w+\s*\(', s):
            score += 1
        # package 声明
        elif re.match(r'^package\s+\w+', s):
            score += 1
        # 多返回值短变量声明 `a, b := ...`
        elif re.search(r'\b\w+\s*,\s*\w+\s*:=', l):
            score += 1
        # log.Fatal / t.Fatal / .Errorf
        elif re.search(r'\.Fatal[f]?\(|\.Errorf\(|t\.(Fatal|Error)', l):
            score += 1
    return score


def _score_python(block_lines):
    """Python 语言特征打分."""
    score = 0
    for l in block_lines:
        s = l.lstrip()
        # def/class/async def
        if re.match(r'^(def|class|async\s+def)\s+\w+', s):
            score += 1
        # from X(.Y)* import Z / import X(.Y)* (as Z)?
        elif re.match(r'^(from\s+\w+(\.\w+)+\s+import\s+|import\s+\w+(\.\w+)*(\s+as\s+\w+)?$)', s):
            score += 1
        # @decorator (无尾随空格 — 避免 GitHub @username mention)
        elif re.match(r'^@[\w.]+(\(.*\))?$', s):
            score += 1
        # if __name__ == "__main__"
        elif re.match(r'^if\s+__name__\s*==\s*[\'"]__main__[\'"]', s):
            score += 1
        # 控制流 + 操作符或特殊语法 (避免散文 'with a ...:')
        elif re.match(r'^(if|elif)\b.*\b(in|is|not|==|!=|<=|>=|<|>|and|or)\b.*:', s):
            score += 1
        elif re.match(r'^for\s+\w+\s+in\s+.*:', s):
            score += 1
        elif re.match(r'^with\s+.+\s+as\s+.*:', s):
            score += 1
        elif re.match(r'^(try|except\s+\w+|finally|else):\s*$', s):
            score += 1
        elif re.match(r'^(return|raise)\s+\S', s):
            score += 1
        elif re.match(r'^yield\s+', s):
            score += 1
        # 字面量赋值 `x = [` / `x = (`
        elif re.match(r'^[A-Za-z_]\w*\s*=\s*[\[\(]', s):
            score += 1
    return score


def _score_rust(block_lines):
    """Rust 语言特征打分."""
    score = 0
    for l in block_lines:
        s = l.lstrip()
        if re.match(r'^(fn|pub\s+fn|impl|struct|enum|trait)\s+\w+', s):
            score += 1
        elif re.match(r'^use\s+\w+::', s):
            score += 1
        elif re.match(r'^let\s+(mut\s+)?\w+\s*[=:]', s):
            score += 1
        elif re.match(r'^(const|static)\s+\w+\s*:', s):
            score += 1
    return score


def _score_js(block_lines):
    """JavaScript/TypeScript 特征打分."""
    score = 0
    for l in block_lines:
        s = l.lstrip()
        # function X( / const/let/var X = / class X / export (default)? X / import X from / async function X(
        if re.match(r'^(function\s+\w+\s*\(|const\s+\w+\s*=|let\s+\w+\s*=|var\s+\w+\s*=|class\s+\w+\b|export\s+(default\s+)?(const|let|var|function|class)\s|import\s+.+\s+from\s+|async\s+function\s+\w+)', s):
            score += 1
        elif re.search(r'=>\s*[{(]', l):
            score += 1
        elif re.search(r'\.(then|catch|finally)\s*\(', l):
            score += 1
        elif re.match(r'^(console\.|document\.|window\.|require\()', s):
            score += 1
    return score


def _lang_features_only(block_lines):
    """仅靠语言特征判定语言 (go/python/rust/js). 不含正则兜底.

    用于 is_code_block 兜底 — 避免 SHELL_MARK 把含 `|` 的散文误判为 bash.
    返回语言字符串, 无法识别返回 ''.
    """
    n = max(len(block_lines), 1)
    first = block_lines[0].lstrip()

    # Phase 1: 首行硬规则
    if re.match(r'^(def |class |import |from |async )', first):
        return 'python'
    # @decorator (排除 GitHub @username mention)
    if re.match(r'^@[\w.]+(\(.*\))?$', first):
        return 'python'
    if re.match(r'^(package |func |type\s+\w+\s+(struct|interface))', first):
        return 'go'
    if re.match(r'^(use\s+\w+::|fn\s+\w+|impl\s+\w+|pub\s+fn)', first):
        return 'rust'
    if re.match(r'^(import\s.*from\s|export\s+(default|const|function|class))', first):
        return 'js'

    # Phase 2: 特征打分 (取最高, 需 ≥20% 行匹配)
    scores = [
        ('go', _score_go(block_lines)),
        ('python', _score_python(block_lines)),
        ('rust', _score_rust(block_lines)),
        ('js', _score_js(block_lines)),
    ]
    scores.sort(key=lambda x: x[1], reverse=True)
    if scores[0][1] > 0 and scores[0][1] / n >= 0.20:
        return scores[0][0]
    return ''


def _prose_end_ratio(block_lines):
    """非注释/非 docstring 行中句末标点行的占比 (块级散文信号)."""
    n = max(len(block_lines), 1)
    c = 0
    for l in block_lines:
        s = l.rstrip()
        if s.lstrip().startswith('#'):
            continue
        if '"""' in s or "'''" in s:   # docstring 行不带散文信号
            continue
        if PROSE_END.search(s):
            c += 1
    return c / n


def _kv_ratio(block_lines):
    n = max(len(block_lines), 1)
    return sum(1 for l in block_lines if KV_LINE.match(l.lstrip())) / n


def is_code_block(block_lines, indent=False, in_html=False, relaxed=False):
    """判定一段连续行是否为代码块. 返回 (ok, marker).

    五通道:
      A) 首行 marker + LINE_CODE_HINT 比例 ≥ 阈值 (0.8 / 0.5 in-html/relaxed)
      B) 首行 shell 命令形态 (小写词开头, 无句末标点, 非 >) + 比例 ≥ 阈值
      C) n ≥ 4 + 比例 ≥ 0.9 + 首行有 hint
      D) 语言结构特征 (go/python/rust/js)
      E) key: value 密度 ≥ 0.6 (yaml-ish)
    块级否决: 句末标点率 > 0.4 且无结构特征 → 散文段落.

    参数:
      indent: True → 缩进块语义, 要求 len >= 4
      in_html: True → <details>/<pre> 内, 阈值放宽到 0.5
      relaxed: True → 邻接重试 (紧跟已接受块), 阈值同样放宽到 0.5
    """
    if indent and len(block_lines) < 4:
        STATS['reject'] += 1
        return False, None
    n = len(block_lines)
    if n < 2:
        STATS['reject'] += 1
        return False, None
    code_like = sum(1 for l in block_lines if LINE_CODE_HINT.search(l.lstrip()))
    first = block_lines[0].lstrip()
    marker = first_code_marker(first)
    threshold = 0.5 if (in_html or relaxed) else 0.8
    ratio = code_like / n
    lang_feat = _lang_features_only(block_lines)
    prose_ratio = _prose_end_ratio(block_lines)

    # 块级散文否决 (结构特征命中则豁免 — 代码注释/文档串可带句号)
    if not lang_feat and prose_ratio > 0.4:
        STATS['reject'] += 1
        return False, None

    if marker is not None and ratio >= threshold:
        STATS['A'] += 1
        return True, marker
    if (re.match(r'^[a-z][a-z0-9_-]*\s+\S', first)
            and not PROSE_END.search(first)
            and not first.startswith('>')
            and ratio >= threshold):
        STATS['B'] += 1
        return True, first.split()[0]
    # 强码率: len >= 4 + ratio >= 0.9 + 首行也得有 hint (避免 2-3 行散文假阳)
    if n >= 4 and ratio >= 0.9 and LINE_CODE_HINT.search(first):
        STATS['C'] += 1
        return True, ''

    # 语言结构特征兜底 (仅 go/python/rust/js, 不信任 shell/JSON 正则)
    if lang_feat:
        STATS['D'] += 1
        return True, lang_feat

    # yaml-ish: key: value 密度
    if _kv_ratio(block_lines) >= 0.6 and prose_ratio <= 0.3:
        STATS['E'] += 1
        return True, 'yaml'

    STATS['reject'] += 1
    return False, None


def trim_leading_label(runs_lines):
    """跳过开头的短非代码标签行 (如 【主节点】, ### Step 1).

    返回 trim 后的 lines (可能不足 4 行, 由调用方决定去留), 空则 None.
    不剥离任何 LINE_CODE_HINT 匹配的行 (避免误删 'vllm serve \\' 等 shell 续行).
    """
    if not runs_lines:
        return None
    first = runs_lines[0].lstrip()
    # 短标签 (≤20 字符) 且不是代码, 且不是任何 LINE_CODE_HINT 匹配
    if (len(first) <= 20
            and not KW_FIRST.match(first)
            and not CODE_MARK.match(first)
            and not first_code_marker(first)
            and not KV_LINE.match(first)
            and not LINE_CODE_HINT.search(first)):
        rest = runs_lines[1:]
        return rest if rest else None
    return runs_lines


def trim_trailing_prose(block_lines):
    """剥离块尾散文行 (句末标点收尾 + 无 code hint + 非注释 + ≤120 字符).

    如 "See the docs for more details." 不应被包进 fence.
    保底留 2 行.
    """
    end = len(block_lines)
    while end >= 2:
        last = block_lines[end - 1].rstrip()
        if (last and len(last) <= 120
                and PROSE_END.search(last)
                and not last.lstrip().startswith('#')
                and not LINE_CODE_HINT.search(last.lstrip())):
            end -= 1
        else:
            break
    return block_lines[:end]


def detect_lang(block_lines):
    """粗判语种. 特征打分 (go/python/rust/js) → 正则兜底 (html/json/css/yaml/bash)."""
    n = max(len(block_lines), 1)
    first = block_lines[0].lstrip()

    # Phase 1+2: 语言特征
    lang = _lang_features_only(block_lines)
    if lang:
        return lang

    # Phase 3: 正则兜底
    # python REPL 会话 (>>> 提示符)
    repl = sum(1 for l in block_lines if l.lstrip().startswith('>>>'))
    if repl / n >= 0.25:
        return 'python'
    if first.startswith('<'):
        return 'html'
    json_key = sum(1 for l in block_lines
                   if re.match(r'^\s*"[^"]+"\s*:', l.lstrip()))
    if json_key / n >= 0.5:
        return 'json'
    # 小块 brace 平衡 (n≤10 + 配对 + 双引号)
    joined = '\n'.join(block_lines)
    if n <= 10 and joined.count('{') >= 1 and joined.count('}') >= 1 \
            and joined.count('"') >= 2:
        return 'json'
    css_count = sum(1 for l in block_lines if CSS_LINE.match(l))
    if css_count / n >= 0.4:
        return 'css'
    if _kv_ratio(block_lines) >= 0.5:
        return 'yaml'
    shell_count = sum(1 for l in block_lines
                      if SHELL_MARK.match(l.lstrip())
                      or l.lstrip().startswith('--')
                      or re.search(r'\$\{|\$\w', l)
                      or re.search(r'\|\s*[\w.$/-]', l)   # 管道后接 token (表格行已被断点排除)
                      or (re.match(r'^[a-z][a-z0-9_.-]*\s+\S', l.lstrip())
                          and re.search(r'(^|\s)--?[\w/-]|\$\w|\\$|/', l)))
    if shell_count / n >= 0.25:
        return 'bash'
    return ''


def _nonblank(lines, s, e):
    return [l for l in lines[s:e + 1] if l.strip()]


def merge_runs(lines, runs_with_meta):
    """合并相邻 runs (含 indent 和 bare). gap ≤2 空行 (全空) → 一段.

    合并仅跨越空行, 不引入新内容行; bare 部分已逐段验证, indent 来源最终块后置验证.
    """
    merged = []
    for entry in runs_with_meta:
        s, e, in_html, marker, origin = entry
        if merged:
            ps, pe, ph, pm, po = merged[-1]
            gap = s - pe - 1
            blank_count = sum(1 for i in range(pe + 1, s) if not lines[i].strip())
            new_total = (pe - ps + 1) + gap + (e - s + 1)
            if 0 <= gap <= 2 and blank_count == gap and new_total <= 200:
                merged[-1] = [ps, e, ph or in_html, pm or marker, po | origin]
                continue
        merged.append([s, e, in_html, marker, origin])

    # 转成 (s, e, lang) 格式; indent 来源块做后置验证
    out = []
    for s, e, in_html, marker, origin in merged:
        block_lines = lines[s:e + 1]
        if 'indent' in origin:
            nb = _nonblank(lines, s, e)
            indent_maj = (sum(1 for l in nb if l.startswith('    ') or l.startswith('\t')) * 2 > len(nb))
            ok, _ = is_code_block(nb, indent=indent_maj, in_html=in_html)
            if not ok:
                continue
        out.append((s, e, detect_lang(block_lines)))
    return out


def find_code_blocks(path):
    with open(path, encoding='utf-8', newline='') as f:
        text = f.read()
    lines = text.split('\n')
    fenced, fence_closed, last_fence = find_fences(lines)
    if not fence_closed:
        print(f'WARN {path}: 未闭合 fence @line {last_fence + 1}, 其后内容跳过', file=sys.stderr)
    html_blocks = find_html_blocks(lines)

    # 收集所有候选 runs (含 indent + bare)
    # indent: 不预过滤 — 短片段靠 merge 挽回, 验证后置
    candidates = []
    for s, e in find_indent_runs(lines, fenced):
        candidates.append([s, e, False, None, {'indent'}])

    # bare: 先常规验证; 被拒 run 若紧跟已接受块 (gap ≤2 全空行) 用放宽阈值重试, 链式传播
    accepted = []
    pending = []
    for s, e, in_html in find_bare_runs(lines, fenced, html_blocks):
        block = lines[s:e + 1]
        after_lead = trim_leading_label(block)
        if after_lead is None:
            continue
        lead_removed = len(block) - len(after_lead)
        trimmed = trim_trailing_prose(after_lead)
        if len(trimmed) < 2:
            continue
        s_adj = s + lead_removed
        e_adj = s_adj + len(trimmed) - 1
        ok, marker = is_code_block(trimmed, indent=False, in_html=in_html)
        if ok:
            accepted.append((s_adj, e_adj, in_html, marker))
        else:
            pending.append((s_adj, e_adj, in_html, trimmed))

    # 邻接重试直到不动点 (新接受的块可解锁后续 run)
    while True:
        ends = [e for _, e, _, _ in accepted]
        progressed = False
        still = []
        for s, e, in_html, trimmed in pending:
            near = any(
                0 <= s - ae - 1 <= 2
                and all(not lines[i].strip() for i in range(ae + 1, s))
                for ae in ends
            )
            ok, marker = is_code_block(trimmed, indent=False, in_html=in_html,
                                       relaxed=near) if near else (False, None)
            if ok:
                accepted.append((s, e, in_html, marker))
                progressed = True
            else:
                still.append((s, e, in_html, trimmed))
        pending = still
        if not progressed or not pending:
            break

    for s, e, in_html, marker in accepted:
        candidates.append([s, e, in_html, marker, {'bare'}])

    if not candidates:
        return [], lines

    # 按 start 排序, 去重叠 (保留较长者)
    candidates.sort(key=lambda x: (x[0], -(x[1] - x[0])))
    deduped = []
    for c in candidates:
        s, e, _, _, _ = c
        if deduped and s < deduped[-1][1]:
            # 重叠, 跳过 (前者较长)
            continue
        deduped.append(c)

    return merge_runs(lines, deduped), lines


def format_report(path, blocks, lines):
    rel = path
    out = [f'## {rel}', f'识别 {len(blocks)} 段\n']
    for idx, (s, e, lang) in enumerate(blocks, 1):
        n = e - s + 1
        out.append(f'### 段 {idx}: lines {s + 1}-{e + 1} ({n} 行) [{lang or "-"}]')
        first = lines[s].lstrip()[:80]
        out.append(f'首行: `{first}`')
        out.append('')
    return '\n'.join(out)


def apply_fixes(path, blocks, dry=True, bak=False):
    with open(path, encoding='utf-8', newline='') as f:
        text = f.read()
    lines = text.split('\n')
    new_lines = list(lines)
    changes = 0
    for s, e, lang in reversed(blocks):
        # fence 永远左对齐 (markdown 规范); 内容保持原缩进
        fence_open = f'```{lang}'.rstrip()
        fence_close = '```'
        new_lines.insert(e + 1, fence_close)
        new_lines.insert(s, fence_open)
        changes += 1
    new_text = '\n'.join(new_lines)
    if not dry:
        if bak:
            bak_path = path + '.bak'
            if not os.path.exists(bak_path):
                with open(bak_path, 'w', encoding='utf-8', newline='') as f:
                    f.write(text)
        with open(path, 'w', encoding='utf-8', newline='') as f:
            f.write(new_text)
    return new_text, changes


def iter_md(root):
    for dp, _, files in os.walk(root):
        for fn in files:
            if fn.endswith('.md'):
                yield os.path.join(dp, fn)


def load_state():
    try:
        with open(STATE_PATH, encoding='utf-8') as f:
            return json.load(f)
    except (OSError, ValueError):
        return {}


def save_state(state):
    with open(STATE_PATH, 'w', encoding='utf-8') as f:
        json.dump(state, f, ensure_ascii=False, sort_keys=True)


def hash_file(path):
    with open(path, 'rb') as f:
        return hashlib.sha1(f.read()).hexdigest()


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--dry-run', action='store_true', help='只列, 不写')
    ap.add_argument('--apply', action='store_true', help='原地修改')
    ap.add_argument('--bak', action='store_true', help='apply 时写 .bak 备份 (默认不写)')
    ap.add_argument('--review', action='store_true', help='生成 review 候选文件')
    ap.add_argument('--stats', action='store_true', help='输出判定通道统计')
    ap.add_argument('--only', help='只处理某 SRC (e.g. SRC-008)')
    ap.add_argument('--root', default=SOURCES, help='扫描根目录')
    ap.add_argument('--force', action='store_true', help='忽略已执行记录, 全量处理')
    args = ap.parse_args()

    if not (args.dry_run or args.apply or args.review):
        args.dry_run = True

    if args.only:
        only_root = os.path.join(args.root, args.only)
        if not os.path.isdir(only_root):
            print(f'NOT FOUND: {only_root}', file=sys.stderr)
            sys.exit(1)
        roots = [only_root]
    else:
        # 按 SRC-NNN 子目录分组, 每个 SRC 单独处理
        roots = []
        for entry in sorted(os.listdir(args.root)):
            sub = os.path.join(args.root, entry)
            if os.path.isdir(sub) and entry.startswith('SRC-'):
                roots.append(sub)
        if not roots:
            # 兜底: 整个 root 当一个单元
            roots = [args.root]

    total_files = 0
    total_blocks = 0
    total_changes = 0
    total_skipped = 0
    review_path = os.path.join(ROOT, 'scrape', 'review_fence_candidates.md')

    state = load_state()
    state_dirty = False

    if args.review:
        review_out = ['# Fence 修复候选 (review)\n']
    else:
        review_out = None

    for r in roots:
        md_files = sorted(iter_md(r))
        src_label = os.path.basename(r.rstrip('/'))
        print(f'>>> {src_label}: {len(md_files)} files', flush=True)
        for idx, p in enumerate(md_files, 1):
            rel = os.path.relpath(p, ROOT)
            if not args.force:
                try:
                    if state.get(rel) == hash_file(p):
                        total_skipped += 1
                        continue
                except OSError:
                    pass
            try:
                blocks, lines = find_code_blocks(p)
            except Exception as ex:
                print(f'  [{idx}/{len(md_files)}] SKIP {p}: {ex}', file=sys.stderr, flush=True)
                continue
            if not blocks:
                if args.apply:
                    # 无块也算已执行, 记 hash 免得每天重扫
                    try:
                        state[rel] = hash_file(p)
                        state_dirty = True
                    except OSError:
                        pass
                # 进度日志: 每 50 文件或末文件打一行
                if idx % 50 == 0 or idx == len(md_files):
                    print(f'  [{idx}/{len(md_files)}] scanned (0 blocks so far in this batch)', flush=True)
                continue
            total_files += 1
            total_blocks += len(blocks)
            if args.review:
                review_out.append(format_report(p, blocks, lines))
                for ridx, (s, e, lang) in enumerate(blocks, 1):
                    preview = '\n'.join(lines[s:s + 15])
                    review_out.append('```')
                    review_out.append(preview)
                    review_out.append('```')
                    review_out.append('')
            elif args.dry_run:
                print(f'\n  [{idx}/{len(md_files)}] {p}')
                for bidx, (s, e, lang) in enumerate(blocks, 1):
                    first = lines[s].lstrip()[:80]
                    print(f'    段 {bidx}: lines {s + 1}-{e + 1} ({e - s + 1} 行) [{lang or "-"}] `{first}`', flush=True)
            elif args.apply:
                _, ch = apply_fixes(p, blocks, dry=False, bak=args.bak)
                total_changes += ch
                # 记录 apply 后内容 hash; 后续运行内容未变即跳过
                try:
                    state[rel] = hash_file(p)
                    state_dirty = True
                except OSError:
                    pass
                print(f'  [{idx}/{len(md_files)}] FIXED {p}: +{ch} fences', flush=True)

    # 保存状态: 仅 apply 有新记录时; 顺带清掉已删除文件的条目
    if state_dirty:
        alive = set()
        for r in roots:
            for p in iter_md(r):
                alive.add(os.path.relpath(p, ROOT))
        state = {k: v for k, v in state.items() if k in alive}
        save_state(state)

    if args.review:
        with open(review_path, 'w', encoding='utf-8', newline='') as f:
            f.write('\n'.join(review_out))
        print(f'wrote {review_path} ({os.path.getsize(review_path) / 1024:.0f} KB)')
    else:
        print(f'\n=== done: files={total_files}, blocks={total_blocks}'
              + (f', changes={total_changes}' if args.apply else '')
              + (f', skipped={total_skipped}' if total_skipped else ''), flush=True)

    if args.stats:
        print(f'channels: {dict(STATS)}', flush=True)


if __name__ == '__main__':
    main()
