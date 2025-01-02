# For this simply create a hashmap and rmb that if the target - value is in the array you can solve this question
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numSet = {}
        for i, n in enumerate(nums):
            if target - n in numSet:
                return (numSet[target-n], i)
            numSet[n] = i
