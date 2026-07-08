# py-file-organizer 📁

按扩展名自动整理文件到分类文件夹。

## 快速开始

```bash
python3 organize.py ~/Downloads
```

## 用法

```bash
python3 organize.py <目标文件夹> [--dry-run]
```

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
