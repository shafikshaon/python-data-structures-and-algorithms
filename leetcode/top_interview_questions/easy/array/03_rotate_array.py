from typing import List


def reverse_array(nums: List, start: int, end: int) -> None:
    while start < end:
        nums[start], nums[end] = nums[end], nums[start]
        start, end = start + 1, end - 1


def main(nums: List[int], k: int) -> None:
    print(f"Original array: {nums} and k = {k}\n")
    array_size = len(nums)
    k %= len(nums)

    reverse_array(nums=nums, start=0, end=array_size - 1)
    print(f"After reverse whole array: {nums}\n")
    print(f"Reversing first {k} (k) elements...")
    reverse_array(nums=nums, start=0, end=k - 1)
    print(f"After reverse first {k} (k) elements in array: {nums}\n")
    print(f"Reversing last {array_size - k} (array_size - k) elements...")
    reverse_array(nums=nums, start=k, end=array_size - 1)
    print(
        f"After reversing last {array_size - k} (array_size - k) elements in array: {nums}"
    )
    print(f"\nThe final array is: {nums}")


main(nums=[1, 2, 3, 4, 5, 6, 7], k=3)

# Output

# Time complexity - O(n)
# Space complexity - O(1)
