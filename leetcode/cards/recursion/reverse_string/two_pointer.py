from typing import List


def main(s: List[str]) -> None:
    print(f"Original array: {s}.\n")
    start = 0
    end = len(s) - 1

    while start < end:
        print(f"Array s is now: {s}.")
        print(f"{s[start]} swap with {s[end]}.")
        s[start], s[end] = s[end], s[start]
        print(f"After swap the array s: {s}.\n")
        start, end = start + 1, end - 1
    print(f"After reversing the s is: {s}.")


main(s=["h", "e", "l", "l", "o"])

# Output
"""
Output:
Original array: ['h', 'e', 'l', 'l', 'o'].

Array s is now: ['h', 'e', 'l', 'l', 'o'].
h swap with o.
After swap the array s: ['o', 'e', 'l', 'l', 'h'].

Array s is now: ['o', 'e', 'l', 'l', 'h'].
e swap with l.
After swap the array s: ['o', 'l', 'l', 'e', 'h'].

After reversing the s is: ['o', 'l', 'l', 'e', 'h'].
"""

# Time complexity - O(n)
# Space complexity - O(1)
