n = input("Enter a number: ")
n = int(n)

start = 1
result = 1

while start <= n:
    result = result * start
    start += 1

print ("Factorial of " + str(n) + " is " + str(result))
