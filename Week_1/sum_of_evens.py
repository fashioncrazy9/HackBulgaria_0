# sum_of_evens.py

n = input("Give me a number: ")
n = int(n)

counter = 0
sum = 0

while counter <= n:
    if counter % 2 == 0:
        sum = sum + counter
        counter = counter +1
        
    else:
        counter = counter + 1

print("Sum of even numbers in this intervarl is: ", sum)
