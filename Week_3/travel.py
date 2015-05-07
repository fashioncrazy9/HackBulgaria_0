# travel.py (REVISE)


def travel_cost(n):

    cost = 0

    count = 1
    lines =[]

    while count <= n:
        trips = input("Enter number of trips for this line: ")
        trips = int(trips)

        lines += [trips]

        count +=  1


    for total in lines:
        if total >= 23:
            cost += 23
 
        else:
            cost += total
            

    if cost >= 50:
        return 50
        
    return cost

n_lines = input("Enter number of lines: ")
n_lines = int(n_lines)

print(travel_cost(n_lines))
