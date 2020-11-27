from typing import List


def convert_list_string(list_content: List[str], separator: str = ",") -> str:

    content: str = ""

    for item in list_content:
        content += item + separator

    return content
