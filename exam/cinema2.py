#approach 1
#Find empty seats (column, seat)- transform seat location to coordinates
#check availability of seats ON EACH ROW - eliminate from list of all seats occupied (diff)
#Compare availability and create priority - dict of [row]: available
#Fill row till full
#Move to the next


def list_to_dict(items):
    result = {}

    index = 0

    for index in range(0,len(items)):
        result[index] = items[index]
        index += 1

    return result

def order_of_seats(cinema):
    result = []
    cinema_dict = list_to_dict(cinema)
    #print(cinema_dict)
    
    available_seats = {}

    for row in cinema_dict:
        for seat in cinema_dict[row]:
            if cinema_dict[row][seat] == 0:
                 available_seats[row] += [(row,seat)]
# all + 1 to compensate for 0 indexes

    
    return result


cinema = [ [1, 1, 1],
           [1, 0, 0],
           [1, 0, 0],
           [1, 1, 0] ]

print(order_of_seats(cinema))
