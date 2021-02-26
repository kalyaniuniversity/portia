from typing import List, Union
from portia_datastructure import model as m


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
