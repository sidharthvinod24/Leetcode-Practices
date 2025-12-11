# Main idea will be to use the GCD algorithm


def GreatestCommonDivisor(str1, str2):
    a = len(str1)
    b = len(str2)

    maxLen = max(a, b)

    if str1+str2 != str2+str1:
        return ""

    while b:
        a, b = b, a % b

    return str1[:a]


str1 = "AAAAAB"
str2 = "AAA"

print(GreatestCommonDivisor(str1, str2))
