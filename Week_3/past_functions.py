def divisor(n):
    
    divisors = [1]

    start = 2

    while start < n:
        if n % start == 0:
            divisors = divisors +[start]
        start += 1

    return divisors

def sum_ints(n):
    total_sum = 0

    divisor_values = divisor(n)
    
    for value in divisor_values:
        total_sum += value
    
    return total_sum

def is_perfect_number(n):
    
    total_sum = sum_ints(n)
    
    is_perfect = False

    if total_sum == n:
        is_perfect = True
    
    return is_perfect

def to_digits(n):

    result  = []
    digit = 0

    while n!= 0:
        digit = n % 10
        result = [digit] + result
        n = n // 10

    return result

print(to_digits(123))

def is_prime (n):
    result = True

    start = 2
    
    if n == 1:
        result = True

    while start < n:
        if n % start == 0:
            result = False
        start += 1

    return result

print(is_prime(7))