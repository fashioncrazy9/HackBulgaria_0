def on_budget(prices, budget): 
    result = {"books_on_budget": 0, "loan":0 }

    prices = sorted(prices)
    remaining = budget

    for price in prices:

        if remaining > 0 and remaining >= price :
            remaining -= price
            result["books_on_budget"] += 1

        else:
            result["loan"] += price 

    result["loan"] -= remaining

    return result



prices = [0, 10, 100, 5, 3, 8, 25]
budget = 35

print(on_budget(prices, budget))
