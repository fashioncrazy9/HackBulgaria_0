# n_dice_more.py

from random import randint

print ( "Hi")
number = input ("Enter integer number ")

dice = randint(1,int(number))

print("I have thrown the dice of destiny. Here is the result:")
print(dice)
result1 = dice

dice = randint(1,int(number))
print("I have thrown the dice of destiny a second time. Here is the result:")
print(dice)
result2 = dice

dice = randint(1,int(number))
print("I have thrown the dice of destiny a third time. Here is the result:")
print(dice)
result3 = dice

sum = result1 + result2 + result3
print ("Sum of your destiny numbers is", sum)

