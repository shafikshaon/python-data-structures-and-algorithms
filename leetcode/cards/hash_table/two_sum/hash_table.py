from typing import List


def main(nums: List[int], target: int) -> List[int]:
    print(f"Original array: {nums}.\n")
    hash_table = {}
    for i in range(len(nums)):
        print(f"Current index {i}, value {nums[i]}.")
        print(
            f"Complement {target - nums[i]} = {target} - {nums[i]} (complement = target - nums[i])."
        )
        complement = target - nums[i]
        if complement in hash_table:
            print(f"\nReturn the result: {[i, hash_table[complement]]}.")
            return [i, hash_table[complement]]
        else:
            hash_table[nums[i]] = i
        print(f"Current hash table {hash_table}.\n")


main(nums=[2, 7, 11, 15], target=9)

"""
Output:
Original array: [2, 7, 11, 15].

Current index 0, value 2.
Complement 7 = 9 - 2 (complement = target - nums[i]).
Current hash table {2: 0}.

Current index 1, value 7.
Complement 2 = 9 - 7 (complement = target - nums[i]).

Return the result: [1, 0].
"""
# Time complexity - O(n)
# Space complexity - O(1)
