"""Persistent Chrome daemon with remote-debugging-port.

One real Chrome process listens on 127.0.0.1:9222. User manually passes CF
challenges in that browser. Playwright then attaches via CDP — same IP, TLS,
fingerprint, cookies as the real session.

Start:
    python3 chrome_daemon.py            # foreground, headless=new (has window)
    python3 chrome_daemon.py --bg       # background, headless=new
    python3 chrome_daemon.py --kill     # stop running daemon

Use from scraper:
    from chrome_daemon import browser_ctx
    with browser_ctx() as (browser, ctx):
        page = ctx.new_page()
        ...
"""
import argparse
import json
import os
import signal
import subprocess
import sys
import time
from pathlib import Path

CDP_URL = 'http://127.0.0.1:9222'
PID_FILE = Path('/tmp/scrape_chrome_daemon.pid')
LOG_FILE = Path('/tmp/scrape_chrome_daemon.log')

# Use real Chrome (user's installed browser). Falls back to puppeteer chrome.
CHROME_PATHS = [
    '/mnt/c/Program Files/Google/Chrome/Application/chrome.exe',
    '/mnt/c/Program Files (x86)/Google/Chrome/Application/chrome.exe',
    os.path.expanduser('~/.cache/puppeteer/chrome/linux-131.0.6778.204/chrome-linux64/chrome'),
    '/usr/bin/google-chrome',
    '/usr/bin/chromium-browser',
]


def find_chrome():
    for p in CHROME_PATHS:
        if os.path.exists(p):
            return p
    return None


def is_alive():
    """Daemon live if PID file exists + process running + CDP responding."""
    if not PID_FILE.exists():
        return False
    try:
        pid = int(PID_FILE.read_text().strip())
        os.kill(pid, 0)
    except Exception:
        return False
    try:
        import urllib.request
        urllib.request.urlopen(f'{CDP_URL}/json/version', timeout=2).read()
        return True
    except Exception:
        return False


def start(background=False):
    if is_alive():
        print(f'[daemon] already alive (pid={PID_FILE.read_text().strip()})', flush=True)
        return
    chrome = find_chrome()
    if not chrome:
        print('[daemon] no Chrome found in:', *CHROME_PATHS, file=sys.stderr)
        sys.exit(1)
    # In WSL2, .exe must be invoked via cmd.exe with Windows-style path
    in_wsl = 'microsoft' in os.uname().release.lower() or os.path.exists('/proc/version')
    is_windows_exe = chrome.endswith('.exe')
    if in_wsl and is_windows_exe:
        # convert /mnt/c/... to C:\...
        win_path = chrome.replace('/mnt/c/', 'C:\\').replace('/', '\\')
        profile_dir = 'C:\\scrape_chrome_profile'
        cmd = ['cmd.exe', '/c', win_path,
               '--remote-debugging-port=9222',
               '--remote-debugging-address=127.0.0.1',
               f'--user-data-dir={profile_dir}',
               '--no-first-run', '--no-default-browser-check',
               '--window-size=1280,800', 'about:blank']
    else:
        profile_dir = '/tmp/scrape_chrome_profile'
        os.makedirs(profile_dir, exist_ok=True)
        cmd = [chrome,
               '--remote-debugging-port=9222',
               '--remote-debugging-address=127.0.0.1',
               f'--user-data-dir={profile_dir}',
               '--no-first-run',
               '--no-default-browser-check',
               '--disable-background-timer-throttling',
               '--disable-backgrounding-occluded-windows',
               '--disable-renderer-backgrounding',
               '--window-size=1280,800',
               'about:blank']
    log = open(LOG_FILE, 'ab')
    proc = subprocess.Popen(cmd, stdout=log, stderr=log,
                            stdin=subprocess.DEVNULL,
                            creationflags=subprocess.CREATE_NEW_PROCESS_GROUP if os.name == 'nt' else 0)
    PID_FILE.write_text(str(proc.pid))
    # wait for CDP
    import urllib.request
    for i in range(30):
        try:
            urllib.request.urlopen(f'{CDP_URL}/json/version', timeout=1).read()
            print(f'[daemon] up — pid={proc.pid} chrome={chrome}', flush=True)
            print(f'[daemon] open in real Chrome: {CDP_URL}', flush=True)
            print(f'[daemon] OR visit https://rocm.blogs.amd.com/ in this window to pass CF', flush=True)
            return
        except Exception:
            time.sleep(0.5)
    print('[daemon] failed to bring up CDP — see', LOG_FILE, file=sys.stderr)
    sys.exit(1)


def kill():
    if not PID_FILE.exists():
        print('[daemon] no pidfile')
        return
    pid = int(PID_FILE.read_text().strip())
    try:
        os.kill(pid, signal.SIGTERM)
    except Exception:
        pass
    PID_FILE.unlink(missing_ok=True)
    print(f'[daemon] killed pid={pid}')


def status():
    if is_alive():
        pid = PID_FILE.read_text().strip()
        print(f'[daemon] alive pid={pid}')
        try:
            import urllib.request
            v = json.loads(urllib.request.urlopen(f'{CDP_URL}/json/version', timeout=2).read())
            print(f'  browser: {v.get("Browser")}')
            print(f'  url:     {v.get("webSocketDebuggerUrl", "")[:80]}...')
        except Exception as e:
            print(f'  (CDP error: {e})')
    else:
        print('[daemon] not running')


def browser_ctx():
    """Context manager: connect playwright to existing Chrome via CDP.

    Returns (browser, ctx, page_hint).
    Usage:
        with browser_ctx() as (browser, ctx, page):
            page.goto(...)
    """
    from playwright.sync_api import sync_playwright
    if not is_alive():
        raise RuntimeError(f'Chrome daemon not running. Start: python3 {__file__}')
    pw = sync_playwright().start()
    browser = pw.chromium.connect_over_cdp(CDP_URL)
    # reuse default context (carries user's cookies / CF clearance)
    ctx = browser.contexts[0] if browser.contexts else browser.new_context()
    page = ctx.pages[0] if ctx.pages else ctx.new_page()
    try:
        yield browser, ctx, page
    finally:
        try:
            pw.stop()
        except Exception:
            pass


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--bg', action='store_true', help='start in background')
    ap.add_argument('--kill', action='store_true')
    ap.add_argument('--status', action='store_true')
    args = ap.parse_args()
    if args.kill:
        kill()
    elif args.status:
        status()
    else:
        start(background=args.bg)


if __name__ == '__main__':
    main()