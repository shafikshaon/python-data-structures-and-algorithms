from typing import List


def main(nums1: List[int], nums2: List[int]) -> List[int]:
    answer = []
    hash_table = {}
    for n in nums1:
        if n in hash_table:
            continue
        else:
            hash_table[n] = 1
    print(f"Hash table now: {hash_table}.")
    nums2 = set(nums2)
    for n in nums2:
        if n in hash_table and hash_table[n] == 1:
            answer.append(n)
    print(f"Output is: {answer}.")
    return answer


main(nums1=[1, 2, 2, 1], nums2=[2, 2])

"""
Output:
Hash table now: {1: 1, 2: 1}.
Output is: [2].
"""
# Time complexity - O(n)
# Space complexity - O(n)
