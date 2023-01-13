def main(nums):
    sum_l = 0
    sum_r = sum(nums)
    for n in range(len(nums)):
        print(
            f"Current index {n}, value {nums[n]}, sum left {sum_l}, sum right {sum_r - nums[n]}."
        )
        sum_r -= nums[n]
        if sum_l == sum_r:
            return n
        sum_l += nums[n]

    return -1


print(main(nums=[1, 7, 3, 6, 5, 6]))

# Time complexity: O(n)
# Space complexity: O(1)

# Output
"""
Current index 0, value 1, sum left 0, sum right 27.
Current index 1, value 7, sum left 1, sum right 20.
Current index 2, value 3, sum left 8, sum right 17.
Current index 3, value 6, sum left 11, sum right 11.
3
"""
