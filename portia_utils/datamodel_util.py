from typing import List, Union
import copy
from portia_datamodel import model as m


def get_list_of_list_from_datamatrix(datamatrix: m.DataMatrix) -> List[List[float]]:

	list_of_list: List[List[float]] = list()

	for sample in datamatrix.samples:
		list_of_list.append(sample.get_values())

	return list_of_list


def get_classlabeled_list_of_list_from_datamatrix(
		datamatrix: m.DataMatrix
) -> List[List[Union[float, str]]]:

	list_of_list: List[List[Union[float, str]]] = list()

	for sample in datamatrix.samples:
		values: List[Union[float, str]] = sample.get_values()
		values.append(sample.classlabel)
		list_of_list.append(values)

	return list_of_list


def get_label_separated_attributes(
		attribute_list: List[float],
		classlabels: List[str],
		unique_classlabels: List[str]
) -> List[List[float]]:

	label_separated_attributes: List[List[float]] = list()

	for label in unique_classlabels:

		similar_labeled_attributes: List[float] = list()

		for i in range(0, len(attribute_list)):
			if classlabels[i] == label:
				similar_labeled_attributes.append(attribute_list[i])

		label_separated_attributes.append(copy.deepcopy(similar_labeled_attributes))

	return label_separated_attributes


def get_column(list_of_list: List[List], index: int) -> List:

	column: List = list()

	for row in list_of_list:
		column.append(row[index])

	return column

