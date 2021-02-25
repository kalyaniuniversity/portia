from typing import List


def convert_list_string(list_content: List[str], separator: str = ",") -> str:

    content: str = ""

    for item in list_content:
        content += item + separator

    return content


def convert_2D_list_string(list_content):

    content: str = ""

    for data in list_content:
        for i in range(len(data)):
            if i != len(data)-1:
                content += data[i] + ","
            else:
                content += data[i]
        content += "\n"

    return content
