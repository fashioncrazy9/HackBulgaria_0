a = [2, 8, 4, 842, 4, - 2 , -4, 0, 2874]
a = sorted(a)

def bsearch(x,xs): 
    left = 0
    right = len(xs) - 1

    while left <= right:
        mid  = (left+right) // 2

        if xs[mid] == x:
            return True
        elif x < xs[mid]:
            right = mid - 1
        else:
            left = mid + 1

    return False 

print(bsearch(4,a))