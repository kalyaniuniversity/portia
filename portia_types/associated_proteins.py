from typing import List
from typing import TypedDict


class AssociatedProteins(TypedDict):
	gene_name: str
	proteins: List[str]
