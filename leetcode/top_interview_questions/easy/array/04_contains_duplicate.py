from typing import List


def main(nums: List[int]) -> bool:
    hash_table = {}
    for i in nums:
        if i in hash_table:
            print(f"Found {i} already found in array.")
            print(f"Value appears at least twice: Yes")
            return True
        else:
            print(f"Value {i} push to hash table.")
            hash_table[i] = 1
    print(f"Value appears at least twice: No")
    return False


main(nums=[1, 2, 3, 4, 4])

# Time complexity - O(n)
# Space complexity - O(n)
