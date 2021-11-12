class FlatIterator:
	def __init__(self, matrix: list):
		self.matrix = matrix

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
		return self

	def __next__(self):
		self.count += 1
		if self.count == len(self.matrix):
			raise StopIteration
		words_line = '\n'.join(self.recursion(self.matrix[self.count]))
		return words_line


nested_list = [
	[['a', ['1', '2']], ['b', '3', '4'], 'c'],
	['d', 'e', 'f'],
	['g', 'h', 'i']
]
for item in FlatIterator(nested_list):
	print(item)
