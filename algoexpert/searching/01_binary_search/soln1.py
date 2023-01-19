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
    for i in range(len(array)):
        if array[i] == target:
            print(f"{target} found in array at index {i}.")
            return i
    print(f"{target} not found in array.")
    return -1


if __name__ == "__main__":
    main(array=[0, 1, 21, 33, 45, 45, 61, 71, 72, 73], target=33)
    main(array=[1, 5, 23, 111], target=35)

"""
Output:
33 found in array at index 3.
35 not found in array.
"""

"""
Time complexity: O(n)
Space complexity: O(1
"""
