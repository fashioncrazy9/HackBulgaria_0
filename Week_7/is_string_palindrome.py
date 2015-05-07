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


def trim_left(string):
    while startswith(" ", string):
    string = str_drop(1, string)
    return string

def trim_right(string):
    return str_reverse(
                trim_left(
                    str_reverse(string)))

def trim(string):
    result = trim_left(string)
    result = trim_right(result)
    return result

def is_string_palindrom(string):
    result = True

    string1 = string_to_char_list(string)
    


    return result