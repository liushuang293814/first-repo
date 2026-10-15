# -*- coding: utf-8 -*-
"""批量重命名工具：给目录下指定类型的文件加序号前缀。

用法:
    python rename_with_index.py <目录> <扩展名> [起始序号]
示例:
    python rename_with_index.py ./imgs png 1
    # imgs/shot.png -> imgs/001_shot.png
"""
import sys
from pathlib import Path


def rename_with_index(folder: Path, ext: str, start: int = 1, width: int = 3) -> list:
    """给 folder 下所有 ext 文件按名字排序加序号前缀，返回改动清单。"""
    files = sorted(folder.glob(f"*.{ext.lstrip('.')}"))
    changes = []
    for i, f in enumerate(files, start=start):
        new_name = f"{i:0{width}d}_{f.name}"
        f.rename(f.with_name(new_name))
        changes.append((f.name, new_name))
    return changes


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print(__doc__)
        sys.exit(1)
    target = Path(sys.argv[1])
    if not target.is_dir():
        print(f"目录不存在: {target}")
        sys.exit(1)
    result = rename_with_index(target, sys.argv[2], int(sys.argv[3]) if len(sys.argv) > 3 else 1)
    for old, new in result:
        print(f"{old}  ->  {new}")
    print(f"共重命名 {len(result)} 个文件")
