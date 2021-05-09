from typing import List
from typing import Iterator
from portia_types.pubmed_article import ArticleDictionary
from web_scrapper.pubmed_scrapper import PubMedScrapper


class PubmedManager:

    _scrapper: PubMedScrapper

    def __init__(self):
        self._scrapper = PubMedScrapper()

    def fetch(
            self,
            search_term: str,
            get_citation: bool = False
    ) -> List[ArticleDictionary]:
        pubmed_result: List[ArticleDictionary] = self._scrapper.get_search_result(
            search_term,
            get_citation
        )
        return pubmed_result

    def fetch_with_associated_keywords(
            self,
            search_term: str,
            keywords: List[str],
            get_citation: bool = False
    ) -> List[ArticleDictionary]:
        results: List[ArticleDictionary] = self.fetch(search_term, get_citation=get_citation)
        filtered: Iterator[ArticleDictionary] = filter(
            lambda item: PubmedManager.filter_by_keyword(item, keywords),
            results
        )
        return [article for article in filtered]

    def fask(
            self,
            search_term: str,
            keywords: List[str],
            get_citation: bool = False
    ) -> List[ArticleDictionary]:
        return self.fetch_with_associated_keywords(search_term, keywords, get_citation=get_citation)

    @staticmethod
    def filter_by_keyword(article: ArticleDictionary, keywords: List[str]):
        for word in keywords:
            if word.lower() in article['title'].lower() or word.lower()in article['abstract'].lower():
                return True
        return False
