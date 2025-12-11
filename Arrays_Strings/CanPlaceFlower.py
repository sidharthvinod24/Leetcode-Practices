# Main idea is to consider all the edge cases
# First we check if the we are at the start or end of the flowerbed
# Next we check if the left and right positions are empty or not


def canPlaceFlowers(flowerbed, n):
    for i in range(len(flowerbed)):
        if flowerbed[i] == 0:
            startIndex = (i == 0)
            endIndex = (i == len(flowerbed) - 1)

            rightEmptyCheck = flowerbed[i+1] == 0 if not endIndex else True
            leftEmptyCheck = flowerbed[i-1] == 0 if not startIndex else True

            if rightEmptyCheck and leftEmptyCheck:
                flowerbed[i] = 1
                n -= 1
    if n <= 0:
        return True
    return False
