class FlatIterator:
	def __init__(self, matrix: list):
		self.matrix = [item for i in matrix for item in i]

	def recursion(self, item_list: list):
		new_list = []
		for element in item_list:
			if isinstance(element, list):
				new_list.extend(self.recursion(element))
			else:
				new_list.append(element)
		return new_list

	def __iter__(self):
		self.count = -1
		self.matrix = self.recursion(self.matrix)
		return self

	def __next__(self):
		self.count += 1
		if self.count == len(self.matrix):
			raise StopIteration
		return self.matrix[self.count]


nested_list = [
	[['a', [1, 2]], ['b', 3, 4], 'c'],
	['d', 'e', 'f'],
	[1, 2, None]
]
for item in FlatIterator(nested_list):
	print(item)
