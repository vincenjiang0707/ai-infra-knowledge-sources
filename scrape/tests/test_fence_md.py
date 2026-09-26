#!/usr/bin/env python3
"""fence_md 定位逻辑回归测试. 运行: python3 scrape/tests/test_fence_md.py

fixture → 期望 (start, end, lang) 列表, 0-indexed 行号 (含两端).
"""
import contextlib
import io
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..'))
import fence_md  # noqa: E402

FIX = os.path.join(HERE, 'fixtures')
RESULTS = []


def blocks_of(fname):
    blocks, _ = fence_md.find_code_blocks(os.path.join(FIX, fname))
    return blocks


def check(name, actual, expected):
    ok = actual == expected
    RESULTS.append((name, ok))
    print(f'{"PASS" if ok else "FAIL"} {name}')
    if not ok:
        print(f'  expected: {expected!r}')
        print(f'  actual:   {actual!r}')


def case_details_json():
    # <details> 内 2 空格缩进 JSON 必须检出 (B1 回归)
    check('details_json', blocks_of('details_json.md'), [(3, 6, 'json')])


def case_details_open():
    # <details open> 属性变体也进 html 区间, 享受 0.5 阈值
    check('details_open', blocks_of('details_open.md'), [(1, 2, 'bash')])


def case_heading_mixed():
    # 标题紧贴代码 (无空行) 时不入块
    check('heading_mixed', blocks_of('heading_mixed.md'), [(1, 2, 'bash')])


def case_quote_code():
    # > 引用行不当 separator 时会混入; 现在应被排除
    check('quote_code', blocks_of('quote_code.md'), [(5, 7, 'bash')])


def case_indent_blank_split():
    # 空行切开的 indent 代码段应合并为一块
    check('indent_blank_split', blocks_of('indent_blank_split.md'), [(2, 6, 'python')])


def case_unclosed_fence():
    # 未闭合 fence: 警告 + 0 块
    err = io.StringIO()
    with contextlib.redirect_stderr(err):
        blocks = blocks_of('unclosed_fence.md')
    check('unclosed_fence_blocks', blocks, [])
    check('unclosed_fence_warn', '未闭合' in err.getvalue(), True)


def case_prose_paragraph():
    # 英文散文段落 (含括号) 不检出
    check('prose_paragraph', blocks_of('prose_paragraph.md'), [])


def case_table():
    # 表格行不入块
    check('table', blocks_of('table.md'), [(4, 7, 'bash')])


def case_yaml_doc():
    # --- 后的 yaml 块检出
    check('yaml_doc', blocks_of('yaml_doc.md'), [(1, 4, 'yaml')])


def case_list_continuation():
    # 列表 4 空格续行散文不检出; 短 indent 代码保守跳过
    check('list_continuation', blocks_of('list_continuation.md'), [])


def case_trailing_prose():
    # 块尾散文行 ("See the docs...") 剥离
    check('trailing_prose', blocks_of('trailing_prose.md'), [(0, 3, 'bash')])


def case_repl_session():
    # >>> REPL 会话不是引用, 必须检出
    check('repl_session', blocks_of('repl_session.md'), [(2, 5, 'python')])


def case_crlf():
    # CRLF 文件: 定位正常 + dry apply 保留 \r
    path = os.path.join(FIX, 'crlf_runtime.md')
    with open(path, 'wb') as f:
        f.write(b'Intro line here.\r\n\r\nexport A=1\r\n--flag-one 1\r\n--flag-two 2\r\n--flag-three 3\r\n')
    try:
        blocks, _ = fence_md.find_code_blocks(path)
        check('crlf_blocks', blocks, [(2, 5, 'bash')])
        new_text, ch = fence_md.apply_fixes(path, blocks, dry=True)
        check('crlf_preserved', ('\r\n' in new_text) and ('```bash' in new_text), True)
        check('crlf_changes', ch, 1)
    finally:
        if os.path.exists(path):
            os.remove(path)


def main():
    for fn in [
        case_details_json, case_details_open, case_heading_mixed,
        case_quote_code, case_indent_blank_split, case_unclosed_fence,
        case_prose_paragraph, case_table, case_yaml_doc,
        case_list_continuation, case_trailing_prose, case_repl_session, case_crlf,
    ]:
        fn()
    failed = [r for r in RESULTS if not r[1]]
    print(f'\n{len(RESULTS) - len(failed)}/{len(RESULTS)} passed')
    sys.exit(1 if failed else 0)


if __name__ == '__main__':
    main()
