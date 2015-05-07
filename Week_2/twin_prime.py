# twin_prime.py

n = input("Enter n: ")
n = int(n)

start = 2
is_n_prime = True

q = n + 2
q1 = n - 2

if n == 1:
    is_n_prime = False

while start < n :
    if n % start == 0:
        is_n_prime = False
        break
    start += 1


start = 2
is_q_prime = True

while start < q :
    if q % start == 0:
        is_q_prime = False
        break
    start += 1
            
start = 2
is_q1_prime = True

while start < q1 :
    if q1 % start == 0:
        is_q1_prime = False
        break
    start += 1

if is_n_prime and (not is_q_prime) and (not is_q1_prime):
    print(n, " is prime")
    print("But " + str(q) + " and " + str(q1) + " are not!")
elif is_n_prime:
    if is_q_prime:
        print(n,q)
    if is_q1_prime:
        print(n, q1)
else:
    print(n, " is not prime")
    
    
    
