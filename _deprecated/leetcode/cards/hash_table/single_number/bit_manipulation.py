from typing import List


def main(nums: List[int]) -> int:
    print(f"Original array: {nums}\n")
    a: int = 0
    for i in nums:
        print(f"Current number is: {i} and after applying XOR ({a} ^ {i}): {a ^ i}")
        print(f"{a:08b}")
        print(f"{i:08b}")
        print("--------")
        print(f"{a ^ i:08b} ({a ^ i})")
        print("")
        a ^= i
    return a


main(nums=[4, 1, 1])

"""
Output:
Original array: [4, 1, 1]

Current number is: 4 and after applying XOR (0 ^ 4): 4
00000000
00000100
--------
00000100 (4)

Current number is: 1 and after applying XOR (4 ^ 1): 5
00000100
00000001
--------
00000101 (5)

Current number is: 1 and after applying XOR (5 ^ 1): 4
00000101
00000001
--------
00000100 (4)
"""
# Time complexity - O(n)
# Space complexity - O(1)
