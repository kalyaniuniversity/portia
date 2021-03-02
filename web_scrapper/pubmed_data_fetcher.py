import requests
from bs4 import BeautifulSoup
from typing import List


def fetch_article_title(soup):
    return str(soup.find("h1", attrs={"class": "heading-title"}).text).strip()


def fetch_article_author(soup):
    authors_name: List[str] = list()
    div_content = soup.find("div", attrs={"class": "authors-list"})

    if div_content != None:
        author_list = div_content.find_all(
            "span", attrs={"class": "authors-list-item"})

        for author in author_list:
            authors_name.append(str(author.find("a").text).strip())

    else:
        authors_name.append("Authors Details not Available")

    return authors_name


def fetch_article_pmId(soup):
    return str(soup.find("strong", attrs={"class": "current-id", "title": "PubMed ID"}).text).strip()


def fetch_article_pmcId(soup):
    pmc_id: str = "PMC not Available"
    if soup.find("span", attrs={"class": "identifier pmc"}) != None:
        pmc_id = str(soup.find(
            "span", attrs={"class": "identifier pmc"}).find("a").text).strip()

    return pmc_id


def fetch_article_doiId(soup):
    doi_id: str = "DOI not Available"
    if soup.find("span", attrs={"class": "identifier doi"}) != None:
        doi_id = str(soup.find(
            "span", attrs={"class": "identifier doi"}).find("a").text).strip()

    return doi_id


def fetch_article_abstruct(soup):
    abstruct: str = "Abstrct is not Available"
    if "No abstract available" not in str(soup.find("div", attrs={"class": "abstract"}).text):
        abstruct = str(
            soup.find("div", attrs={"class": "abstract"}).find("p").text).strip()

    return abstruct
