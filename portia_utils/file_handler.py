from typing import List
import os
import glob


def readfile(filename: str, rstrip: bool = False) -> List[str]:

    lines: List[str] = list()

    with open(filename, 'r') as datafile:
        for line in datafile:
            if rstrip:
                line = line.rstrip()
            lines.append(line)

    return lines


def writefile(filename: str, content: str):
    writer = open(filename, 'w+')
    writer.write(content)
    writer.close()


def is_valid_path(path: str) -> bool:
    return os.path.exists(path)


def create_path_if_not_exists(path: str):
    if not is_valid_path(path):
        os.mkdir(path)


def clear_temp():

    temp_folder: str = '__temp__'

    if not is_valid_path(temp_folder):
        return

    filelist = glob.glob(os.path.join(temp_folder, '*'))

    for f in filelist:
        if is_valid_path(os.path.join(f)):
            os.remove(f)
