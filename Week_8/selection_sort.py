def swap(i,j,nums):
    temp = nums[i]
    nums[i] = nums[j]
    nums[j] = temp


def min_elem(start_index, nums):
    min_index = start_index

    index = start_index
    while index <= len(nums) -1:
        if nums[index] < nums[min_index]:
            min_index = index
        index +=1           

    return min_index


def selection_sort(nums):

    index = 0

    while index <= len(nums)-1:
        min_index = min_elem(index,nums)
        swap(index, min_index, nums)
        index += 1

a =[0,7,-1,4]
selection_sort(a)
print(a)



