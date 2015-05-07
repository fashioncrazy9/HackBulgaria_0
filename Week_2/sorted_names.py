# sorted_names.py

n = input("Enter total number: ")
n = int(n)

count = 1
names = []

while count <= n:
    name = input("Enter a name: ")

    names = names + [name]

    count += 1

names = sorted(names)

print(names)
        
