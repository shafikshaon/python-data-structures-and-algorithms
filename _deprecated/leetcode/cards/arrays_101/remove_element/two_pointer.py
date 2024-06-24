def main(nums, val):
    left = 0
    right = len(nums)

    while left < right:
        if nums[left] == val:
            nums[left] = nums[right - 1]
            right -= 1
        else:
            left += 1
    return right


def main2(nums, val):
    count = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[count] = nums[i]
            count += 1
    return count


print(main(nums=[3, 2, 2, 3], val=3))
print(main2(nums=[3, 2, 2, 3], val=3))

"""
Output:
2
2

Time Complexity: O(n)
Space Complexity: O(1) 
"""
