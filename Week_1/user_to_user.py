# user_to_user.py

while True:
    a = input("Enter first number: ")
    b = input("Enter second number: ")

    a = int(a)
    b = int(b)

    if a < b :

        start = a

        while start <= b:
            print(start)
            start = start+1
            
    elif a > b:
        
        start = b

        while start <= a:
            print(start)
            start = start+1
    else:
        print(a)
