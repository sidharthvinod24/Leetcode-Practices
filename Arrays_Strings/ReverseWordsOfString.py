def reverseWords(s):
    s = s.split(' ')
    emptyArr = []

    for i in s:
        if i != '':
            emptyArr.append(i)

    l = 0
    r = len(emptyArr) - 1

    while l < r:
        emptyArr[l], emptyArr[r] = emptyArr[r], emptyArr[l]
        l += 1
        r -= 1
    return " ".join(emptyArr)


print(reverseWords("the sky     is blue"))
