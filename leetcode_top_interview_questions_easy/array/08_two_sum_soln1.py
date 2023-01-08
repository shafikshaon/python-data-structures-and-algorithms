from typing import List


def main(nums: List[int], target: int) -> List[int]:
    print(f"Original array: {nums}.\n")

    nums.sort()
    left: int = 0
    right: int = len(nums) - 1
    while left < right:
        print(f"\nCurrent left index {left}, right index {right}.")
        print(
            f"Current sum {nums[left] + nums[right]} = {nums[left]} + {nums[right]} (curr_sum = nums[left] + nums[right])."
        )
        curr_sum: int = nums[left] + nums[right]
        if curr_sum == target:
            print(f"\nReturn the result: {[nums[left], nums[right]]}.")
            return [nums[left], nums[right]]
        if curr_sum < target:
            left += 1
        else:
            right -= 1
    return []


main(nums=[2, 7, 11, 15], target=9)

# Time complexity - O(nlog(n))
# Space complexity - O(1)
