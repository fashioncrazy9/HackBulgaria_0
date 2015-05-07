#Gergana Karadzhova

def last(items):
    return items[len(items)-1]

#print(last([1,2,3,4]))


def second_to_last(items):
    return items[len(items) -2]

#print(second_to_last([1,2,3,4]))

def drop_last(items):
    result =[]

    for index in range (0, len(items) -1):
        item = items[index]
        result += [item]

    return result

#print(drop_last([1,2,3,4]))

def remove_duplicates(items):
    result = []

    for item in items:
        if item not in result:
            result += [item]

    return result 

def second_largest(numbers):

    numbers = sorted(numbers)
    numbers = remove_duplicates(numbers)
    
    all_same = True

    for index in range(0, len(numbers)):
        if numbers[index] != numbers[0]:
            all_same = False

    if len(numbers) < 2 or all_same == True:
        return False
    else:
            while last(numbers) == second_to_last(numbers):
                drop_last(numbers)

            return numbers[len(numbers)-2]

print(second_largest([89, 33, -22]))

b =  [5, 5, 4]
print(second_largest(b))


