from typing import List
from bs4 import BeautifulSoup
from bs4 import PageElement
from bs4 import ResultSet
from bs4 import Tag
from web_automator import gene_card_automator as gca
from web_scrapper import scrapper as sc


def _prepare_url(tag: str) -> str:
    return "https://reactome.org/content/query?q=" + tag


def scrape_details_page(url: str) -> str:

    dom: BeautifulSoup = sc.get_dom(url)
    div_content: Tag = sc.get_div_content(dom, attrs={"id": "fav-lead1"})
    search_results: ResultSet = div_content.find_all(
        'div',
        attrs={
            "class": "favth-col-lg-10 favth-col-md-10 favth-col-sm-9 favth-col-xs-12 details-field"
        }
    )
    entrez_id: str = ""

    for result in search_results:

        link: PageElement = result.find('a', href=True)

        if link is not None:
            if "https://www.genecards.org/cgi-bin/carddisp.pl?gene=" in str(link):
                gene_card_url = link['href']
                entrez_id = gca.get_entrez_id(gene_card_url)

    return entrez_id


def get_entrez_id(gene_tag: str) -> str:

    url: str = _prepare_url(gene_tag)
    dom: BeautifulSoup = sc.get_dom(url)
    div_content: Tag = sc.get_div_content(dom, attrs={"id": "fav-lead1"})
    h3_element: PageElement = div_content.find('h3')

    if "No results found" in str(h3_element):
        return "n/a"
    else:
        search_result: PageElement = div_content.find(
            'div',
            attrs={
                "id": "search-results"
            }
        )
        href_link: Tag = search_result.a['href']
        href_link_text: str = str(href_link)
        details_url: str = href_link_text.replace(
            './detail',
            'https://reactome.org/content/detail'
        )
        return scrape_details_page(details_url)


def get_associated_proteins(gene_tag: str) -> List[str]:

    result: List[str] = []

    url: str = _prepare_url(gene_tag)
    dom: BeautifulSoup = sc.get_dom(url)
    div_content: Tag = sc.get_div_content(dom, attrs={"id": "fav-lead1"})
    h3_element: PageElement = div_content.find('h3')

    if "No results found" in str(h3_element):
        result.append("n/a")
        return result
    else:
        searched_result: ResultSet = div_content.find_all(
            "h4", attrs={"class": "title"})
        for data in searched_result:
            result.append(data.find("a").text)

    return result
