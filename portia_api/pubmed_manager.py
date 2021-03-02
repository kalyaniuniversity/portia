from typing import List

from portia_types.pubmed_article import ArticleDictionary
from web_scrapper.pubmed_scrapper import PubMedScrapper


class PubmedManager:

    _scrapper: PubMedScrapper

    def __init__(self):
        self._scrapper = PubMedScrapper()

    @classmethod
    def fetch_associated_pubmed_result(
            cls,
            data: str,
            get_citation: bool = False
    ) -> List[ArticleDictionary]:

        pubmed_result: List[ArticleDictionary] = cls._scrapper.get_associate_search_result(
            data,
            get_citation
        )

        return pubmed_result
