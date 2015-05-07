def factoriel(n):
    result = 1

    while n > 0:
        result = result*n
        n -=1

    return result

print(factoriel(5))

def fact_digits(n):
    result = 0
    list_n = []

    if n == 0:
         result = 0

    while n % 10 >= 0 and n != 0:
        list_n += [(n % 10)]
        n = n // 10

    for digits in list_n:
        result += factoriel(digits)

    return result

print(fact_digits(999))