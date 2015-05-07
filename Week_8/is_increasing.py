def is_increasing(seq):
    result = True

    index = 0 

    while index < len(seq)-1:
        if seq[index] < seq[index+1]:
            index +=1
        else:
            result = False
            break

    return result

print(is_increasing([1,2,3,4,5])) 
print(is_increasing([1]))
print (is_increasing([5,6,-10]))
print(is_increasing([1,1,1,1]))