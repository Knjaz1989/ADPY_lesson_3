def flat_generator(matrix: list):
    count = 0
    while count != len(matrix):
        yield '\n'.join(matrix[count])
        count += 1


nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f'],
    ['g', 'h', 'i']
]

for item in flat_generator(nested_list):
    print(item)
