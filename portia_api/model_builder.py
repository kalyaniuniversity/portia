import copy
import os
from typing import List
import anndata as ad
import scanpy as sc
from portia_utils import csv_handler as csv
from portia_datamodel import model as m
from portia_utils import util as u
from portia_utils import file_handler as fh


class ModelBuilder:

	@classmethod
	def build_model_from_csv(
			cls,
			filename: str,
			separator: str = ',',
			rstrip: bool = True
	) -> m.DataMatrix:
		return m.DataMatrix.from_list_of_list(list_of_list=csv.readcsv(filename, separator=separator, rstrip=rstrip))

	@classmethod
	def build_model_from_selected_attributes(
			cls,
			filename: str,
			attributes: List[str],
			separator: str = ',',
			rstrip: bool = True
	) -> m.DataMatrix:
		return cls.build_subset_from_selected_attributes(
			cls.build_model_from_csv(filename, separator=separator, rstrip=rstrip),
			attributes
		)

	@classmethod
	def bmfsa(cls, f: str, a: List[str], s: str = ',', rs: bool = True) -> m.DataMatrix:
		return cls.build_model_from_selected_attributes(f, a, separator=s, rstrip=rs)

	@classmethod
	def build_subset_from_selected_attributes(
			cls,
			datamatrix: m.DataMatrix,
			attributes: List[str]
	) -> m.DataMatrix:

		new_samples: List[m.Sample] = list()

		for sample in datamatrix.samples:
			new_samples.append(m.Sample(
				sample.get_datapoints([
					datamatrix.attributes.index(attribute.strip()) for attribute in attributes
				]),
				associated_attributes=copy.deepcopy(attributes),
				classlabel=sample.classlabel
			))

		return m.DataMatrix(
			new_samples,
			attributes=copy.deepcopy(attributes),
			classlabels=copy.deepcopy(datamatrix.classlabels),
			unique_classlabels=copy.deepcopy(datamatrix.unique_classlabels),
			dataset_name=datamatrix.dataset_name
		)

	@classmethod
	def bfsfa(cls, d: m.DataMatrix, a: List[str]) -> m.DataMatrix:
		return cls.build_subset_from_selected_attributes(d, a)

	@classmethod
	def bmsa(
			cls,
			filename: str,
			attributes: List[str],
			separator: str = ',',
			rstrip: bool = True
	) -> m.DataMatrix:
		return cls.build_model_from_selected_attributes(filename, attributes, separator=separator, rstrip=rstrip)

	@classmethod
	def read_as_anndata(
			cls,
			list_of_list: List[List[float]],
			roundoff_decimal: int = 5,
			filename: str = None
	) -> ad.AnnData:

		temp_folder: str = '__temp__'
		complete_file_path: str = os.path.join(temp_folder, filename)

		list_of_list = [[u.roundoff(value, roundoff_decimal) for value in row] for row in list_of_list]

		fh.create_path_if_not_exists(temp_folder)
		csv.writecsv(filename, list_of_list, directory=temp_folder)

		return sc.read_csv(complete_file_path)

	@classmethod
	def rad(
			cls,
			list_of_list: List[List[float]],
			roundoff_decimal: int = 5,
			filename: str = None
	) -> ad.AnnData:
		return cls.read_as_anndata(list_of_list, roundoff_decimal=roundoff_decimal, filename=filename)
