# largest_3_digits.py

small = input("Give me a number: ")
med = input("Give me a second number: ")
big = input("Give me a third number: ")



op1 = small*100 + med*10+big
op2 = small*100 + big*10 + med
op3 = med*100 + big*10 + small
op4 = med*100 + small*10 + big
op5 = big*100 + small*10 + med
op6 = big*100 + med*10 + small


if op1 > op2 and op1 > op3 and op1 > op4 and op1 > op5 and op1 > op6:
    print(op1)

elif op1 > op2 and op1 > op3 and op1 > op4 and op1 > op5 and op1 > op6:
    print(op1)
    
elif op2 > op1 and op2 > op3 and op2 > op4 and op2 > op5 and op2 > op6:
    print(op2)



    if m > v:
        print("Largest: ",int(n+m+v))
        print("Smallest: ", int(v+m+n))

    elif v > m:
        print("Largest: ",int(n+v+m))
        print("Smallest: ", int(v+v+m))

elif m > n and m > v:

    if n > v:
        print("Largest: ",int(m+n+v))
        print("Smallest: ", int(v+n+m))

    elif v > n:
        print("Largest: ",int(m+v+n))
        print("Smallest: ", int(n+v+m))
        
elif v > n and v > m:

    if n > m:
        print("Largest: ",int(v+n+m))
        print("Smallest: ", int(m+n+v))

    elif m > n:
        print("Largest: ",int(v+m+n))
        print("Smallest: ", int(n+m+v))


elif n == m:

    if v > n:
        print("Largest: ",int(v+n+m))
        print("Smallest: ", int(m+n+v)

    elif v < n:
        print("Largest: ",int(n+m+v))
        print("Smallest: ", int(v+m+n))

