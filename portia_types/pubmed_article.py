from typing import List
from typing import Optional
from typing import TypedDict


class ArticleDictionary(TypedDict):
    link: str
    title: str
    author: List[str]
    pm_id: str
    pmc_id: str
    doi: str
    abstract: str
    citation: Optional[str]
