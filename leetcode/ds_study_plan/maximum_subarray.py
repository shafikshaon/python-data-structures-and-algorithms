from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_subarray = max_subarray = nums[0]

        for num in nums[1:]:
            print(f"New sub array: {current_subarray+num}.")
            current_subarray = max(num, current_subarray + num)
            max_subarray = max(max_subarray, current_subarray)
            print(f"Now max subarray: {max_subarray}.")
        print(f"\nMax subarray: {max_subarray}.")
        return max_subarray


sol = Solution()
sol.maxSubArray(nums=[-2, 1, -3, 4, -1, 2, 1, -5, 4])

"""
Output:
New sub array: -1.
Now max subarray: 1.
New sub array: -2.
Now max subarray: 1.
New sub array: 2.
Now max subarray: 4.
New sub array: 3.
Now max subarray: 4.
New sub array: 5.
Now max subarray: 5.
New sub array: 6.
Now max subarray: 6.
New sub array: 1.
Now max subarray: 6.
New sub array: 5.
Now max subarray: 6.

Max subarray: 6.
"""
# Time complexity: O(n)
# Space complexity: O(1)
