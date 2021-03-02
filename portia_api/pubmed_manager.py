from typing import List

from portia_types.pubmed_article import ArticleDictionary
from web_scrapper import pubmed_scrapper as ps


class PubmedManager:

    @classmethod
    def fetch_associated_pubmed_result(
            cls,
            data: str,
            get_citation: bool = False
    ) -> List[ArticleDictionary]:

        pubmed_result: List[ArticleDictionary] = ps.get_associate_search_result(
            data,
            get_citation
        )

        return pubmed_result
