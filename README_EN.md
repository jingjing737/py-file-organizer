# py-file-organizer 📁

Auto file organizer — sorts files into folders by extension.

## Quick Start

```bash
python3 organize.py ~/Downloads
```

## Usage

```bash
python3 organize.py <folder> [--dry-run]
python3 restore_downloads.py ~/Downloads   # restore
```

| Flag | Description |
|------|-------------|
| `folder` | Target directory |
| `--dry-run` | Preview only, no moves |

## Categories

| Category | Extensions |
|----------|------------|
| Images | jpg, png, gif, svg, webp, ico |
| Documents | pdf, doc, txt, md, xlsx, pptx |
| Videos | mp4, avi, mkv, mov |
| Audio | mp3, wav, flac |
| Archives | zip, rar, 7z, tar.gz |
| Code | py, js, ts, html, css, json |
| Other | unmatched files |

## License

MIT
