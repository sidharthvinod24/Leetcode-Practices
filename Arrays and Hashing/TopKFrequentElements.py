# This might look simple but the solution is to get better than o(nlogn) which means no sorting
# This solution involves a min_heap
# The time complexity is O(m log k) because the heap size is limited to k.

from collections import Counter
import heapq
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        min_heap = []

        for num, freq in count.items():
            # The freq must be the first items
            heapq.heappush(min_heap, (freq, num))

            if len(min_heap) > k:  # Remove all small frequent element and only leave the top k
                heapq.heappop(min_heap)

        return [num for freq, num in min_heap]
