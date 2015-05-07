def str_reverse(string):
    result = ""

    last_index = len(string) - 1

    while last_index >= 0:
        result += string[last_index]
        last_index -= 1

    return result

print(str_reverse("Python"))

def join(delimiter, items):
    result = ""

    for item in items:
        item = str(items)

    for index in range(0, len(items)):
        result += items[index] + delimiter

    return result

print(join(" ", ["Radoslav", "Yordanov", "Georgiev"]))

def string_to_char_list(string):
    result = []
    for ch in string:
        result += [ch]
   
    return result

def char_list_to_string(char_list):
    result = ""
    for ch in char_list:
        result += ch
    
    return result

def take(n, items):
    if n > len(items):
        n = len(items)

    index = 0
    new_list = []

    while index < n:
        new_list = new_list + [items[index]]
        index += 1

    return new_list

def startswith(search, string):
    n = len(search)
    
    search_char_list = string_to_char_list(search)

    return take(n,string) == search_char_list

print(startswith("Py", "Python"))

def endswith(search,string):
    string = str_reverse(string)
    search = str_reverse(search)
    
    return startswith(search, string)

print(endswith(".py", "hello.py"))

def str_drop(n, string):
    result = ""
    for index in range(n, len(string)):
        result += string[index]
    return result

def trim_left(string):

    while startswith(" ", string):
        string = str_drop(1, string)

    return string

def trim_right(string):
    return str_reverse( trim_left(str_reverse(string)))

def trim(string):
    result = trim_right(string)
    result = trim_left(string)

    return result

print(trim("   ddd   "))