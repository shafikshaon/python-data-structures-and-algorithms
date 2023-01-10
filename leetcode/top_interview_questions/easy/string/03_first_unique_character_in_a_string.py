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

# Time complexity - O(n)
# Space complexity - O(1)
