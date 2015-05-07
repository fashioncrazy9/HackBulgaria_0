# begin_functions.py

def square(x):
    return x**2

def factoriel(pesho):
    
    numbers = range(1,pesho+1)
    f = 1
    
    for number in numbers:
        f = f*number

    print(f)



def count_elements(items):

    counter = 0
    
    for item in items:
        counter +=1

    return counter
        
def member(x, xs):
    
    is_there = True

    for neshto in xs:
        if neshto == x:
            break
        else:
            is_there = False
            
    return is_there

def grades_that_pass(students, grades, limit):

    st_passed = []

    index = 0
    end = len(students) - 1

    while index <= end:
        if grades[index] >= limit:
            st_passed += [students[index]]

        index +=1

    return st_passed
