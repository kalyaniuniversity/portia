from typing import TypedDict
from typing import List


class AssociatedProteins(TypedDict):
	gene_name: str
	proteins: List[str]
