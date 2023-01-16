def main(s: str) -> int:
    print(f"Input string is: {s}.\n")
    singles = set()
    length = 0

    for c in s:
        if c in singles:
            print(f'"{c}" remove from: {singles}.')
            singles.remove(c)
            length += 2
        else:
            print(f'"{c}" add to: {singles}.')
            singles.add(c)
        print(f"Character set now: {singles}.\n")
    if len(singles) > 0:
        length += 1
    print(f"Longest length of palindrome: {length}.")
    return length


main(s="abccccdd")
print(
    "-----------------------------------------------------------------------------------------------------"
)
main(s="a")

# Time complexity: O(n)
# Space complexity: O(1)

# Output
"""

"""
