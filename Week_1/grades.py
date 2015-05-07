# grades.py

while True:
    
    g = input("Enter number of points: ")

    g = int(g)

    if g == 100:
        print ("You rock!")
    elif g >= 0 and g <= 50:
        print("Poor 2")
    elif g >= 51 and g <= 60:
        print("Average 3")
    elif g >= 61 and g <= 70:
        print("Good 4")
    elif g >= 71 and g <= 80:
        print("Very good 5")
    elif g >= 81:
        print("Excellent 6")



