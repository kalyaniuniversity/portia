from typing import List
from portia_types.associated_proteins import AssociatedProteins
from portia_utils import file_handler as fh
from portia_utils import util as u
from web_scrapper import reactome_scrapper as rs


class AssociatedProteinManager:

	@classmethod
	def fetch_associated_proteins(cls, gene_id: str) -> AssociatedProteins:

		proteins: List[str] = rs.get_associated_proteins(gene_id)
		associated_proteins: AssociatedProteins = {
			'gene_name': gene_id,
			'proteins': proteins
		}

		return associated_proteins

	@classmethod
	def fetch_associated_proteins_from_list(cls, gene_id_list: List[str]) -> List[AssociatedProteins]:

		associated_proteins_list: List[AssociatedProteins] = []

		for gene_id in gene_id_list:
			associated_proteins_list.append(cls.fetch_associated_proteins(gene_id))

		return associated_proteins_list

	@classmethod
	def fetch_associated_proteins_from_file(cls, complete_file_path: str) -> List[AssociatedProteins]:

		gene_id_list = List[str] = fh.readfile(complete_file_path, True)
		associated_proteins_list: List[AssociatedProteins] = cls.fetch_associated_proteins_from_list(gene_id_list)

		return associated_proteins_list

	@classmethod
	def fetch_associated_proteins_to_file(cls, complete_read_file_path: str, complete_write_file_path: str):
		associated_proteins_list: List[AssociatedProteins] = cls.fetch_associated_proteins_from_file(complete_read_file_path)
		fh.writefile(
			complete_write_file_path,
			u.convert_associated_proteins_list_to_string(
				associated_proteins_list
			)
		)

	@classmethod
	def fetch_associated_proteins_from_list_to_file(cls, gene_id_list: List[str], complete_write_file_path: str):
		associated_protein_list: List[AssociatedProteins] = cls.fetch_associated_proteins_from_list(gene_id_list)
		fh.writefile(
			complete_write_file_path,
			u.convert_associated_proteins_list_to_string(
				associated_protein_list
			)
		)
