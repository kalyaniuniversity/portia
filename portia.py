from portia_api.associated_protein_manager import AssociatedProteinManager
from portia_api.entrez_id_manager import EntrezIDManager
from portia_api.pubmed_manager import PubmedManager


def get_entrez_id_manager() -> EntrezIDManager:
    return EntrezIDManager()


def get_associated_protein_manager() -> AssociatedProteinManager:
    return AssociatedProteinManager()


def get_pubmed_manager() -> PubmedManager:
    return PubmedManager()


def eim() -> EntrezIDManager:
    return get_entrez_id_manager()


def apm() -> AssociatedProteinManager:
    return get_associated_protein_manager()


def pubmg() -> PubmedManager:
    return get_pubmed_manager()
