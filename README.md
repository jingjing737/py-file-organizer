# py-file-organizer 📁

按扩展名自动整理文件到分类文件夹。

## 快速开始

### 整理文件

```bash
python3 organize.py ~/Downloads
```

### 恢复整理（恢复 Downloads）

```bash
python3 restore_downloads.py ~/Downloads

# 预览模式
python3 restore_downloads.py ~/Downloads --dry-run
```

## 用法

### organize.py — 按扩展名整理

```bash
python3 organize.py <目标文件夹> [--dry-run]
```

| 参数 | 说明 |
|------|------|
| `folder` | 要整理的目录 |
| `--dry-run` | 预览模式，不移动文件 |

### restore_downloads.py — 恢复 Downloads 整理

将 `organize.py` 生成的分类文件夹（`图片/`、`代码/`、`其他/` 等）中的文件移回根目录，并删除空文件夹。**不会动你原本的文件夹**（如 `BackupRecord/`、`moshi/` 等）。

```bash
# 恢复 Downloads
python3 restore_downloads.py ~/Downloads

# 预览模式
python3 restore_downloads.py ~/Downloads --dry-run

# 恢复其他目录
python3 restore_downloads.py ~/Desktop
```

**特点：**
- ✅ 只处理 `organize.py` 创建的分类文件夹（`图片`、`文档`、`视频`、`音频`、`压缩包`、`代码`、`其他`）
- ✅ 跳过所有其他文件夹（你的原文件夹完全不动）
- ✅ 自动处理重名文件（`file_1.ext`、`file_2.ext`...）
- ✅ 自动删除已空的分类文件夹

| 参数 | 说明 |
|------|------|
| `folder` | 要整理的目录 |
| `--dry-run` | 预览模式，不移动文件 |

## 分类规则

| 分类 | 扩展名 |
|------|--------|
| 图片 | jpg, png, gif, svg, webp, ico |
| 文档 | pdf, doc, txt, md, xlsx, pptx |
| 视频 | mp4, avi, mkv, mov |
| 音频 | mp3, wav, flac |
| 压缩包 | zip, rar, 7z, tar.gz |
| 代码 | py, js, ts, html, css, json |
| 其他 | 未匹配的文件 |

## 示例

```bash
# 整理 Downloads，预览模式
python3 organize.py ~/Downloads --dry-run

# 整理 Desktop
python3 organize.py ~/Desktop
```

## License

MIT
