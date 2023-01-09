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

# Time complexity - O(n)
# Space complexity - O(1)
