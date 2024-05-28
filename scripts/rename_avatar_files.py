import os
from pathlib import Path
import re


def rename_avatar_files(directory, x):
    files = os.listdir(directory)

    pattern = re.compile(r"^\d+\.png$")
    png_files = [f for f in files if pattern.match(f)]

    # Sort the files in descending order based on the numeric part of the filename
    png_files.sort(key=lambda f: int(f.split(".")[0]), reverse=True)

    # Rename each file by adding x to its numeric part
    for filename in png_files:
        number = int(filename.split(".")[0])
        new_number = number + x
        new_filename = f"{new_number}.png"

        old_path = os.path.join(directory, filename)
        new_path = os.path.join(directory, new_filename)

        os.rename(old_path, new_path)
        print(f"Renamed {old_path} to {new_path}")


if __name__ == "__main__":
    base_dir = Path(__file__).resolve().parent
    directory = base_dir.parent / "src" / "assets" / "avatars"
    rename_avatar_files(directory, 2)
