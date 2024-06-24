import heapq
from collections import Counter
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if k == len(nums):
            return nums

        count = Counter(nums)
        return heapq.nlargest(k, count.keys(), key=count.get)


sol = Solution()
print(sol.topKFrequent(nums=[1, 1, 1, 2, 2, 3], k=2))

"""
Output:
[1, 2]

Time complexity: O(nlogk)
Space complexity: O(n+k)
"""
