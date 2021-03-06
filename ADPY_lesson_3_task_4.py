def recursion(item_list: list):
    new_list = []
    for element in item_list:
        if isinstance(element, list):
            new_list.extend(recursion(element))
        else:
            new_list.append(element)
    return new_list

def flat_generator(matrix: list):
    count = 0
    matrix = recursion([item for i in matrix for item in i])
    while count != len(matrix):
        yield matrix[count]
        count += 1


nested_list = [
    [['a', [1, 2]], ['b', 3, 4], 'c'],
    ['d', 'e', 'f'],
    [1, 2, None]
]

for item in flat_generator(nested_list):
    print(item)
