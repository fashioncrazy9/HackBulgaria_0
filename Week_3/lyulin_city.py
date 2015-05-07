# lyulin_city.py

n = input("Enter number of buldings: ")
n = int(n)

count = 1
blocks =[]

while count <= n:
    block = input("Enter number of stories: ")
    block = int(block)

    blocks += [block]

    count +=  1

count_blocks = 1

start_index = 0
end_index = len(blocks)

max_high = blocks[0]

while start_index < end_index:
    
    if max_high < blocks[start_index]:
        count_blocks += 1

        max_high = blocks[start_index]      
    start_index += 1

    
print("Ivan will see", count_blocks)
