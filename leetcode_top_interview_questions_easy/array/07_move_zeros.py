from typing import List


def main(nums: List[int]) -> None:
    print(f"Original array: {nums}\n")
    n: int = len(nums)
    i = 0
    for j in range(n):
        print(f"\nCurrent index: {j} and value is: {nums[j]}.")
        if nums[j] != 0:
            print(
                f"Swapping index {i} (value {nums[i]}) with index {j} (value {nums[j]})."
            )
            nums[i], nums[j] = nums[j], nums[i]
            print(f"Current array state is: {nums}.\n")
            i += 1
        else:
            print(f"Skipping index {j} because the values is 0.")
    print(f"Final array is: {nums}")


main(nums=[0, 0, 12, 1])

# Time complexity - O(n)
# Space complexity - O(1)
