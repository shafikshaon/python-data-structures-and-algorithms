from typing import List


def two_number_sum(array: List, target_sum: int) -> List:
    array.sort()
    left = 0
    right = len(array) - 1
    while left < right:
        curr_sum = array[left] + array[right]
        if curr_sum == target_sum:
            return [array[left], array[right]]
        if curr_sum < target_sum:
            left += 1
        else:
            right -= 1
    return []


def main():
    array = [3, 5, -4, 8, 11, 1, -1, 6]
    target_sum = 10
    print(two_number_sum(array, target_sum))


main()

# Time complexity - O(log(n))
# Space complexity - O(1)
