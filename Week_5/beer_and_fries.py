def max_score(beers, fries):
    beers = sorted(beers)
    fries = sorted(fries)

    result = 0

    n = len(beers)

    for i in range(0,n):
        result += beers[i]*fries[i]

    return result
print(max_score([1000, 1010, 1020, 1030, 1040], [834, 500, -1, 0, 60]))