"""Inject CF clearance cookies from real Chrome into playwright contexts.

Use for SRCs that block headless playwright (Cloudflare bot detection).

Usage from blog.py:
    from . import cookies
    ctx = browser.new_context(...)
    cookies.inject_cf_clearance(ctx, '.amd.com',
                                'cf_clearance_value...')
"""
import time


def inject_cf_clearance(ctx, domain, clearance_value,
                        other_cookies=None, ua=None):
    """Add cf_clearance + optional companion cookies to a playwright context.

    domain: '.amd.com' (with leading dot) — CF uses this for subdomains.
    clearance_value: the literal cf_clearance string.
    other_cookies: list of dicts with name/value/domain/path/expires (optional).
    """
    cookies_list = [{
        'name': 'cf_clearance',
        'value': clearance_value,
        'domain': domain,
        'path': '/',
        'expires': int(time.time()) + 3600,  # 1h — CF will revalidate
        'httpOnly': True,
        'secure': True,
        'sameSite': 'None',
    }]
    if other_cookies:
        for c in other_cookies:
            if 'expires' not in c or isinstance(c.get('expires'), str):
                # convert ISO date to epoch if needed
                pass
            cookies_list.append({**c, 'secure': True})
    ctx.add_cookies(cookies_list)