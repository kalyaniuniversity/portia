from portia_utils import file_handler as fh
from typing import List


def dlbcl_1000() -> List[str]:
    return fh.readfile('sample_datasets/dlbcl-sd-1000-attributes.txt', True)


def gse412_1000() -> List[str]:
    return fh.readfile('sample_datasets/gse412-sd-1000-attributes.txt', True)
