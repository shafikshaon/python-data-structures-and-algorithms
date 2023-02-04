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
                print(
                    f"Taken stone {-stone_1} and {-stone_2}. "
                    f"Both stone are not same weight so new stone weight is {-(stone_1 - stone_2)}. "
                    f"Stone array: {stones}."
                )
                heapq.heappush(stones, stone_1 - stone_2)
            else:
                print(
                    f"Taken stone {-stone_1} and {-stone_2}. "
                    f"Both stone are same weight so destroyed both stone. Stone array: {stones}."
                )
        return -heapq.heappop(stones) if stones else 0


sol = Solution()
print(f"Last stone weight: {sol.lastStoneWeight(stones=[2, 7, 4, 1, 8, 1])}.")

"""
Output:
Taken stone 8 and 7. Both stone are not same weight so new stone weight is 1. Stone array: [-4, -2, -1, -1].
Taken stone 4 and 2. Both stone are not same weight so new stone weight is 2. Stone array: [-1, -1, -1].
Taken stone 2 and 1. Both stone are not same weight so new stone weight is 1. Stone array: [-1, -1].
Taken stone 1 and 1. Both stone are same weight so destroyed both stone. Stone array: [-1].
Last stone weight: 1.

Time Complexity: O(nlogn)
Space Complexity: O(n)
"""
