from typing import List


def main(nums: List[int]) -> int:
    print(f"Original array: {nums}\n")
    hash_table = {}
    for i in nums:
        if i in hash_table:
            hash_table[i] += 1
        else:
            hash_table[i] = 1
    print(f"Hash table now: {hash_table}.")
    for i in hash_table:
        if hash_table[i] == 1:
            print(f"Found {i} one time.")
            return i


main(nums=[4, 1, 1])

"""
Output:
Original array: [4, 1, 1]

Hash table now: {4: 1, 1: 2}.
Found 4 one time.
"""
# Time complexity - O(n)
# Space complexity - O(n)
