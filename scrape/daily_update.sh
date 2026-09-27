#!/usr/bin/env bash
# 每日全量刷新一键流程:
#   scrape.py 全 SRC 增量 → fence_md 代码块包裹 → summary → index → README 快照表
#   → git commit → push
#
# 失败策略:
#   scrape / fence / README 快照失败 → 继续 (幂等, 次日自愈)
#   summary / index 失败 → 中止 commit (避免"数据新文档旧"的误导性提交),
#     数据保留在工作区, 修好后重跑即可
#
# 用法:
#   bash scrape/daily_update.sh                # 全流程 (含 push)
#   bash scrape/daily_update.sh --skip-push    # 到 commit 为止, 手动确认后再 push
#   bash scrape/daily_update.sh --skip-scrape  # 跳过抓取, 直接 fence→summary→index→commit→push
#
# 日志: scrape/logs/daily_YYYY-MM-DD.log (gitignored)
# 锁:   scrape/logs/daily.lock (单实例)
set -uo pipefail
cd "$(dirname "$0")/.."   # 仓库根 knowledge-sources/

DATE=$(date +%F)
LOGDIR="scrape/logs"
LOG="$LOGDIR/daily_${DATE}.log"
mkdir -p "$LOGDIR"
SKIP_PUSH=0
SKIP_SCRAPE=0
for a in "$@"; do
    case "$a" in
        --skip-push) SKIP_PUSH=1 ;;
        --skip-scrape) SKIP_SCRAPE=1 ;;
        *) echo "unknown arg: $a (支持 --skip-push / --skip-scrape)"; exit 2 ;;
    esac
done

exec 9>"$LOGDIR/daily.lock"
flock -n 9 || { echo "daily_update already running, exit"; exit 1; }

log() { echo "[$(date '+%T')] $*" | tee -a "$LOG"; }

log "== daily update ${DATE} start (skip_push=${SKIP_PUSH})"
CRIT_FAIL=0   # summary/index 任一失败 → 不 commit

# ① 全量 SRC 增量 (head-check, 无变化的 SRC 只花 1 次 API)
# 失败: per-SRC 容错, 整体挂=网络/API 断, 已更新部分照用, 次日自愈
if [ "$SKIP_SCRAPE" -eq 1 ]; then
    log "step1 SKIPPED (--skip-scrape)"
else
    log "step1: scrape.py 全量遍历"
    if python3 -u scrape/scrape.py >> "$LOG" 2>&1; then
        log "step1 ok"
    else
        log "step1 FAILED (部分数据可能已入库, 明日重跑自愈) rc=$?"
    fi
fi

# ② 新增/变更 md 的代码块包裹 (增量状态自动跳过未变文件)
# 失败: 纯观感问题, 继续
log "step2: fence_md --apply"
if python3 -u scrape/fence_md.py --apply >> "$LOG" 2>&1; then
    log "step2 ok"
else
    log "step2 FAILED (新文件未包裹, 下次补上) rc=$?"
fi

# ③ _summary/ 报告 — 派生层, 失败必须中止 commit
log "step3: summary_gen"
if python3 scrape/summary_gen.py >> "$LOG" 2>&1; then
    log "step3 ok"
else
    log "step3 FAILED — summary 过期, 中止 commit"
    CRIT_FAIL=1
fi

# ④ index.html / _index.json — 派生层, 失败必须中止 commit
log "step4: build_index --regen"
if python3 scrape/build_index.py --regen >> "$LOG" 2>&1; then
    log "step4 ok"
else
    log "step4 FAILED — index 过期, 中止 commit"
    CRIT_FAIL=1
fi

if [ "$CRIT_FAIL" -eq 1 ]; then
    log "== ABORT: summary/index 失败, 数据保留工作区未提交; 修复后重跑 (幂等) 后再 commit"
    exit 1
fi

# ⑤ README 快照表 (日期 / 文件总数 / 总体积) — 数字略旧可容忍, 继续
log "step5: README snapshot"
if python3 - <<'PYEOF' >> "$LOG" 2>&1
import datetime
import os
import re

today = datetime.date.today().isoformat()
n = 0
b = 0
for dp, _, fs in os.walk('sources'):
    for f in fs:
        n += 1
        b += os.path.getsize(os.path.join(dp, f))
p = 'README.md'
s = open(p, encoding='utf-8').read()
s2 = re.sub(r'(\| 抓取快照日期 \| )[^|]*\|', lambda m: f"{m.group(1)}{today} |", s)
s2 = re.sub(r'(\| 文件总数 \| )[^|]*\|', lambda m: f"{m.group(1)}~{n} |", s2)
s2 = re.sub(r'(\| 总体积 \| )[^|]*\|', lambda m: f"{m.group(1)}~{b/1e6:.0f} MB |", s2)
open(p, 'w', encoding='utf-8').write(s2)
print(f'README snapshot -> date={today} files={n} bytes={b/1e6:.0f}MB changed={s2 != s}')
PYEOF
then
    log "step5 ok"
else
    log "step5 FAILED (快照数字略旧, 继续) rc=$?"
fi

# ⑥ commit + push
log "step6: git commit"
git add -A
CHANGED=$(git status --short | wc -l)
if [ "${CHANGED:-0}" -eq 0 ]; then
    log "no changes — nothing to commit"
    log "== daily update ${DATE} done (clean)"
    exit 0
fi
git commit -m "chore: daily refresh ${DATE} (${CHANGED} files)" >> "$LOG" 2>&1
log "step6 committed ${CHANGED} files"

if [ "$SKIP_PUSH" -eq 1 ]; then
    log "--skip-push: 本地 commit 完成, 未推送 (git push origin main 手动推)"
else
    log "step7: push"
    if git push origin main >> "$LOG" 2>&1; then
        log "step7 pushed"
    else
        log "step7 PUSH FAILED — 检查 ${LOG} 后手动 git push"
    fi
fi
log "== daily update ${DATE} done"
