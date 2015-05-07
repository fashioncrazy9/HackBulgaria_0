a = {"first_name": "Gergana", 
    "age": 25,
    "hometown": "Plovdiv"}

def reverse_dict(a):
    result = {}
    
    for key in a:
        value = a[key]
        result[value] = key
    
    return result

