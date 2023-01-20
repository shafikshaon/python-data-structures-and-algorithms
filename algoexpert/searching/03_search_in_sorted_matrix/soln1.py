# Question tag:  Medium

"""
Problem Statement:
- Given 2D array of distinct integers and a target integer
- Each row in the matrix is sorted and column also sorted. The row, column doesn't have the same height and width.
- Return the row, colum indices of target integer otherwise [-1, -1]

Sample Input:
matrix = [
  [1, 4, 7, 12, 15, 1000],
  [2, 5, 19, 31, 32, 1001],
  [3, 8, 24, 33, 35, 1002],
  [40, 41, 42, 44, 45, 1003],
  [99, 100, 103, 106, 128, 1004],
]
target = 44

Sample Output:
[3, 3]
"""
from typing import List


def main(matrix: List, target: int) -> List:
    print(f"Initial matrix: {matrix} and target is: {target}.")
    row = 0
    column = len(matrix[0]) - 1
    while row < len(matrix) and column >= 0:
        picked_value = matrix[row][column]
        if picked_value == target:
            print(f"Target {target} found at index {[row, column]}.\n")
            return [row, column]
        elif picked_value > target:
            column -= 1
        else:
            row += 1
    print(f"Target {target} not found.\n")
    return [-1, -1]


if __name__ == "__main__":
    main(
        matrix=[
            [1, 4, 7, 12, 15, 1000],
            [2, 5, 19, 31, 32, 1001],
            [3, 8, 24, 33, 35, 1002],
            [40, 41, 42, 44, 45, 1003],
            [99, 100, 103, 106, 128, 1004],
        ],
        target=44,
    )
    main(
        matrix=[
            [1, 4, 7, 12, 15, 1000],
            [2, 5, 19, 31, 32, 1001],
            [3, 8, 24, 33, 35, 1002],
            [40, 41, 42, 44, 45, 1003],
            [99, 100, 103, 106, 128, 1004],
        ],
        target=106,
    )
    main(
        matrix=[
            [1, 4, 7, 12, 15, 1000],
            [2, 5, 19, 31, 32, 1001],
            [3, 8, 24, 33, 35, 1002],
            [40, 41, 42, 44, 45, 1003],
            [99, 100, 103, 106, 128, 1004],
        ],
        target=40,
    )

"""
Output:
Initial matrix: [[1, 4, 7, 12, 15, 1000], [2, 5, 19, 31, 32, 1001], [3, 8, 24, 33, 35, 1002], [40, 41, 42, 44, 45, 1003], [99, 100, 103, 106, 128, 1004]] and target is: 44.
Target 44 found at index [3, 3].

Initial matrix: [[1, 4, 7, 12, 15, 1000], [2, 5, 19, 31, 32, 1001], [3, 8, 24, 33, 35, 1002], [40, 41, 42, 44, 45, 1003], [99, 100, 103, 106, 128, 1004]] and target is: 106.
Target 106 found at index [4, 3].

Initial matrix: [[1, 4, 7, 12, 15, 1000], [2, 5, 19, 31, 32, 1001], [3, 8, 24, 33, 35, 1002], [40, 41, 42, 44, 45, 1003], [99, 100, 103, 106, 128, 1004]] and target is: 40.
Target 40 found at index [3, 0].

"""

"""
Time complexity: O(n + m)
Space complexity: O(1)
"""
