# sum_digits.py

while True:
    n = input("Give me a number: ")
    n = int(n)

    sum = 0


    if n == 0:
         print("Sum is 0")

    while n % 10 >= 0 and n != 0:
        sum = sum + (n % 10)
        n = n // 10
    print("Sum is", sum)
        

