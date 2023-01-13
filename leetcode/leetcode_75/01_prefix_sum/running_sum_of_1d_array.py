def main(nums):
    for n in range(1, len(nums)):
        print(f"Current index {n}, sum {nums[n]} and array is: {nums}.")
        nums[n] += nums[n - 1]

    return nums


print(main(nums=[1, 2, 3, 4]))

# Time complexity: O(n)
# Space complexity: O(1)

# Output
"""
Current index 1, sum 2 and array is: [1, 2, 3, 4].
Current index 2, sum 3 and array is: [1, 3, 3, 4].
Current index 3, sum 4 and array is: [1, 3, 6, 4].
[1, 3, 6, 10]
"""
