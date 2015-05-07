# int_functions.py

def reverse_int(n):
    digits = []

    while n!= 0:
        digit = n % 10

        digits += [digit]
        
        n = n // 10

    rev_n = []
    
    for digit in digits:
        rev_n += [digit]
        
    reversed_n = 0
    
    for digit in rev_n:
        reversed_n = reversed_n * 10 + digit
        
    return reversed_n

def sum_digits(n):

    digits = []
    total_sum = 0
    while n!= 0:
        digit = n % 10

        digits += [digit]
        
        n = n // 10
        
    for digit in digits:
        
        total_sum += digit
        
    return total_sum

def product_digits(n):

    digits = []
    total_product = 1
    
    while n!= 0:
        digit = n % 10

        digits += [digit]
        
        n = n // 10
        
    for digit in digits:
        
        total_product += total_product *
        
    return total_product

n = input("Enter a number: ")
n = int(n)

print("Reversed numbers is",reverse_int(n))
print("Sum of digits is ", sum_digits(n))
print("Product of digits is ", product_digits(n))
