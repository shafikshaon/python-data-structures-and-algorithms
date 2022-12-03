from typing import List


def two_number_sum(array: List, target_sum: int) -> List:
    nums = {}
    for i in range(len(array)):
        first_sum = array[i]
        possible_sum = target_sum - first_sum
        if possible_sum in nums:
            return [possible_sum, first_sum]
        else:
            nums[first_sum] = True
    return []


def main():
    array = [3, 5, -4, 8, 11, 1, -1, 6]
    target_sum = 10
    print(two_number_sum(array, target_sum))


main()

# Time complexity - O(n)
# Space complexity - O(n)
