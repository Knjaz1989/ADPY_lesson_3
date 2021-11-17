def flat_generator(matrix: list):
    count = 0
    matrix = [item for i in matrix for item in i]
    while count != len(matrix):
        yield matrix[count]
        count += 1


nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f'],
    [1, 2, None]
]

for item in flat_generator(nested_list):
    print(item)
