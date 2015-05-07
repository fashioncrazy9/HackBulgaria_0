def string_to_char_list(string):
    result = []

    for ch in string:
        result += [ch]

    return result

def take(n, items):
    result = []

    for index in range(0, min(n, len(items))):
        result += items[index]

    return result

def startswith (search, string):
    n = len(search)
    search_char_list = string_to_char_list(string)

    return take(n,string) == search_char_list


def taken_name(nameh, namew):    
       
    return nameh in namew


print(taken_name("Petrov", "Petrova"))
print(taken_name("Ivanov", "Tsvetanova"))
print(taken_name("Petrov", "Ivanova-Petrova"))
