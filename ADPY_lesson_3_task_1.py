class FlatIterator:
	def __init__(self, matrix: list):
		self.matrix = [item for i in matrix for item in i]

	def __iter__(self):
		self.count = -1
		return self

	def __next__(self):
		self.count += 1
		if self.count == len(self.matrix):
			raise StopIteration
		return self.matrix[self.count]


nested_list = [
	['a', 'b', 'c'],
	['d', 'e', 'f'],
	[1, 2, None]
]
for item in FlatIterator(nested_list):
	print(item)