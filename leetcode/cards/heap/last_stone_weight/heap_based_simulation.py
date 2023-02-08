import heapq
from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i] *= -1

        heapq.heapify(stones)

        while len(stones) > 1:
            stone_1 = heapq.heappop(stones)
            stone_2 = heapq.heappop(stones)

            if stone_1 != stone_2:
                heapq.heappush(stones, stone_1 - stone_2)
        return -heapq.heappop(stones) if stones else 0


sol = Solution()
print(sol.lastStoneWeight(stones=[2, 7, 4, 1, 8, 1]))


"""
Output:
1

Time complexity: O(nlogn)
Space complexity: O(n)
"""
