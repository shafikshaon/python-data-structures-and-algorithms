from typing import List


def two_number_sum(array: List, target_sum: int) -> List:
    for i in range(len(array)):
        first_sum = array[i]
        for j in range(i + 1, len(array)):
            second_sum = array[j]
            if first_sum + second_sum == target_sum:
                return [array[i], array[j]]
    return []


def main():
    array = [3, 5, -4, 8, 11, 1, -1, 6]
    target_sum = 10
    print(two_number_sum(array, target_sum))


main()

# Time complexity - O(n^2)
# Space complexity - O(1)
