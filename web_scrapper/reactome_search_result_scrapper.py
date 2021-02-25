from web_scrapper import scrapper as sc
from bs4 import BeautifulSoup
from bs4 import PageElement
from bs4 import Tag
from bs4 import ResultSet


def _prepare_url(tag: str) -> str:
    return "https://reactome.org/content/query?q=" + tag


def get_searched_result(gene_tag: str) -> str:
    result: List[str] = []

    url: str = _prepare_url(gene_tag)
    dom: BeautifulSoup = sc.get_dom(url)
    div_content: Tag = sc.get_div_content(dom, attrs={"id": "fav-lead1"})
    h3_element: PageElement = div_content.find('h3')
    entrez_id: str = ""

    if "No results found" in str(h3_element):
        result.append("n/a")
        return result
    else:
        searched_result = div_content.find_all("h4", attrs={"class": "title"})
        for data in searched_result:
            result.append(data.find("a").text)

    return result
