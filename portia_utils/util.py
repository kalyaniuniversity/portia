from typing import List
from portia_types.associated_proteins import AssociatedProteins


def convert_list_string(list_content: List[str], separator: str = ",") -> str:

    content: str = ""

    for item in list_content:
        content += item + separator

    return content


def convert_associated_proteins_to_string(associated_proteins: AssociatedProteins) -> str:
    return associated_proteins['gene_name'] + ' -> ' + convert_list_string(associated_proteins['proteins'])


def convert_associated_proteins_list_to_string(associated_proteins_list: List[AssociatedProteins]) -> str:

    content: str = ''

    for associated_proteins in associated_proteins_list:
        content += convert_associated_proteins_to_string(associated_proteins) + '\n'

    return content
