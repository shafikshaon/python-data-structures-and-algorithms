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

# Time complexity - O(n)
# Space complexity - O(1)
