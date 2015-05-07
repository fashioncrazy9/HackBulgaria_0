def setify(a):
    result = []

    for item in a:
        if item not in result:
            result.append(item)

    return result


def diff(a, b):
    result = []

    for item in a:
        if item not in b:
            result.append(item)
    return setify(result)
    
def union(a, b):
    result =[]

    for item in a + b:
        if item not in result:
            result.append(item)

    return setify(result)

def union2(a,b):
    return setify(a+b)


def intersection(a,b):
    result = []

    for item in a:
        if item in b:
            result.append(item)

    return setify(result)


def cartesian_product(a, b):
    result = []
    a1 = setify(a)
    b1 = setify(b)

    for item1 in a1:
        for item2 in b1:
            result.append((item1,item2))

    return result


print(setify([0, 1, 1, 5, 5, 6]) == [0, 1, 5, 6])
print(union([0, 0, 0, 0, 0], [1, 2]) == [0, 1, 2])
print(intersection([0, 0, 1, 2, 5], [5, 5, 6]) == [5])
print(diff([0, 1, 2, 3, 4, 5], [0, 0, 1, 1, 2, 2, 3, 3]) == [4, 5])
print(cartesian_product([0, 1], [1]) == [(0, 1), (1, 1)])


