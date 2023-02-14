class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x

        left, right = 2, x // 2

        while left <= right:
            pivot = left + (right - left) // 2
            num = pivot * pivot
            if num > x:
                right = pivot - 1
            elif num < x:
                left = pivot + 1
            else:
                return pivot
        return right


sol = Solution()
print(f"Index: {sol.mySqrt(x=8)}.")

"""
Output:
Index: 2.

Time complexity: O(logn)
Space complexity: O(1)
"""