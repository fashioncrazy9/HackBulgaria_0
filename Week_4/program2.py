f_name = input("Enter first name: ")
m_name = input("Enter middle name: ")
fam_name = input("Enter family name: ")
dob = input ("Enter date of birth: ")
dob = int(dob)


person = { "first_name": f_name, "second_name": m_name, "family_name" : fam_name, 
        "birth_year": dob, "current_age": 2015 - dob }

print(person)