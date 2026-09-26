#!/usr/bin/env bash
# fetch_missing_details.py 看门狗:
#   - 未运行 → 启动 (nohup 后台, 日志追加到 scrape/logs/)
#   - 日志出现 "err: timeout" → kill 当前进程(含子进程) → 等 30s → 重启
#   - 每次启动前清空运行日志 (防止旧 timeout 行反复触发重启)
#
# 用法:
#   nohup bash scrape/fetch_details_watchdog.sh >> scrape/logs/watchdog.out 2>&1 &
#
# 环境变量:
#   FETCH_ARGS   传给 fetch_missing_details.py 的参数 (默认空 = 全量; 测试可设 --dry-run)
#   POLL_SEC     轮询间隔 (默认 60)
#   RESTART_SEC  timeout 后等待秒数 (默认 30)
set -u
cd "$(dirname "$0")/.."   # 仓库根 knowledge-sources/

RUN_LOG="scrape/logs/fetch_missing_details.log"
WATCH_LOG="scrape/logs/watchdog.log"
POLL_SEC="${POLL_SEC:-60}"
RESTART_SEC="${RESTART_SEC:-30}"
FETCH_ARGS="${FETCH_ARGS:-}"
mkdir -p scrape/logs

# 单实例锁
exec 200>"scrape/logs/watchdog.lock"
flock -n 200 || { echo "watchdog already running, exit"; exit 1; }

dt() { date '+%F %T'; }
log() { echo "[$(dt)] $*" >> "$WATCH_LOG"; }

is_running() { pgrep -f "fetch_missing_details\.py" >/dev/null 2>&1; }

kill_run() {
    pkill -f "fetch_missing_details\.py" 2>/dev/null
    pkill -f "scrape/scrape\.py SRC-" 2>/dev/null   # 其 scrape.py 子进程
    sleep 1
    pkill -9 -f "fetch_missing_details\.py" 2>/dev/null
    pkill -9 -f "scrape/scrape\.py SRC-" 2>/dev/null
    log "killed old run"
}

start_run() {
    : > "$RUN_LOG"    # 清空, 防旧 timeout 行触发循环重启
    log "start: python3 -u scrape/fetch_missing_details.py $FETCH_ARGS"
    nohup python3 -u scrape/fetch_missing_details.py $FETCH_ARGS >> "$RUN_LOG" 2>&1 &
}

log "watchdog up (poll=${POLL_SEC}s restart_wait=${RESTART_SEC}s args='$FETCH_ARGS')"

while true; do
    if is_running; then
        # 只看本次运行日志的尾部
        if tail -n 50 "$RUN_LOG" 2>/dev/null | grep -q "err: timeout"; then
            log "err: timeout detected -> kill + wait ${RESTART_SEC}s + restart"
            kill_run
            sleep "$RESTART_SEC"
            start_run
        fi
    else
        log "not running -> start"
        start_run
    fi
    sleep "$POLL_SEC"
done
