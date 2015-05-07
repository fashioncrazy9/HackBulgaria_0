# fib_numbers.py

def fib(n):
    list_fib = [1, 1]


    if n == 1:
        return [1]

    elif n == 2:
        return [1,1]

    else:
        counter = 2
        
        while counter < n:
            list_fib += [0]
            list_fib[counter] = list_fib[counter - 1] + list_fib[counter-2]

            counter += 1 
           
    return list_fib

def count_digits(n):
    count = 0

    while n % 10 != 0:
        count += 1
        



    return count

def fib_numbers(n):
    new_numb = 0
    
    for item in n:
        
        new_numb = new_numb*10 + item
    
    return new_numb 
    

n = input("Enter n: ")
n = int(n)

print(fib_numbers(fib(n)))
