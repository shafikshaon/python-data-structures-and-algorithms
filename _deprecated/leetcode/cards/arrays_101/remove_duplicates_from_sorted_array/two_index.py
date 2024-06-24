def main(nums):
    n = len(nums)
    insert_index = 1

    for i in range(1, n):
        if nums[i - 1] != nums[i]:
            nums[insert_index] = nums[i]
            insert_index += 1
    return insert_index


print(main(nums=[1, 1, 2]))

"""
Output:
2

Time Complexity: O(n)
Space Complexity: O(1)
"""
