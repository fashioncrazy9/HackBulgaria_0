
# NEED TO REVISE

n = input("Enter n: ")
n = int(n)



start = 6
end = n - 1
count = 0

while True:

divisors = []
total_sum = 0

    while start <= end:
        if n % start == 0:
            divisors = divisors + [start]
            total_sum = total_sum + start
        
    start += 1

if total_sum == n:
    print("Number is perfect")
else:
    print("Number is not perfect")
