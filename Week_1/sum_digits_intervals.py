# sum_digits_intervals.py

n = input("Give me a number: ")
n = int(n)
m = input("Give me another number: ")
m = int(m)

if n == 0 and m == 0:
     print("Both", n," and ",m, "are 0. Their sum is 0")

start = 0
end = 0

if n < m: 
    start = n
    end = m
    
elif n > m:
    start = m
    end = n
 

while start <= end:
    
    start_digits_sum = 0        
    t = start
    
    while t != 0:
        digit = t % 10
        start_digits_sum += digit
        t = t // 10

    print("Sum of digits of ", start, "is ", start_digits_sum)
    start +=1

     

