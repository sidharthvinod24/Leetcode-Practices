# Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

# A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).


# Example 1:

# Input: s = "abc", t = "ahbgdc"
# Output: true


# Example 2:

# Input: s = "axc", t = "ahbgdc"
# Output: false


s = "abc"
t = "ahbgdc"


def isSubsequence(s, t):

    p1, p2 = 0, 0

    while p1 < len(s) and p2 < len(t):
        if s[p1] == t[p2]:
            p1 += 1
        p2 += 1
    return p1 == len(s)
