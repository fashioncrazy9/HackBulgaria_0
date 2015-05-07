def is_palindrome(n):
    result = True
    list_n = []

    if n == 0:
         result = False

    while n % 10 >= 0 and n != 0:
        list_n += [(n % 10)]
        n = n // 10

    return list_n == list_n[::-1]

def is_bin_palindrome(n):
    result = True
    list_n = []

    if n == 0:
         result = False

    int.n_bin= bin(n)[2:]
    while n_bin % 10 >= 0 and n_bin != 0:
        list_n += [(n % 10)]
        n = n // 10

    return list_n == list_n[::-1]



def is_hack(n):
    result = False

    if is_bin_palindrome(n):
        n_bin = bin(n)[2:]
        if n_bin.count("1") % 2 == 1:
            result = True

    return result

print("is n hack?", is_hack(7))


def next_hack(n):

    if is_hack(n):
        return n
    else:

        while is_hack(n) == False:
            n = n +1 

    return n

print(next_hack(0))
print(next_hack(10))
print(next_hack(8031))