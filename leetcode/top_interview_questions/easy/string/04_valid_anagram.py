def main(s: str, t: str) -> bool:
    print(f"Original value of s: {s}.")
    print(f"Original value of t: {t}.\n")

    if len(s) != len(t):
        print(f"The input string s ({s}) and t ({t}) length are not same.")
        return False

    d = {}
    print(f"Creating hash table for first input string: {s}.")
    for c in s:
        if c in d:
            d[c] += 1
        else:
            d[c] = 1
    print(f"After creating hash table the dictionary is: {d}.\n")
    print(
        "Loop through the second string and decrement the count of each letter in the dictionary\n"
    )

    for c in t:
        if c in d:
            print(f"Found {c} in d. So decrementing occurrence from hash table.")
            d[c] -= 1
            if d[c] < 0:
                print(
                    f"Character {c} appear more than first string: {s}. So, it's not valid anagram."
                )
                return False
        else:
            print(f"Character {c} not found in hash table. So, it's not valid anagram.")
            return False
    print(f"\nNow hash table is: {d}.")
    print("All the counts are 0, then t is an anagram of s")
    print(f'\n"{s}" is valid anagram.')
    return True


main(s="anagram", t="nagaram")

# Time complexity - O(n)
# Space complexity - O(1)

# Output:

"""
Original value of s: anagram.
Original value of t: nagaram.

Creating hash table for first input string: anagram.
After creating hash table the dictionary is: {'a': 3, 'n': 1, 'g': 1, 'r': 1, 'm': 1}.

Loop through the second string and decrement the count of each letter in the dictionary

Found n in d. So decrementing occurrence from hash table.
Found a in d. So decrementing occurrence from hash table.
Found g in d. So decrementing occurrence from hash table.
Found a in d. So decrementing occurrence from hash table.
Found r in d. So decrementing occurrence from hash table.
Found a in d. So decrementing occurrence from hash table.
Found m in d. So decrementing occurrence from hash table.

Now hash table is: {'a': 0, 'n': 0, 'g': 0, 'r': 0, 'm': 0}.
All the counts are 0, then t is an anagram of s

"anagram" is valid anagram.
"""
