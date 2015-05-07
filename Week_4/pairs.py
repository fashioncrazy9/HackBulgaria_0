def count_zero_neighbors(numbers):
    count = 0
    index = 0

    for number in numbers:
        if index < len(numbers)- 1:
            neightbor = numbers[index+1]

            if number + neightbor == 0:
                count +=1
        index += 1

    return count


numbers = [1, 2, -2, 0, 0, 5, -5]
print(count_zero_neighbors(numbers))

def count_zero_pairs(numbers):
    count = 0
    n = len(numbers)

    for index_1 in range(0, n):
        for index_2 in range(index_1,n):
            if numbers[index_1] + numbers[index_2] == 0:
                count += 1

    return count

numbers = [0, 2, -2, 5, 10]
print(count_zero_pairs(numbers))


def is_prime(n):
    is_prime = True
    start = 2

    while start < n:
        if n % start == 0:
            is_prime = False
            break

        start += 1

    return is_prime

def prime_pair(numbers):
    result = False

    n = len(numbers)

    for i in range(0, n):
        for j in range(i,n):
            if is_prime(numbers[i] + numbers[j]) == True:
                result = True
                break
                
    return result