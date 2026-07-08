#!/usr/bin/env python3
"""
py-file-organizer — 按扩展名自动整理文件
支持：图片、文档、视频、音频、压缩包、代码、其他
"""
import os
import shutil
from pathlib import Path

CATEGORIES = {
    "图片": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".webp", ".ico"],
    "文档": [".pdf", ".doc", ".docx", ".txt", ".md", ".xls", ".xlsx", ".ppt", ".pptx"],
    "视频": [".mp4", ".avi", ".mkv", ".mov", ".wmv", ".flv"],
    "音频": [".mp3", ".wav", ".flac", ".aac", ".ogg"],
    "压缩包": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "代码": [".py", ".js", ".ts", ".html", ".css", ".java", ".cpp", ".c", ".json", ".yaml", ".yml"],
}

def organize(folder: str, dry_run: bool = False):
    path = Path(folder)
    if not path.is_dir():
        print(f"❌ 目录不存在：{folder}")
        return

    moved = 0
    for item in path.iterdir():
        if item.is_file() and item.name != "organize.py":
            ext = item.suffix.lower()
            target_dir = "其他"
            for cat, exts in CATEGORIES.items():
                if ext in exts:
                    target_dir = cat
                    break
            dest = path / target_dir / item.name
            if not dry_run:
                (path / target_dir).mkdir(exist_ok=True)
                shutil.move(str(item), str(dest))
            print(f"{'[模拟]' if dry_run else '移动'} {item.name} → {target_dir}/")
            moved += 1

    print(f"\n✅ {'模拟' if dry_run else '整理'}完成，共处理 {moved} 个文件")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="按扩展名整理文件")
    parser.add_argument("folder", help="要整理的目录")
    parser.add_argument("--dry-run", action="store_true", help="只预览，不移动")
    args = parser.parse_args()
    organize(args.folder, args.dry_run)
