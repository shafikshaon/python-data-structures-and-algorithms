def main(s, t):
    mapping_st = {}
    mapping_ts = {}
    for c1, c2 in zip(s, t):
        if c1 not in mapping_st and c2 not in mapping_ts:
            print(f'Adding "{c2}" to mapping_st and "{c1}" to mapping_ts.')
            mapping_st[c1] = c2
            mapping_ts[c2] = c1
        elif mapping_st.get(c1) != c2 or mapping_ts.get(c2) != c1:
            print(f"mapping_st: {mapping_st}, mapping_ts: {mapping_ts}.")
            print(f"{mapping_st.get(c1)} != {c2} or {mapping_st.get(c2)} != {c1}")
            print(f'The "{s}" and "{t}" are not isomorphic.')
            return False
    print(f"mapping_st: {mapping_st}, mapping_ts: {mapping_ts}.")
    print(f'The "{s}" and "{t}" are isomorphic.')
    return True


main(s = "egg", t = "add")

"""
Output:
Adding "a" to mapping_st and "e" to mapping_ts.
Adding "d" to mapping_st and "g" to mapping_ts.
mapping_st: {'e': 'a', 'g': 'd'}, mapping_ts: {'a': 'e', 'd': 'g'}.
The "egg" and "add" are isomorphic.
"""
# Time complexity - O(n)
# Space complexity - O(1) since the size of the ASCII character set is fixed and the keys in our dictionary are all
# valid ASCII characters according to the problem statement.
