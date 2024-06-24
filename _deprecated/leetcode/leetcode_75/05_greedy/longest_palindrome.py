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
Input string is: abccccdd.

"a" add to: set().
Character set now: {'a'}.

"b" add to: {'a'}.
Character set now: {'b', 'a'}.

"c" add to: {'b', 'a'}.
Character set now: {'b', 'a', 'c'}.

"c" remove from: {'b', 'a', 'c'}.
Character set now: {'b', 'a'}.

"c" add to: {'b', 'a'}.
Character set now: {'b', 'a', 'c'}.

"c" remove from: {'b', 'a', 'c'}.
Character set now: {'b', 'a'}.

"d" add to: {'b', 'a'}.
Character set now: {'b', 'a', 'd'}.

"d" remove from: {'b', 'a', 'd'}.
Character set now: {'b', 'a'}.

Longest length of palindrome: 7.
-----------------------------------------------------------------------------------------------------
Input string is: a.

"a" add to: set().
Character set now: {'a'}.

Longest length of palindrome: 1.
"""
