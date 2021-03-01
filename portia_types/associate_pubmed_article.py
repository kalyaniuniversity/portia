from typing import TypedDict
from typing import List


class ArticleDictionary(TypedDict):
    link: str
    title: str
    author: List[str]
    pm_id: str
    pmc_id: str
    doi: str
    abstruct: str
    citation: str
