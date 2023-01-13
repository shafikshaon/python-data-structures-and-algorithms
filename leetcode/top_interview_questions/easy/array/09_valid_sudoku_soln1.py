from typing import List


def display_board(board: List[List[str]]) -> None:
    print("-" * 37)
    for i, row in enumerate(board):
        print(
            ("|" + " {}   {}   {} |" * 3).format(*[x if x != 0 else " " for x in row])
        )
        if i == 8:
            print("-" * 37)
        elif i % 3 == 2:
            print("|" + "---+" * 8 + "---|")
        else:
            print("|" + " - -" * 8 + " - |")


def main(board: List[List[str]]) -> bool:
    print("Original sudoku board:")
    display_board(board)

    rows = [set() for _ in range(9)]
    cols = [set() for _ in range(9)]
    boxes = [set() for _ in range(9)]

    for r in range(9):
        for c in range(9):
            val = board[r][c]

            if val == ".":
                continue

            if val in rows[r]:
                print("Sudoku is invalid.\n")
                print(
                    f"Value {val} found in row {r} column {c}. it's already in the same row."
                )
                return False
            rows[r].add(val)

            if val in cols[c]:
                print("Sudoku is invalid.\n")
                print(
                    f"Value {val} found in row {r} column {c}. it's already in the same col."
                )
                return False
            cols[c].add(val)

            idx = (r // 3) * 3 + c // 3
            if val in boxes[idx]:
                print("Sudoku is invalid.\n")
                print(f"Value {val} already in box {idx}. Row {r} and col {c}.")
                return False
            boxes[idx].add(val)
    print("Sudoku is valid.\n")
    return True


main(
    board=[
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"],
    ]
)

main(
    board=[
        ["8", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"],
    ]
)

# Time complexity - O(n^2)
# Space complexity - O(n^2)
