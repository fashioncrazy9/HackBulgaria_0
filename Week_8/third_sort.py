#Returns index of min element that is not used
def min_elem(items,used):
    unused_indexes = diff(range(0,len(items)), used)

    min_index = unused_indexes[0]

    for index in unused_indexes:
        if items[index] < items[min_index]:
            min_index = index

    return min_index

#Returns list of unused elements
def diff(a,b):
    unused = []

    for item in a:
        if item not in b:
            unused.append(item)

    return unused

#print(diff([1,2,3], [1,2]))

def third_sort(nums):
    sorted_nums = []
    used = []

    while len(sorted_nums) != len(nums):
        min_index = min_elem(nums, used)
        sorted_nums.append(nums[min_index])
        used.append(min_index)

    return sorted_nums

a = [5, 0, -3 ,4]
print(third_sort(a))