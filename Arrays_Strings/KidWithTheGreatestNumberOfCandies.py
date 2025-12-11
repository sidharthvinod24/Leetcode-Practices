def kidWithCandies(candies, extraCandies):
    maxCandies = max(candies)
    returnArr = []
    for i in candies:
        if i + extraCandies >= maxCandies:
            returnArr.append(True)
        else:
            returnArr.append(False)
    return returnArr


candies = [12, 1, 12]
extraCandies = 10
print(kidWithCandies(candies, extraCandies))
