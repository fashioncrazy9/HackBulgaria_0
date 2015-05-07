# print_digits.py

while True: 
    a = input("Enter a: ")
    a = int(a)

    if a == 0:
         print("0")

    while a % 10 >= 0 and a != 0:
        print(a % 10)
        a = a // 10
            
