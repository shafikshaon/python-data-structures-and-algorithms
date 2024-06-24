class Solution:
    def mySqrt(self, x: int):
        if x < 2:
            return x
        left, right = 2, x // 2
        while left <= right:
            pivot = left + (right - left) // 2
            num = pivot * pivot
            print(f"num: {num}, pivot: {pivot}.")
            if num > x:
                right = pivot - 1
            elif num < x:
                left = pivot + 1
            else:
                return pivot
        return right


solution = Solution()

input1 = 4
expectedOutput1 = 2
result1 = solution.mySqrt(input1)
print(result1)
