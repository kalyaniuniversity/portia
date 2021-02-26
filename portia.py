from portia_api.entrez_id_manager import EntrezIDManager
from portia_api.associated_protein_manager import AssociatedProteinManager


def get_entrez_id_manager() -> EntrezIDManager:
    return EntrezIDManager()


def get_associated_protein_manager() -> AssociatedProteinManager:
    return AssociatedProteinManager()


def eim() -> EntrezIDManager:
    return get_entrez_id_manager()


def apm() -> AssociatedProteinManager:
    return get_associated_protein_manager()
