def head(items): 
    return items[0]

print(head([1,2,3,4]))


def last(items):
    return items[len(items)-1]

print(last([1,2,3,4]))


def tail(items):
    result =[]

    for index in range (1, len(items)):
        item = items[index]
        result += [item]

    return result

print(tail([1,2,3,4]))

def equal_lists(items1, items2):

    if len(items1) != len(items2):
        return False

    for index in range(0, len(items1)):
        if items1[index] != items2[index]:
            return False

    return True

print(equal_lists([1,2,3],[1,2,3])) 

def count_item(element, items):

    count = 0

    for item in items:
        if element == item:
            count += 1

    return count

print(count_item(5, [1, 2, 3, 4, 5]))
print(count_item("winter", ["winter", "winter"]))
print(count_item(False, [True, True]))

def take(n, items):
    if n > len(items):
        n = len(items)

    index = 0
    new_list = []

    while index < n:
        new_list = new_list + [items[index]]
        index += 1

    return new_list

print(take(3, [3, 4, 5, 6, 7, 8]))
print(take(10, [1,2]))

def drop (n, items):
    result = []

    for index in range(n, len(items)):
        result += [items[index]]

    return result























