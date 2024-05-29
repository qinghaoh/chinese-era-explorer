import os
from pathlib import Path
import re
import argparse


def rename_avatar_files(directory, delta=0, lower_bound=0, upper_bound=1000):
    if delta == 0:
        return

    files = os.listdir(directory)

    pattern = re.compile(r"^\d+\.png$")
    png_files = [f for f in files if pattern.match(f)]

    # Sort the files based on the numeric part of the filename
    png_files.sort(key=lambda f: int(f.split(".")[0]), reverse=(delta > 0))

    # Rename each file by adding delta to its numeric part
    for filename in png_files:
        number = int(filename.split(".")[0])
        if number < lower_bound or number > upper_bound:
            continue

        new_number = number + delta
        new_filename = f"{new_number}.png"

        old_path = os.path.join(directory, filename)
        new_path = os.path.join(directory, new_filename)

        os.rename(old_path, new_path)
        print(f"Renamed {old_path} to {new_path}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Rename avatar files by incrementing their numeric part."
    )
    parser.add_argument(
        "--delta",
        type=int,
        required=True,
        help="The increment value to add to the numeric part of the filename.",
    )
    parser.add_argument(
        "--lower_bound",
        type=int,
        help="The lower bound value to filter the files to be renamed.",
    )
    parser.add_argument(
        "--upper_bound",
        type=int,
        help="The upper bound value to filter the files to be renamed.",
    )

    args = parser.parse_args()

    base_dir = Path(__file__).resolve().parent
    directory = base_dir.parent / "src" / "assets" / "avatars"

    rename_avatar_files(directory, args.delta, args.lower_bound, args.upper_bound)
