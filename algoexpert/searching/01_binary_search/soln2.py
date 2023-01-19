# Question tag:  Easy

"""
Problem Statement:
- Given sorted integer array and target number
- Return the index or target number or -1 if not found

Sample Input:
array = [0, 1, 21, 33, 45, 45, 61, 71, 72, 73]
target = 33

Sample Output:
3
"""
from typing import List


def main(array: List, target: int) -> int:
    start = 0
    end = len(array) - 1

    while start <= end:
        mid = (start + end) // 2

        if array[mid] == target:
            print(f"{target} found in array at index {mid}.")
            return mid
        elif array[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    print(f"{target} not found in array.")
    return -1


if __name__ == "__main__":
    main(array=[1, 2, 3, 4, 5], target=2)
    main(array=[0, 1, 21, 33, 45, 45, 61, 71, 72, 73], target=33)
    main(array=[1, 5, 23, 111], target=35)

"""
Output:
2 found in array at index 1.
33 found in array at index 3.
35 not found in array.
"""

"""
Time complexity: O(n)
Space complexity: O(1
"""
