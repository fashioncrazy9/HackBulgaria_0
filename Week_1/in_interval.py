# in_interval.py

a = input("Enter lower bound: ")
b = input("Enter upper bound: ")
x = input("Enter random number: ")

a = int(a)
b = int(b)
x = int(x)

if x == a:
    print("The number is equal to the lower bound of the interval")
elif x == b:
    print ("The number is equal to the upper bound of the interval")
elif (x > a) and (x < b):
    print("The number is in the interval")
else:
    print("The number is outside the interval")
    
