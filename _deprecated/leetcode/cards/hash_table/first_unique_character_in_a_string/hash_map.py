import collections


def main(s: str) -> int:
    print(f"Original value: {s}.\n")
    count = collections.Counter(s)

    print(f"Elements with occurrences: {count}.\n")

    for idx, c in enumerate(s):
        print(f"Current character {c}, index {idx}, and occurrences {count[c]}.")
        if count[c] == 1:
            print(f"\nFound first non-repeating character at index {idx}.")
            return idx
    return -1


main(s="loveleetcode")

"""
Output:
Original value: loveleetcode.

Elements with occurrences: Counter({'e': 4, 'l': 2, 'o': 2, 'v': 1, 't': 1, 'c': 1, 'd': 1}).

Current character l, index 0, and occurrences 2.
Current character o, index 1, and occurrences 2.
Current character v, index 2, and occurrences 1.

Found first non-repeating character at index 2.
"""

# Time complexity - O(n)
# Space complexity - O(1)
