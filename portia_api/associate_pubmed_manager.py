from typing import List
from portia_types.associate_pubmed_article import ArticleDictionary
from portia_utils import file_handler as fh
from portia_utils import util as u
from web_scrapper import pubmed_scrapper as ps


class AssociatedPubmedManager:

    @classmethod
    def fetch_associated_pubmed_result(cls, data: str, get_citation: bool = False) -> List[ArticleDictionary]:

        pubmed_result: List[ArticleDictionary] = ps.get_associate_search_result(
            data, get_citation)

        return pubmed_result
