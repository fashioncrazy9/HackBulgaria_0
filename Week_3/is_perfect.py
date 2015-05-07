# is_perfect.py

n = input("Enter n: ")
n = int(n)

divisors = []
total_sum = 0

start = 1
end = n - 1

while start <= end:
    if n % start == 0:
        divisors = divisors + [start]
        total_sum = total_sum + start
        
    start += 1

print(n, " is divided by ", divisors)
print("Sum of its divisors is: ", total_sum)

if total_sum == n:
    print("Number is perfect")
else:
    print("Number is not perfect")
    
