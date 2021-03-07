from typing import List
from bs4 import Tag


class PubmedDataFetcher:

    @staticmethod
    def fetch_article_title(soup) -> str:
        return str(soup.find("h1", attrs={"class": "heading-title"}).text).strip()

    @staticmethod
    def fetch_article_author(soup) -> List[str]:

        authors_name: List[str] = list()
        div_content: Tag = soup.find("div", attrs={"class": "authors-list"})

        if div_content is not None:
            author_list = div_content.find_all("span", attrs={"class": "authors-list-item"})
            for author in author_list:
                authors_name.append(str(author.find("a").text).strip())
        else:
            authors_name.append("n/a")

        return authors_name

    @staticmethod
    def fetch_article_pm_id(soup) -> str:
        return str(soup.find("strong", attrs={"class": "current-id", "title": "PubMed ID"}).text).strip()

    @staticmethod
    def fetch_article_pmc_id(soup) -> str:

        pmc_id: str = "n/a"
        span: Tag = soup.find("span", attrs={"class": "identifier pmc"})

        if span is not None:
            if span.find("a") is not None:
                pmc_id = str(soup.find("span", attrs={"class": "identifier pmc"}).find("a").text).strip()
            elif span.find("strong", attrs={"class": "current-id"}) is not None:
                pmc_id = str(span.find("strong", attrs={"class": "current-id"}).text).strip()

        return pmc_id

    @staticmethod
    def fetch_article_doi_id(soup) -> str:
        doi_id: str = "n/a"
        if soup.find("span", attrs={"class": "identifier doi"}) is not None:
            doi_id = str(soup.find("span", attrs={"class": "identifier doi"}).find("a").text).strip()
        return doi_id

    @staticmethod
    def fetch_article_abstract(soup) -> str:
        abstract: str = "n/a"
        if "No abstract available" not in str(soup.find("div", attrs={"class": "abstract"}).text):
            abstract = str(soup.find("div", attrs={"class": "abstract"}).find("p").text).strip()
        return abstract
