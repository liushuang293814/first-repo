# -*- coding: utf-8 -*-
"""论文写作进度统计：统计 .md/.tex 文件的字数与图表引用数。

用法:
    python word_count.py <目录或文件>
"""
import re
import sys
from pathlib import Path


def count_file(path: Path) -> dict:
    text = path.read_text(encoding="utf-8", errors="ignore")
    cjk = len(re.findall(r"[\u4e00-\u9fff]", text))          # 中文字符
    words = len(re.findall(r"[A-Za-z]+(?:'[A-Za-z]+)?", text))  # 英文单词
    figs = len(re.findall(r"\\ref\{fig:[^}]+\}|图\s?\d+-\d+", text))   # 图引用
    tabs = len(re.findall(r"\\ref\{tab:[^}]+\}|表\s?\d+-\d+", text))   # 表引用
    return {"file": path.name, "cjk": cjk, "en_words": words, "fig_refs": figs, "tab_refs": tabs}


if __name__ == "__main__":
    target = Path(sys.argv[1] if len(sys.argv) > 1 else ".")
    files = target.rglob("*.md") if target.is_dir() else [target]
    files = list(files) + (list(target.rglob("*.tex")) if target.is_dir() else [])
    total_cjk = 0
    print(f"{'文件':<30}{'中文字':>8}{'英文词':>8}{'图引用':>8}{'表引用':>8}")
    for f in files:
        s = count_file(f)
        total_cjk += s["cjk"]
        print(f"{s['file']:<30}{s['cjk']:>8}{s['en_words']:>8}{s['fig_refs']:>8}{s['tab_refs']:>8}")
    print(f"\n中文字符总计: {total_cjk}")
