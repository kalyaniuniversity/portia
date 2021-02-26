from typing import List
import random
import string
import math
from portia_types.associated_proteins import AssociatedProteins


def hash(length=10) -> str:
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))


def decimal_points(value: float) -> int:

    value = str(value)

    if '.' not in value:
        return 0
    return len(value.split('.')[1])


def roundoff(value: float, decimal_place: int, force_completion: bool = False) -> float:
    decimal_place: float = pow(10, decimal_place)
    rounded_value: float = math.ceil(value * decimal_place) / decimal_place

    if force_completion:
        while decimal_points(rounded_value) != decimal_place:
            rounded_value = float(str(rounded_value) + '0')

    return rounded_value


def convert_list_string(list_content: List[str], separator: str = ",") -> str:

    content: str = ""

    for item in list_content:
        content += item + separator

    return content


def equal_lists(list1: List[float], list2: List[float], tolerance: float = 0.0) -> bool:

    if len(list1) != len(list2):
        return False

    for i in range(len(list1)):
        if not math.isclose(
                list1[i],
                list2[i],
                rel_tol=tolerance
        ) and not math.isclose(list1[i], list2[i], abs_tol=tolerance):
            return False

    return True


def convert_associated_proteins_to_string(associated_proteins: AssociatedProteins) -> str:
    return associated_proteins['gene_name'] + ' -> ' + convert_list_string(associated_proteins['proteins'])


def convert_associated_proteins_list_to_string(associated_proteins_list: List[AssociatedProteins]) -> str:

    content: str = ''

    for associated_proteins in associated_proteins_list:
        content += convert_associated_proteins_to_string(associated_proteins) + '\n'

    return content
