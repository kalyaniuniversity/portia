from web_scrapper import reactome_search_result_scrapper as rs
from portia_utils import file_handler as fh
from portia_utils import util as u
from typing import List


def fetch_searched_result(gene_id: str):
    return rs.get_searched_result(gene_id)


def fetch_searched_result_from_list(gene_id_list: List[str]) -> List[str]:

    searched_result: List[str] = []

    for gene_id in gene_id_list:
        searched_result.append(fetch_searched_result(gene_id))

    return searched_result


def fetch_searched_result_from_file(complete_file_path: str):

    gene_id_list: List[str] = fh.readfile(complete_file_path, True)
    searched_result_list: List[str] = fetch_searched_result_from_list(
        gene_id_list)

    return searched_result_list


def fetch_searched_result_to_file(complete_read_file_path: str, complete_write_file_path: str):

    searched_result_list: List[str] = fetch_searched_result_from_file(
        complete_read_file_path)
    fh.writefile(
        complete_write_file_path,
        u.convert_2D_list_string(
            searched_result_list
        )
    )


def fetch_searched_result_from_list_to_file(gene_id_list: List[str], complete_write_file_path: str):

    searched_result_list: List[str] = fetch_searched_result_from_list(
        gene_id_list)
    fh.writefile(
        complete_write_file_path,
        u.convert_2D_list_string(
            searched_result_list
        )
    )


if __name__ == "__main__":
    gene_id_list: List[str] = ['u58522_at', 'X02160_at', 'D87436_at']
    complete_write_file_path: str = "OutputFile.txt"

    fetch_searched_result_from_list_to_file(
        gene_id_list,
        complete_write_file_path)
