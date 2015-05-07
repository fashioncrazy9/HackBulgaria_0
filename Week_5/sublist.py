def tail(items):
    result = []

    for index in range(1,len(items)):
        result += [items[index]]

    return result


def take(n, items):
    result = []

    for index in range(min(n, len(items))):
        result += [items[index]]

    return result


def sublist(l1, l2):

    n = len(l1)

    while len(l2) != 0:
        if take(n,l2) == l1:
            return True

        l2 = tail(l2)

    return False

l1 = [1,2,3,4]
l2 = [0,0,1,2,3]
print(sublist(l1,l2))