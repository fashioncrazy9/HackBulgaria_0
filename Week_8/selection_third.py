def min_elem(items,used):
    unused_indexes = diff(range(0,len(items)-1), used)

    min_index = unused_indexes[0]

    for index in unused_indexes:
        if items[index] < items[min_index]:
            min_index = index

    return min_index
used = [2,3]
items = [1,2,3,6]
print(min_elem(items,used))


def diff(a,b):
    unused = []

    for item in a:
        if item not in b:
            unused.append(item)

    return unused

#print(diff([1,2,3], [1,2]))


def selection_third(numbers):
    result = []
    n = len(numbers)
    used = []

    while len(result) != n:
        min_index = min_index_without_used(numbers, used)
        used.append(min_index)
        result.append(numbers[min_index])


    return result