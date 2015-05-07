from random import randint, shuffle

def generate_test(count):
    names = ["Ivo", "Maria", "Anetta", "Philip", "Rado", "Gergana"]
    result = []
    for name in names:
        result = result + [name] * randint(1, count)
        shuffle(result)
    
    return result

print(generate_test(5))

def get_people_count(activity):
    result = {}

    for item in activity:
        if item in result:
            result[item] += 1
        else:
            result[item] = 1


    return result

activity = ["Rado", "Ivo", "Maria", "Anneta", "Rado", "Rado", "Anneta", "Ivo", "Maria", "Rado"]
print(get_people_count(activity))