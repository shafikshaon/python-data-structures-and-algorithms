def main(nums):
    one_count = 0
    current_max_count = 0
    for n in nums:
        if n == 1:
            one_count += 1
        else:
            if one_count >= current_max_count:
                current_max_count = max(current_max_count, one_count)
            one_count = 0
    return max(current_max_count, one_count)


print(main(nums=[1, 1, 0, 1, 1, 1]))

"""
Output:
3

Time Complexity: O(n)
Space Complexity: O(1)
"""
