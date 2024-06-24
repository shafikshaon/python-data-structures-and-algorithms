import heapq
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return heapq.nlargest(k, nums)[-1]


sol = Solution()
print(sol.findKthLargest(nums=[3, 2, 1, 5, 6, 4], k=2))

"""
Output:
5

Time complexity: O(nlogk)
Space complexity: O(k) to store the heap elements
"""
