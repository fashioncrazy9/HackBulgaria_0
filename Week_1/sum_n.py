# sum_n.py

def sum_n(n):
    n = input("Enter number: ")
    n = int(n)

    counter = 0
    sum = 0

    while counter <= n:
        sum = sum + counter
        counter = counter + 1

    print("Sum equls ", sum)
    return sum

n = input ("Enter number: ")
n = int(n)
print (sum_n(n))
