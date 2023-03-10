from typing import List


def display_array(nums, left, mid, right):
    result = ""
    for i in range(len(nums)):
        if i == left:
            result += f"   ║ left ({i})  " + str(nums[i])
        if i == mid:
            result += f"   ║ mid ({i})   " + str(nums[i])
        if i == right:
            result += f"   ║ right ({i}) " + str(nums[i])
        if i in [left, mid, right]:
            continue
        else:
            result += f"   ║ ({i})       " + str(nums[i])
    result += " ║"
    return result


def main(nums: List, target: int) -> int:
    left, right, mid = 0, len(nums) - 1, 0

    while left <= right:
        mid = (left + right) // 2
        print(
            "   ____________________________________________________________________________________________________________________________________________"
        )
        print("" + display_array(nums, left, mid, right))
        print(
            "   --------------------------------------------------------------------------------------------------------------------------------------------"
        )

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


print("Found at index: " + str(main(nums=[-1, 0, 3, 5, 9, 12], target=9)))
print(
    "-----------------------------------------------------------------------------------------------------"
)
print("Found at index: " + str(main(nums=[-1, 0, 3, 5, 9, 12], target=2)))
print(
    "-----------------------------------------------------------------------------------------------------"
)
print("Found at index: " + str(main(nums=[-1, 0, 3, 5, 9, 12], target=0)))

# Time complexity: O(log(n))
# Space complexity: O(1)

# Output
"""
   ____________________________________________________________________________________________________________________________________________
   ║ left (0)  -1   ║ (1)       0   ║ mid (2)   3   ║ (3)       5   ║ (4)       9   ║ right (5) 12 ║
   --------------------------------------------------------------------------------------------------------------------------------------------
   ____________________________________________________________________________________________________________________________________________
   ║ (0)       -1   ║ (1)       0   ║ (2)       3   ║ left (3)  5   ║ mid (4)   9   ║ right (5) 12 ║
   --------------------------------------------------------------------------------------------------------------------------------------------
Found at index: 4
-----------------------------------------------------------------------------------------------------
   ____________________________________________________________________________________________________________________________________________
   ║ left (0)  -1   ║ (1)       0   ║ mid (2)   3   ║ (3)       5   ║ (4)       9   ║ right (5) 12 ║
   --------------------------------------------------------------------------------------------------------------------------------------------
   ____________________________________________________________________________________________________________________________________________
   ║ left (0)  -1   ║ mid (0)   -1   ║ right (1) 0   ║ (2)       3   ║ (3)       5   ║ (4)       9   ║ (5)       12 ║
   --------------------------------------------------------------------------------------------------------------------------------------------
   ____________________________________________________________________________________________________________________________________________
   ║ (0)       -1   ║ left (1)  0   ║ mid (1)   0   ║ right (1) 0   ║ (2)       3   ║ (3)       5   ║ (4)       9   ║ (5)       12 ║
   --------------------------------------------------------------------------------------------------------------------------------------------
Found at index: -1
-----------------------------------------------------------------------------------------------------
   ____________________________________________________________________________________________________________________________________________
   ║ left (0)  -1   ║ (1)       0   ║ mid (2)   3   ║ (3)       5   ║ (4)       9   ║ right (5) 12 ║
   --------------------------------------------------------------------------------------------------------------------------------------------
   ____________________________________________________________________________________________________________________________________________
   ║ left (0)  -1   ║ mid (0)   -1   ║ right (1) 0   ║ (2)       3   ║ (3)       5   ║ (4)       9   ║ (5)       12 ║
   --------------------------------------------------------------------------------------------------------------------------------------------
   ____________________________________________________________________________________________________________________________________________
   ║ (0)       -1   ║ left (1)  0   ║ mid (1)   0   ║ right (1) 0   ║ (2)       3   ║ (3)       5   ║ (4)       9   ║ (5)       12 ║
   --------------------------------------------------------------------------------------------------------------------------------------------
Found at index: 1

"""
