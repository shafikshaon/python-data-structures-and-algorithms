from typing import List


def main(nums: List[int]) -> int:
    print(f"Original array: {nums}")
    size: int = len(nums)
    insert_index: int = 1

    for i in range(1, size):
        if nums[i - 1] != nums[i]:
            print(f"In index: {i}. Unique value: {nums[i]} found")
            nums[insert_index] = nums[i]
            print(
                f"Value ({nums[i]}) swap with value ({nums[insert_index]}) from index {i} to index {insert_index}"
            )
            print(f"Current array elements: {nums}")
            insert_index += 1

    print(f"Final array: {nums}")
    print(f"Unique elements length: {insert_index}")
    return insert_index


main([1, 1, 2, 3])


# Time complexity - O(n)
# Space complexity - O(1)
