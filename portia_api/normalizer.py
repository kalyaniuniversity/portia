import statistics as st


class Normalizer:

	@classmethod
	def zscore(cls, value, value_list):
		return (value - st.mean(value_list)) / st.stdev(value_list)

	@classmethod
	def minmax(
			cls,
			value,
			actual_min,
			actual_max,
			normalized_min,
			normalized_max
	):
		return (
				(
					(value - actual_min) / (actual_max - actual_min)
				) * (normalized_max - normalized_min)
		) + normalized_min
