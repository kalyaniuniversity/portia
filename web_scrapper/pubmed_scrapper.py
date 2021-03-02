import requests
from bs4 import BeautifulSoup
from portia_types.associate_pubmed_article import ArticleDictionary
from typing import TypedDict
from typing import List
from web_scrapper import pubmed_data_fetcher as pdf


def fetch_article_details(tag: str) -> ArticleDictionary:
    article_link = "https://pubmed.ncbi.nlm.nih.gov" + tag

    html_content = requests.get(article_link).text
    soup = BeautifulSoup(html_content, "lxml")

    article_details: ArticleDictionary = {
        'link': article_link,
        'title': pdf.fetch_article_title(soup),
        'author': pdf.fetch_article_author(soup),
        'pm_id': pdf.fetch_article_pmId(soup),
        'pmc_id': pdf.fetch_article_pmcId(soup),
        'doi': pdf.fetch_article_doiId(soup),
        'abstruct': pdf.fetch_article_abstruct(soup)
    }

    return article_details


def fetch_article_details_list(tag_list: List[str], get_citation: bool = False) -> List[ArticleDictionary]:
    article_detail_list: List[ArticleDictionary] = []

    for tag in tag_list:
        article_detail_list.append(fetch_article_details(tag))

    if get_citation == True:
        from web_automator import pubmed_citation_automator as pca
        citation = pca.get_article_citation(tag_list)

        for i in range(len(article_detail_list)):
            article_detail_list[i]['citation'] = citation[i]

    return article_detail_list


def get_associate_search_result(tag, get_citation=False) -> List[ArticleDictionary]:

    generated_tag_list: List[str] = []

    # tag = tag.replace(' ', '+')
    url = "https://pubmed.ncbi.nlm.nih.gov/?term=" + tag.replace(' ', '+')

    html_content = requests.get(url).text
    soup = BeautifulSoup(html_content, "lxml")

    if 'No results were found.' in str(soup.find(
            "div", attrs={"class": "results-amount"}).text):
        print("Your Keyword is wrong")
        exit
    else:
        article_content = soup.find_all(
            "article", attrs={"class": "full-docsum"})

        for article in article_content:
            generated_tag_list.append(
                str(article.find("a", attrs={"class": "docsum-title"})['href']).strip())

    return fetch_article_details_list(generated_tag_list, get_citation)
