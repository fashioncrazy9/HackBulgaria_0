# divisors.py

n = input("Enter n: ")
n = int(n)

divisors = [1]

start = 2

while start < n:
    if n % start == 0:
        divisors = divisors +[start]
    start += 1
print(n, " is divided by ", divisors)

