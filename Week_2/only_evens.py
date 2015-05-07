# only_evens.py

n = input("Enter total number: ")
n = int(n)

count = 1
numbers = []

while count <= n:
    number = input("Enter number: ")
    number = int(number)

    numbers = numbers + [number]

    count += 1

even_numbers_count = 0
even_numbers = []

for number in numbers:
    if number % 2 == 0:
        even_numbers += [number]
        even_numbers_count += 1 
        print(number)
        
print("Total number of even numbers is ", even_numbers_count)
print("Here are all even numbers")

for num in even_numbers:
    print(num)
