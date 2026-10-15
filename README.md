# first-repo

我的第一个 GitHub 仓库，由 DSH 代管。放一些实用小工具。

## 内容

| 文件 | 用途 |
|---|---|
| `rename_with_index.py` | 批量给文件加序号前缀（`001_名字.png`），整理截图/素材用 |
| `word_count.py` | 统计 .md/.tex 的中文字数、英文词数与图表引用数，论文写作进度用 |

## 用法

```bash
python rename_with_index.py ./imgs png          # imgs 下所有 png 加序号
python word_count.py E:\zhuomian\1我的第一篇论文  # 统计论文目录写作量
```

环境：Python 3.10+，无第三方依赖。
