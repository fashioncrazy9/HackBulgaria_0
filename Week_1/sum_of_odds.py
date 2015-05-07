# sum_of_odds.py

n = input("Give me a number: ")
n = int(n)

counter = 0
sum = 0

while counter <= n:
    if counter % 2 == 1:
        sum = sum + counter
        counter = counter +1
        
    else:
        counter = counter + 1

print("Sum of odd numbers in this intervarl is: ", sum)
