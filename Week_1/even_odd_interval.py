# even_odd_interval.py

while True:
    a = input("Enter first number: ")
    b = input("Enter second number: ")

    a = int(a)
    b = int(b)

    if a < b :

        start = a

        while start <= b:

            if start%2 == 0:
                print(start, "- even")
            else:
                print (start, "- odd")

            start = start+1
            
    elif a > b:
        
        start = b

        while start <= a:
            if start%2 == 0:
                print(start, "- even")
            else:
                print (start, "- odd")

            start = start+1

    elif a == b:
        start = a
        if start%2 == 0:
            print(start, "- even")
        else:
            print (start, "- odd")
