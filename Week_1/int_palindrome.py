# int_palindrome.py

n = input("Give me number: ")
n = int(n)

non_reversed = n
rev_n = 0

while n!= 0:
    digit = n % 10
    rev_n = rev_n * 10 + digit
    n = n // 10

if non_reversed == rev_n:
    print(str(non_reversed) + " is palindrom")
else:
    print(str(non_reversed) + " is not palindom")
