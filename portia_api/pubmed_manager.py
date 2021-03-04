from typing import List
from portia_types.pubmed_article import ArticleDictionary
from web_scrapper.pubmed_scrapper import PubMedScrapper


class PubmedManager:

    _scrapper: PubMedScrapper

    def __init__(self):
        self._scrapper = PubMedScrapper()

    def fetch_result(
            self,
            data: str,
            get_citation: bool = False
    ) -> List[ArticleDictionary]:

        pubmed_result: List[ArticleDictionary] = self._scrapper.get_search_result(
            data,
            get_citation
        )

        return pubmed_result
