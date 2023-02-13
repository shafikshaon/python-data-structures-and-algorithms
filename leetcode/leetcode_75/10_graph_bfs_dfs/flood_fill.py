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

    def display_board(self, image: List[List[int]]):
        return (
                "\n".join(self.print_row(row) for row in image)
                + "\n "
                + "--- " * len(image[-1])
        )

    def flood_fill(self, image, sr, sc, new_color):
        row, col = len(image), len(image[0])
        color = image[sr][sc]
        if color == new_color:
            return image

        def dfs(r, c):
            if image[r][c] == color:
                image[r][c] = new_color
                if r >= 1:
                    dfs(r - 1, c)
                if r + 1 < row:
                    dfs(r + 1, c)
                if c >= 1:
                    dfs(r, c - 1)
                if c + 1 < col:
                    dfs(r, c + 1)

        dfs(sr, sc)
        return image


sol = Solution()
print(f"Input image:")
print(sol.display_board(image=[[1, 1, 1], [1, 1, 0], [1, 0, 1]]))
output = sol.flood_fill(
    image=[[1, 1, 1], [1, 1, 0], [1, 0, 1]], sr=1, sc=1, new_color=2
)
print(f"Output image:")
print(sol.display_board(output))

"""
Output:
Input image:
 ___ ___ ___  
| 1 | 1 | 1 |
 ___ ___ ___  
| 1 | 1 | 0 |
 ___ ___ ___  
| 1 | 0 | 1 |
 --- --- --- 
Output image:
 ___ ___ ___  
| 2 | 2 | 2 |
 ___ ___ ___  
| 2 | 2 | 0 |
 ___ ___ ___  
| 2 | 0 | 1 |
 --- --- --- 

Time Complexity: O(n)
Space Complexity: O(n)
"""
