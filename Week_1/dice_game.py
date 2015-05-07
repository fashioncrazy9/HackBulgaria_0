# dice_game.py

from random import randint

print ( "Hi")
n = input ("Enter integer number ")

name_1 = input ("Enter name first player: ")
name_2 = input ("Enter name second player: ")

dice_1 = randint(1, int(n))
print ( "First plyer got ", dice_1)
dice_2 = randint(1, int(n))
print ( "Second plyer got ", dice_2)


if dice_1>dice_2:
    print ("First player wins")
elif dice_1 == dice_2:
    print ("Lucky guys!Both get a beer")
else:
    print ( "Second player wins")

