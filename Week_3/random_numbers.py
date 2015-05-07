# random_numbers.py


def generate_random_list(n, start, end):
    list = []

    counter = 1

    while counter <= n:
        list += [randint(start, end)]
        counter += 1

    return list


from random import randint

n = input("Enter n: ")
n = int(n)

start = input("Enter start: ")
start = int(start)

end = input("Enter end: ")
end = int(end)

print(generate_random_list(n,start,end))
