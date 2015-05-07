def status_count(students):
    result = { "finalized": [], 
                "not_finalized": []
    }

    for student in students:
        if student["status"] == "not_finalized":
            result["not_finalized"] += [student["name"]]

        else:
            result["finalized"] += [student["name"]]

    return result

students = [{
              "name": "RadoRado",
              "status": "not_finalized"
            }, {
              "name": "Ivo",
              "status": "finalized"
            }, {
              "name": "Genadi",
              "status": "finalized"}]

print(status_count(students))