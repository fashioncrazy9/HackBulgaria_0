# avg.py

n = input("Enter total number: ")
n = int(n)

count = 1
numbers = []

while count <= n:
    number = input("Enter number: ")
    number = int(number)

    numbers = numbers + [number]

    count += 1

total_sum = 0

for number in numbers:
    total_sum += number
    
        
print(total_sum/len(numbers))
