from portia_api.entrez_id_manager import EntrezIDManager
from portia_api.associated_protein_manager import AssociatedProteinManager
from portia_api.associate_pubmed_manager import AssociatedPubmedManager


def get_entrez_id_manager() -> EntrezIDManager:
    return EntrezIDManager()


def get_associated_protein_manager() -> AssociatedProteinManager:
    return AssociatedProteinManager()


def get_associated_pubmed_manager() -> AssociatedPubmedManager:
    return AssociatedPubmedManager()


def eim() -> EntrezIDManager:
    return get_entrez_id_manager()


def apm() -> AssociatedProteinManager:
    return get_associated_protein_manager()


def pubmg() -> AssociatedPubmedManager:
    return AssociatedPubmedManager()
