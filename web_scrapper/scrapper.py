import requests
from bs4 import BeautifulSoup as bs
from bs4 import Tag

from typing import Dict


def get_dom(url: str) -> bs:
    return bs(
        requests.get(url).text,
        "lxml"
    )


def get_div_content(dom: bs, attrs: Dict[str, str]) -> Tag:
    return dom.find('div', attrs=attrs)
