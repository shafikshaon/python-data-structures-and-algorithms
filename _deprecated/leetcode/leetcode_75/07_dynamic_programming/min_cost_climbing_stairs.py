# Bottom-Up Dynamic Programming
from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        minimum_cost = [0] * (len(cost) + 1)
        print(f"Minimum cost: {minimum_cost}.\n")
        for i in range(2, len(cost) + 1):
            take_one_step = minimum_cost[i - 1] + cost[i - 1]
            take_two_steps = minimum_cost[i - 2] + cost[i - 2]
            print(
                f"One step cost: {take_one_step}, Two step cost: {take_two_steps}, and min cost is: {min(take_one_step, take_two_steps)}."
            )
            minimum_cost[i] = min(take_one_step, take_two_steps)
            print(f"Now minimum cost: {minimum_cost}.\n")
        print(f"\nThe minimum cost is: {minimum_cost[-1]}.")
        return minimum_cost[-1]


sol = Solution()
print(f"Input cost: {[10, 15, 20]}\n")
sol.minCostClimbingStairs(cost=[10, 15, 20])

"""
Output:
Input cost: [10, 15, 20]

Minimum cost: [0, 0, 0, 0].

One step cost: 15, Two step cost: 10, and min cost is: 10.
Now minimum cost: [0, 0, 10, 0].

One step cost: 30, Two step cost: 15, and min cost is: 15.
Now minimum cost: [0, 0, 10, 15].


The minimum cost is: 15.

Time complexity: O(n)
Space complexity: O(n)
"""
