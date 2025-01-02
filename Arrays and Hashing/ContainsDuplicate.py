# Time Complexity: O(n) (for converting nums to a set)
# Space Complexity: O(n) (for storing the unique elements in the set

from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len((nums)) > len(set(nums))
