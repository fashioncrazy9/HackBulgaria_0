# bigger_last_digit.py

while True: 
    a = input("Enter a: ")
    b = input("Enter b: ")
    a = int(a)
    b = int(b)

    if a == b:
        print(a, " is equal to ",b)
    elif a % 10 > b % 10:
        print(a," has bigger last digit")
    elif b % 10 > a % 10 :
        print(b," has bigger last digit")
    elif a % 10 == b % 10:

        if a > b:
            print("same last digits but ", a, "is bigger")
        else:
            print ("same last digits but ", b, "is bigger")
            

    print("That was it")

    
           
