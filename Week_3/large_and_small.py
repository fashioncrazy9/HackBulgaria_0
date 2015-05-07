def to_digits(n):

    result  = []

    while n != 0:
        digit = n % 10
        
        result = [digit] + result
        
        n = n // 10

    return result

def build_num(digits):
    result = 0

    for digit in digits:
        result = result*10 + digit

    return result

n = input("Enter a number: ")
n = int(n)

digits = to_digits(n)
print("smallest number is: ")

smallest = build_num(digits) 
print(smallest)

print("biggest number is")
digits = reversed(digits)
biggest = build_num(digits)
print(biggest)
