f_name = input("Enter first name: ")
s_name = input("Enter second name: ")
t_name = input("Enter third name: ")
dob = input("Enter birth year: ")
dob = int(dob)

person = {
    "first_name": f_name,
    "second_name": s_name,
    "third_name": t_name,
    "birth_year": dob,
    "current_age": 2015 - dob,  

    }
print(person)
