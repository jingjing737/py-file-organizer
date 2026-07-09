#!/usr/bin/env python3
"""
restore_downloads.py — 恢复 Downloads 整理
只恢复 organize.py 创建的分类文件夹（图片/代码/其他/压缩包/文档/视频/音频）
"""
import os
import shutil
from pathlib import Path

# organize.py 创建的分类文件夹（白名单）
CATEGORIES = {"图片", "文档", "视频", "音频", "压缩包", "代码", "其他"}


def restore(folder: str, dry_run: bool = False):
    path = Path(folder)
    if not path.is_dir():
        print(f"❌ 目录不存在：{folder}")
        return

    moved = 0
    
    for cat_dir in sorted(path.iterdir()):
        if not cat_dir.is_dir():
            continue
        # 只处理分类文件夹
        if cat_dir.name not in CATEGORIES:
            print(f"⏭️  跳过非分类文件夹：{cat_dir.name}/")
            continue
            
        # 遍历子文件夹里的文件
        for item in cat_dir.iterdir():
            if item.is_file():
                dest = path / item.name
                # 处理重名
                if dest.exists():
                    stem = item.stem
                    suffix = item.suffix
                    counter = 1
                    while dest.exists():
                        dest = path / f"{stem}_{counter}{suffix}"
                        counter += 1
                
                if not dry_run:
                    shutil.move(str(item), str(dest))
                print(f"{'[模拟]' if dry_run else '移动'} {cat_dir.name}/{item.name} → {item.name}")
                moved += 1

    print(f"\n✅ {'模拟' if dry_run else '恢复'}完成，共处理 {moved} 个文件")
    if not dry_run:
        # 删除已空的分类文件夹
        for cat_dir in path.iterdir():
            if cat_dir.is_dir() and cat_dir.name in CATEGORIES:
                try:
                    remaining = list(cat_dir.iterdir())
                    if not remaining:
                        cat_dir.rmdir()
                        print(f"🗑️  删除空文件夹：{cat_dir.name}/")
                    else:
                        print(f"⚠️  {cat_dir.name}/ 还有文件未移动")
                except OSError as e:
                    print(f"⚠️  无法删除 {cat_dir.name}/: {e}")


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="恢复 Downloads 整理")
    parser.add_argument("folder", help="Downloads 目录", default=os.path.expanduser("~/Downloads"), nargs="?")
    parser.add_argument("--dry-run", action="store_true", help="只预览，不移动")
    args = parser.parse_args()
    restore(args.folder, args.dry_run)
