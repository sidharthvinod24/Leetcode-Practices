# Look at the possible scenarios in the case of an anagram the length of the two words must be the same so you have to check it
# Next create a hashmap for both the num and check if it is equal to each other
# Time Complexity
# o(n)

# Space Complexity
# o(n)

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        hashMap1 = {}
        hashMap2 = {}

        for i in s:
            hashMap1[i] = hashMap1.get(i, 0) + 1

        for i in t:
            hashMap2[i] = hashMap2.get(i, 0) + 1

        return hashMap1 == hashMap2
