from typing import List


def is_bad_version(mid, bad):
    return mid == bad


def main(n: int, bad: int) -> int:
    print(f"The n: {n} and bad version is: {bad}.")
    left = 1
    right = n

    while left < right:
        mid = (left + right) // 2
        print(f"Current left is: {left}, right is: {right}, and mid is: {mid}.")
        if is_bad_version(mid, bad):
            right = mid
        else:
            left = mid + 1
        print(f"Now left is: {left} and right is: {right}.")
    print(f"Found bad version: {left}.\n")
    return left


main(n=5, bad=4)
main(n=1, bad=1)

# Output
"""
The n: 5 and bad version is: 4.
Current left is: 1, right is: 5, and mid is: 3.
Now left is: 4 and right is: 5.
Current left is: 4, right is: 5, and mid is: 4.
Now left is: 4 and right is: 4.
Found bad version: 4.

The n: 1 and bad version is: 1.
Found bad version: 1.
"""

# Time complexity - O(log(n))
# Space complexity - O(1)
