from typing import List


class PubmedDataFetcher:

    @classmethod
    def fetch_article_title(cls, soup) -> str:
        return str(soup.find("h1", attrs={"class": "heading-title"}).text).strip()

    @classmethod
    def fetch_article_author(cls, soup) -> List[str]:

        authors_name: List[str] = list()
        div_content = soup.find("div", attrs={"class": "authors-list"})

        if div_content is not None:
            author_list = div_content.find_all("span", attrs={"class": "authors-list-item"})
            for author in author_list:
                authors_name.append(str(author.find("a").text).strip())
        else:
            authors_name.append("n/a")

        return authors_name

    @classmethod
    def fetch_article_pm_id(cls, soup) -> str:
        return str(soup.find("strong", attrs={"class": "current-id", "title": "PubMed ID"}).text).strip()

    @classmethod
    def fetch_article_pmc_id(cls, soup) -> str:
        pmc_id: str = "n/a"
        if soup.find("span", attrs={"class": "identifier pmc"}) is not None:
            pmc_id = str(soup.find("span", attrs={"class": "identifier pmc"}).find("a").text).strip()
        return pmc_id

    @classmethod
    def fetch_article_doi_id(cls, soup) -> str:
        doi_id: str = "n/a"
        if soup.find("span", attrs={"class": "identifier doi"}) is not None:
            doi_id = str(soup.find("span", attrs={"class": "identifier doi"}).find("a").text).strip()
        return doi_id

    @classmethod
    def fetch_article_abstract(cls, soup) -> str:
        abstract: str = "n/a"
        if "No abstract available" not in str(soup.find("div", attrs={"class": "abstract"}).text):
            abstract = str(soup.find("div", attrs={"class": "abstract"}).find("p").text).strip()
        return abstract
