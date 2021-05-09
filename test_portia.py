import portia as p
import json

from portia_api.associated_protein_manager import AssociatedProteinManager
from portia_types.associated_proteins import AssociatedProteins
from portia_api.pubmed_manager import PubmedManager
from portia_types.pubmed_article import ArticleDictionary
from portia_utils import file_handler as fh

from typing import List

apm: AssociatedProteinManager = p.apm()
pubmg: PubmedManager = p.pubmg()
keywords: List[str] = [
    'cancer',
    'cyst',
    'tumor',
    'tumour',
    'carcinoma',
    'malignant',
    'lymphoma',
    'lump',
    'leukemia',
    'oncology',
    'tubercle'
]


def prepare_dlbcl_100() -> None:
    prepare_article(
        'sample_datasets/dlbcl-100-selected.txt',
        keywords + ['dlbcl'],
        'sample_datasets/dlbcl-100-selected-articles.json'
    )


def prepare_dlbcl_1000() -> None:
    prepare_article(
        'sample_datasets/dlbcl-1000-selected.txt',
        keywords + ['dlbcl'],
        'sample_datasets/dlbcl-1000-selected-articles.txt'
    )


def prepare_dlbcl_all() -> None:
    prepare_article(
        'sample_datasets/dlbcl-all-selected.txt',
        keywords + ['dlbcl'],
        'sample_datasets/dlbcl-all-selected-articles.txt'
    )


def prepare_gse412_100() -> None:
    prepare_article(
        'sample_datasets/gse412-100-selected.txt',
        keywords + ['gse412', 'childALL', 'ALL', 'AML', 'ALL-AML', 'ChildALL'],
        'sample_datasets/gse412-100-selected-articles.json'
    )


def prepare_gse412_1000() -> None:
    prepare_article(
        'sample_datasets/gse412-1000-selected.txt',
        keywords + ['gse412', 'childALL', 'ALL', 'AML', 'ALL-AML', 'ChildALL'],
        'sample_datasets/gse412-1000-selected-articles.txt'
    )


def prepare_gse412_all() -> None:
    prepare_article(
        'sample_datasets/gse412-all-selected.txt',
        keywords + ['gse412', 'childALL', 'ALL', 'AML', 'ALL-AML', 'ChildALL'],
        'sample_datasets/gse412-all-selected-articles.txt'
    )


def prepare_leukemia_100() -> None:
    prepare_article(
        'sample_datasets/leukemia-100-selected.txt',
        keywords + ['ALL', 'AML', 'ALL-AML'],
        'sample_datasets/leukemia-100-selected-articles.json'
    )


def prepare_leukemia_1000() -> None:
    prepare_article(
        'sample_datasets/leukemia-1000-selected.txt',
        keywords + ['ALL', 'AML', 'ALL-AML'],
        'sample_datasets/leukemia-1000-selected-articles.json'
    )


def prepare_leukemia_all() -> None:
    prepare_article(
        'sample_datasets/leukemia-all-selected.txt',
        keywords + ['ALL', 'AML', 'ALL-AML'],
        'sample_datasets/leukemia-all-selected-articles.txt'
    )


def prepare_article(
        filename: str,
        keywordz: List[str],
        writefile: str
) -> None:

    gene_list: List[str] = fh.readfile(filename, rstrip=True)[0].split(',')
    associated_proteins_list: List[AssociatedProteins] = apm.fetch_associated_proteins_from_list(gene_list)
    total_count: int = 0
    article_content: str = '{"articles": ['

    for associated_proteins in associated_proteins_list:

        print('# gene name ->', associated_proteins['gene_name'])
        proteins: List[str] = associated_proteins['proteins']

        for protein in proteins:
            print('\t* protein ->', protein)
            if protein != "n/a":
                articles: List[ArticleDictionary] = pubmg.fetch_with_associated_keywords(
                    protein,
                    keywordz,
                    get_citation=True
                )
                total_count += len(articles)
                article_content += json.dumps(articles) + ','

    fh.writefile(
        writefile,
        article_content + '], "count":' + str(total_count) + '}'
    )


def main() -> None:
    # prepare_dlbcl_100() # done
    prepare_dlbcl_1000()
    # prepare_dlbcl_all()
    # prepare_gse412_100() # done
    # prepare_gse412_1000()
    # prepare_gse412_all()
    # prepare_leukemia_100() # done
    # prepare_leukemia_1000() # done
    # prepare_leukemia_all()


main()
