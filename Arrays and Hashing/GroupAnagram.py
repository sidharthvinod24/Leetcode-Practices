# This is a bit of a hard question for me essentially we want to create a hashmap containing how many times each character appears

from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # We create a default dict as when we first initialize a normal dict there is no value inside so this is done to prevent it from happening
        anagram_map = defaultdict(list)
        res = []

        for i in strs:
            # We need a tuple as it is a immutable data type and we need immutable data types when it comes to being keys in a dictionary
            sorted_i = tuple(sorted(i))
            anagram_map[sorted_i].append(i)
        for i in anagram_map.values():
            res.append(i)
        return res


# This solution has time complexity of o(m * klogk) as we need to sort each element


# Another solution using the ord function


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            anagram_map[tuple(count)].append(s)
        return list(anagram_map.values())
