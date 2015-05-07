def calculate_coins(sum):
    #result = {"1": 0,"2": 0,"100": 0 ,"5": 0,"10": 0,"50":0,"20":0}
    result ={}
    coins = [ 100, 50, 20, 10, 5, 2, 1]
    sum = round(sum * 100)

    for coin in coins:
        coin_count = sum //coin
        result[coin] = coin_count
        sum -= coin * coin_count

    return result

print(calculate_coins(8.94) == { 1: 0, 2: 2, 100: 8, 5: 0, 10: 0, 50: 1, 20: 2 })
print(calculate_coins(0.53) == { 1: 1, 2: 1, 100: 0, 5: 0, 10: 0, 50: 1, 20: 0 })