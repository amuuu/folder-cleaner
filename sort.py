TARGET_DIR = "./test_folder/"

TARGET_EXTENSIONS = {
    "Sorted_Docs": ["pdf", "csv", "pptx"],
    "Sorted_Archives": ["rar", "zip", "7z", "zst", "gzip"],
    "Sorted_Programs": ["exe", "msi"],
    "Sorted_Sounds": ["wav", "mp3"],
    "Sorted_Videos": ["mp4"],
    "Sorted_Photos": ["jpg", "jpeg", "png", "bmp"],
    "Sorted_VS Themes": ["vsix"],
    "Sorted_Fonts": ["ttf"],
    "Sorted_Codes": ["hpp", "cpp", "html", "css", "js", "o", "py"],
}

import os
from os import listdir
from os.path import isfile, join
from pathlib import Path


def isAllowed(file_path) -> bool:
    if "sort.py" in file_path:
        return False
    return True


if TARGET_DIR[-1] != "/":
    TARGET_DIR += "/"

files_adr_list = [f for f in listdir(TARGET_DIR) if isfile(join(TARGET_DIR, f))]

maps = {}
for file_adr in files_adr_list:
    print(file_adr)
    ext = file_adr.split(".")[-1]
    if not maps.get(ext):
        maps[ext] = []
    maps[ext].append(file_adr)

for target_ext_category in TARGET_EXTENSIONS:
    new_path_str = TARGET_DIR + target_ext_category + "/"
    path = Path(new_path_str)
    if not path.exists():
        path.mkdir()  # parents=True
        # path.mkdir(parents=True)
    for target_ext in TARGET_EXTENSIONS[target_ext_category]:
        if target_ext in maps:
            for file in maps[target_ext]:
                if isAllowed(file):
                    os.rename(TARGET_DIR + file, new_path_str + file)
