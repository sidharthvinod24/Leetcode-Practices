#

s = "III"


def romanToInt(s):
    roman = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    res = 0
    lenS = len(s)

    for index, letter in enumerate(s):
        if index < lenS - 1 and roman[letter] < roman[s[index+1]]:
            res -= roman[letter]
        else:
            res += roman[letter]

    return res


print(romanToInt(s))
