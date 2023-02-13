from typing import List


class Solution:
    def print_row(self, row):
        return (
                " "
                + "___ " * len(row)
                + " \n"
                + "|"
                + "|".join(f" {x} " for x in row)
                + "|"
        )

    def display_board(self, grid: List[List[str]]):
        return (
                "\n".join(self.print_row(row) for row in grid)
                + "\n "
                + "--- " * len(grid[-1])
        )

    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        is_lands = 0
        visited = set()
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                print(
                    f"Current row: {row}, current col: {col}, value is: {grid[row][col]}."
                )
                is_lands += self.dfs(grid, row, col, visited)
        print(f"Number of island: {is_lands}.")
        return is_lands

    def dfs(self, grid, row, col, visited):
        if (
                row < 0
                or row >= len(grid)
                or col < 0
                or col >= len(grid[row])
                or grid[row][col] == "0"
                or (row, col) in visited
        ):
            return 0

        visited.add((row, col))

        self.dfs(grid, row + 1, col, visited)
        self.dfs(grid, row - 1, col, visited)
        self.dfs(grid, row, col + 1, visited)
        self.dfs(grid, row, col - 1, visited)
        return 1


sol = Solution()
print(f"Input matrix:")
print(
    sol.display_board(
        grid=[
            ["1", "1", "0", "0", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "1", "0", "0"],
            ["0", "0", "0", "1", "1"],
        ]
    )
)
sol.numIslands(
    grid=[
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"],
    ]
)

"""
Output:
Input matrix:
 ___ ___ ___ ___ ___  
| 1 | 1 | 0 | 0 | 0 |
 ___ ___ ___ ___ ___  
| 1 | 1 | 0 | 0 | 0 |
 ___ ___ ___ ___ ___  
| 0 | 0 | 1 | 0 | 0 |
 ___ ___ ___ ___ ___  
| 0 | 0 | 0 | 1 | 1 |
 --- --- --- --- --- 
Current row: 0, current col: 0, value is: 1.
Current row: 0, current col: 1, value is: 1.
Current row: 0, current col: 2, value is: 0.
Current row: 0, current col: 3, value is: 0.
Current row: 0, current col: 4, value is: 0.
Current row: 1, current col: 0, value is: 1.
Current row: 1, current col: 1, value is: 1.
Current row: 1, current col: 2, value is: 0.
Current row: 1, current col: 3, value is: 0.
Current row: 1, current col: 4, value is: 0.
Current row: 2, current col: 0, value is: 0.
Current row: 2, current col: 1, value is: 0.
Current row: 2, current col: 2, value is: 1.
Current row: 2, current col: 3, value is: 0.
Current row: 2, current col: 4, value is: 0.
Current row: 3, current col: 0, value is: 0.
Current row: 3, current col: 1, value is: 0.
Current row: 3, current col: 2, value is: 0.
Current row: 3, current col: 3, value is: 1.
Current row: 3, current col: 4, value is: 1.
Number of island: 3.

Time complexity: O(m x n)
Space complexity: O(m x n)
"""
