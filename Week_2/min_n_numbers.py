# min_n_numbers.py


n = input("Enter total number: ")
n = int(n)

count = 1
numbers = []

while count <= n:
    number = input("Enter number: ")
    number = int(number)

    numbers = numbers + [number]

    count += 1


min_value = numbers[0]

for number in numbers:
    if number < min_value:
        min_value = number

print(min_value)
