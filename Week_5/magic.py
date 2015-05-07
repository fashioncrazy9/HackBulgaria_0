#NOT READY -> return to finish
def sum_list(items):
    result = 0 
    for item in items:
        result+= item
    return result

#print(sum_list([2,0,2]))

def magic_square(square):
    is_magic = False

    value = sum_list(square[0][0])
    index = 0

    for row in square:
        for item in row:
            pass
    return is_magic