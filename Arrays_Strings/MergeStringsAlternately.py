# The main idea is simple, just loop through the charcaters of both strings and add them to the result one by one
# And finally if there is any extra leeters it will be added to the behind of the result

def mergeAlternateStrings(word1, word2):
    minWordLen = min(len(word1), len(word2))
    mergedStr = ""

    for i in range(minWordLen):
        mergedStr += word1[i]
        mergedStr += word2[i]

    if len(word1) > len(word2):
        mergedStr += word1[minWordLen:]
    else:
        mergedStr += word2[minWordLen:]

    return mergedStr
