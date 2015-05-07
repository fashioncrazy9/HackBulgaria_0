#Gergana Karadzhova

def loss_or_profit(income, outcome):
    total_sum = 0

    for item in income:
        total_sum += item

    for item in outcome:
        total_sum -= item

    if total_sum > 0:
        total_sum = "+" + str(total_sum)
    elif total_sum < 0:
        total_sum = str(total_sum)
    else:
        total_sum = "=0"

        
    return str(total_sum)

print(loss_or_profit([1, 2, 3], [3]))
print(loss_or_profit([10], [20, 30]))
print(loss_or_profit([10], [10]))

