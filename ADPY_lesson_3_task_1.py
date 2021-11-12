class FlatIterator:
	def __init__(self, matrix: list):
		self.matrix = matrix

	def __iter__(self):
		self.count = -1
		return self

	def __next__(self):
		self.count += 1
		if self.count == len(self.matrix):
			raise StopIteration
		trio = '\n'.join(self.matrix[self.count])
		return trio


nested_list = [
	['a', 'b', 'c'],
	['d', 'e', 'f'],
	['g', 'h', 'i']
]
for item in FlatIterator(nested_list):
	print(item)